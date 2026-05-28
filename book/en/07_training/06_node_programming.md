# IoT Node Programming

Firmware development for the ESP32 will preferably be done in **PlatformIO** or the **Arduino IDE**, using C/C++. The goal is to read the sensors, pack the data ultra-efficiently, and send it via LoRaWAN, minimizing the time the microcontroller spends powered on.

## 1. Required Libraries
- **MCCI LoRaWAN LMIC library**: The standard implementation of the LoRaWAN stack for microcontrollers. It handles MAC logic, RX1/RX2 timings, and Duty Cycle.
- **Wire.h** and specific libraries (such as `BH1750.h` or those for temperature/humidity sensors).

## 2. Sensor Reading and Payload Optimization (Packing)

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

## 3. Event-Driven Logic and LMIC

The LMIC library works via callbacks (events). The main flow of our program will be:
1. `setup()`: Initializes the LoRa chip, I2C/ADC sensors, and sets the OTAA keys (`DevEUI`, `AppEUI`, `AppKey`).
2. A *Join Request* is queued.
3. `EV_JOINED` event: The node has successfully joined. Periodic transmissions are enabled.
4. `EV_TXCOMPLETE` event: The packet has been transmitted and the reception windows are closed. **This is the exact moment to go to sleep.**

## 4. Extreme Power Management (Deep Sleep)

Instead of using the `delay()` function (which keeps the CPU consuming between 40 and 80 mA), we will use the ESP32's **Deep Sleep**.
In Deep Sleep, the RAM and CPU are turned off, reducing consumption to < 10 µA. Only the RTC (Real Time Clock) coprocessor stays on to wake up the chip after the stipulated time (e.g., 30 minutes).

Upon waking from Deep Sleep, the ESP32 executes the `setup()` function again. So that LMIC does not have to redo the *Join* process (which wastes a lot of battery), we will save the dynamic session keys in the ESP32's RTC RAM memory to recover them upon waking up.
