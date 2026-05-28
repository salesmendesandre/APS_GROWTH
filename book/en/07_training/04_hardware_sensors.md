# Hardware and Materials

To carry out the monitoring of the garden in this workshop, we will build the node from discrete components. It is essential to know the specifications of each element to ensure electrical and logical compatibility.

## Main Module: Heltec LoRa32 (ESP32)

The brain of our environmental node is the **Heltec WiFi LoRa 32** development module.

- **SoC (System on Chip)**: Dual-core ESP32 at 240 MHz.
- **Connectivity**: WiFi (802.11 b/g/n), Bluetooth LE, and a LoRa transceiver chip (SX1276 or SX1262 depending on the version) integrated on the same board.
- **Integrated peripherals**: 0.96-inch SSD1306 OLED display (connected via I2C) and battery charge management circuit.
- **Power Consumption**: Although the ESP32 is powerful, it can enter *Deep Sleep* mode, reducing consumption to a few microamperes (µA). Disabling unused peripherals (like WiFi) and turning off the OLED via software is vital for continuous solar operations.

## Environmental Sensors

We will integrate a set of sensors to measure critical variables of the garden ecosystem:

### 1. Light Sensor (BH1750)
Digital ambient light sensor.
- **Interface**: I2C (Inter-Integrated Circuit).
- **Range**: Measures from 1 to 65535 lux.
- **Advantage**: Being digital, it offers precise and directly calibrated measurements without requiring complex equations on the microcontroller's ADC.

### 2. Soil Moisture Sensors
To measure the amount of water available for the roots.
- **Interface**: Analog. It generates a variable voltage that we will connect to the ADC (Analog-to-Digital Converter) pins of the ESP32.
- The dry and water saturation values will have to be calibrated empirically.

### 3. Ambient Temperature Sensors
They allow recording the thermal fluctuations that affect the germination and growth of crops in the garden. The microcontroller will periodically request the value of this sensor before packing the frame.

```{figure} ../../_static/generated/diagrams/es/lorawan_hardware.svg
---
width: 100%
align: center
---
IoT node hardware block diagram.
```

## Infrastructure and Energy Management

### Solar Panel and Battery
The goal of a remote sensor node is absolute autonomy. For this, we use:
- **24V DC 6W Solar Panel**: Provides enough energy to recharge the system during the day.
- **7200 mAh Battery**: Stores excess energy to support nighttime consumption and keep the node alive during prolonged periods of rain or cloudiness.

### Transparent Waterproof Box
To protect the electronics from rain, humidity, and environmental dust, all elements are placed inside a plastic enclosure. The transparent cover allows observing the OLED screen during the debugging process without having to open the case and expose the wires.

### Heltec LoRaWAN Gateway
The bridge between our LoRa RF network and the Network Server on the Internet.
- It will be equipped with a high-gain **External LoRa Antenna**.
- To maximize coverage, the antenna should be placed at the highest possible point and with a direct view of the garden (*Line of Sight*), thus clearing the "Fresnel zone" of physical obstacles.
