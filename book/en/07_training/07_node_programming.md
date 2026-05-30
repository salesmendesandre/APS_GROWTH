# IoT Node Programming

```{admonition} Learning Objectives
:class: tip

At the end of this section, you should be able to:
- Set up the development environment (Arduino IDE or PlatformIO) for the microcontroller.
- Write basic code to read local sensors (I2C/ADC).
- Pack data into binary payloads to optimize transmission.
- Understand and apply the LoRaWAN power-saving cycle (Deep Sleep).
```

Developing firmware for the ESP32 will preferably be done in **PlatformIO** or the **Arduino IDE**, using C/C++. The ultimate goal is to read the sensors, pack the data ultra-efficiently, and send it via LoRaWAN, minimizing the time the microcontroller spends turned on.

## 0. Environment Setup (Arduino IDE)

Before writing code, we need to set up our development environment so it recognizes the **Heltec LoRa32 V3** board and has the necessary libraries:

1. **ESP32 Board Manager**: In the Arduino IDE preferences, add the Espressif board manager URL (`https://espressif.github.io/arduino-esp32/package_esp32_index.json`). Then, go to the "Board Manager" and install the **esp32** platform.
2. **Board Selection**: Select the **Heltec WiFi LoRa 32(V3) / Wireless shell(V3)** board from the `Tools > Board` menu.
3. **Library Installation**: Go to `Sketch > Include Library > Manage Libraries` and install the following core dependencies:
   - `MCCI LoRaWAN LMIC library` by IBM/MCCI (for the LoRaWAN stack).
   - `BH1750` by Christopher Laws (for the light sensor).
   - `OneWire` and `DallasTemperature` (for the moisture/temperature sensor).

*Note: If you prefer to use **PlatformIO** (VS Code), you can add these libraries directly under `lib_deps` in your `platformio.ini` file.*

## 1. Preliminary Sensor Testing (Local Reading)

Before integrating radio frequency communication (LoRaWAN), it is essential to test in isolation that the microcontroller can communicate with each sensor and get valid readings through the Serial Monitor.

For instance, to check the I2C bus and the **BH1750** light sensor, we'll create a basic script (without LoRa):

```cpp
#include <Wire.h>
#include <BH1750.h>

BH1750 luxSensor;

void setup() {
  Serial.begin(115200);
  Wire.begin(); // Initializes the I2C bus (SDA and SCL pins by default)
  
  if (luxSensor.begin()) {
    Serial.println("BH1750 sensor initialized correctly.");
  } else {
    Serial.println("Error: BH1750 not detected.");
  }
}

void loop() {
  uint16_t lux = luxSensor.readLightLevel();
  Serial.print("Ambient light: ");
  Serial.print(lux);
  Serial.println(" lux");
  delay(2000);
}
```

*This preliminary step of local validation (correct hardware and wiring) will save you hours of debugging later.*

## 2. Library Inclusion and MAC Logic
- **MCCI LoRaWAN LMIC library**: This is the standard LoRaWAN stack implementation for microcontrollers. Besides radio transmissions, it handles MAC layer logic, RX1/RX2 receive window timings, and strict Duty Cycle compliance (allowed time on air).
- **Wire.h**: Native library for controlling the sensors' I2C bus.

## 3. Payload Packing and Optimization

In LoRaWAN, every extra byte sent drastically reduces battery life and increases collision probabilities. **You should never send JSON strings or clear text**. Everything must be packed in binary.

Example of optimization using *bit shifting*:
If the temperature can range from -10 to 50 ºC, instead of sending a `float` (4 bytes), we can send an `int16_t` (2 bytes) by multiplying the value by 10 or 100.

```cpp
// Example: Temperature 24.5 ºC -> 245
int16_t temp = (int16_t)(temperature_read * 10);
uint8_t payload[4];
payload[0] = temp >> 8;   // Most significant byte
payload[1] = temp & 0xFF; // Least significant byte

// Same for light or moisture
uint16_t light = read_luxes();
payload[2] = light >> 8;
payload[3] = light & 0xFF;
```

## 4. Event-Driven Logic and LMIC

The LMIC library works via callbacks (events). Our program's main flow will be:
1. `setup()`: Initializes the LoRa chip, I2C/ADC sensors, and sets the OTAA keys (`DevEUI`, `AppEUI`, `AppKey`).
2. A *Join Request* is queued.
3. `EV_JOINED` Event: The node successfully joined. Periodic transmissions are enabled.
4. `EV_TXCOMPLETE` Event: The packet has been transmitted and the receive windows are closed. **This is the exact moment to go to sleep.**

## 5. Extreme Power Management (Deep Sleep)

Instead of using the `delay()` function (which keeps the CPU drawing between 40 and 80 mA), we'll use the ESP32's **Deep Sleep**.
In Deep Sleep, RAM and CPU are shut down, dropping consumption to < 10 µA. Only the RTC (Real Time Clock) coprocessor stays on to wake the chip up after the set time (e.g., 30 minutes).

When waking up from Deep Sleep, the ESP32 runs the `setup()` function again. So that LMIC doesn't have to redo the *Join* process (which drains a lot of battery), we'll save the dynamic session keys in the ESP32's RTC RAM memory to retrieve them upon waking.

```{figure} ../../_static/generated/diagrams/en/deep_sleep_flow.svg
---
width: 100%
align: center
---
Node lifecycle and Deep Sleep entry after completing transmission.
```

```{admonition} Self-Assessment
:class: dropdown

**1. Why shouldn't we send JSON over LoRaWAN?**
Because every character in a JSON takes at least 1 byte. Transmitting text drastically increases Time on Air, raising battery consumption and network collision probabilities. Binary packing must always be used.

**2. What happens to the ESP32's main RAM during Deep Sleep?**
The main RAM is completely powered off to save energy, losing all its data. Only the RTC RAM (powered by the real-time clock) retains data, such as LoRaWAN network session keys.
```
