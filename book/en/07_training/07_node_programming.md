# IoT Node Programming

Firmware development for the ESP32 will preferably be done in **PlatformIO** or the **Arduino IDE**, using C/C++. The final goal is to read the sensors, pack the data ultra-efficiently, and send it via LoRaWAN, minimizing the time the microcontroller spends powered on.

## 0. Environment Pre-configuration (Arduino IDE)

Before writing any code, we must prepare our development environment so that it recognizes the **Heltec LoRa32 V3** board and has the necessary libraries:

1. **ESP32 Board Manager**: In the Arduino IDE preferences, add the Espressif board manager URL (`https://espressif.github.io/arduino-esp32/package_esp32_index.json`). Then, go to the "Boards Manager" and install the **esp32** platform.
2. **Board Selection**: Select the **Heltec WiFi LoRa 32(V3) / Wireless shell(V3)** board from the `Tools > Board` menu.
3. **Library Installation**: Go to `Sketch > Include Library > Manage Libraries` and install the following base dependencies:
   - `MCCI LoRaWAN LMIC library` by IBM/MCCI (for the LoRaWAN stack).
   - `BH1750` by Christopher Laws (for the light sensor).
   - `OneWire` and `DallasTemperature` (for the humidity/temperature sensor).

*Note: If you prefer to use **PlatformIO** (VS Code), you can add these libraries directly under `lib_deps` in your `platformio.ini` file.*

## 1. Initial Sensor Tests (Local Reading)

Before integrating radio frequency communication (LoRaWAN), it is essential to test in isolation that the microcontroller can communicate with each sensor and obtain valid readings via the Serial Monitor.

For example, to check the I2C bus and the **BH1750** light sensor, we will create a basic script (without LoRa):

```cpp
#include <Wire.h>
#include <BH1750.h>

BH1750 luxSensor;

void setup() {
  Serial.begin(115200);
  Wire.begin(); // Initializes the I2C bus (default SDA and SCL pins)
  
  if (luxSensor.begin()) {
    Serial.println("BH1750 sensor started successfully.");
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

*This preliminary local validation step (correct hardware and wiring) will save you hours of debugging later on.*

## 2. Library Inclusion and MAC Logic
- **MCCI LoRaWAN LMIC library**: This is the standard implementation of the LoRaWAN stack for microcontrollers. Besides radio transmissions, it handles MAC layer logic, reception window timings (RX1/RX2), and strict compliance with the Duty Cycle (allowed time on air).
- **Wire.h**: Native library to control the I2C bus for the sensors.

## 3. Payload Optimization (Packing)

In LoRaWAN, every extra byte sent drastically reduces battery life and increases the chances of collision. **You should never send JSON strings or clear text**. Everything must be packed in binary.

Example of optimization via *bit shifting*:
If the temperature can vary between -10 and 50 ºC, instead of sending a `float` (4 bytes), we can send an `int16_t` (2 bytes) by multiplying the value by 10 or 100.

```cpp
// Example: Temperature 24.5 ºC -> 245
int16_t temp = (int16_t)(temperature_read * 10);
uint8_t payload[4];
payload[0] = temp >> 8;   // Most significant byte
payload[1] = temp & 0xFF; // Least significant byte

// Same for light or humidity
uint16_t light = read_lux();
payload[2] = light >> 8;
payload[3] = light & 0xFF;
```

## 4. Event-Driven Logic and LMIC

The LMIC library works via callbacks (events). The main flow of our program will be:
1. `setup()`: Initializes the LoRa chip, I2C/ADC sensors, and sets the OTAA keys (`DevEUI`, `AppEUI`, `AppKey`).
2. A *Join Request* is queued.
3. `EV_JOINED` event: The node has successfully joined. Periodic transmissions are enabled.
4. `EV_TXCOMPLETE` event: The packet has been transmitted and the reception windows are closed. **This is the exact moment to go to sleep.**

## 5. Extreme Power Management (Deep Sleep)

Instead of using the `delay()` function (which keeps the CPU consuming between 40 and 80 mA), we will use the ESP32's **Deep Sleep**.
In Deep Sleep, the RAM and CPU are turned off, reducing consumption to < 10 µA. Only the RTC (Real Time Clock) coprocessor stays on to wake up the chip after the stipulated time (e.g., 30 minutes).

Upon waking from Deep Sleep, the ESP32 executes the `setup()` function again. So that LMIC does not have to redo the *Join* process (which wastes a lot of battery), we will save the dynamic session keys in the ESP32's RTC RAM memory to recover them upon waking up.
