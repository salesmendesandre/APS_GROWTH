# Hardware and Materials

To carry out the monitoring of the garden in this workshop, we will build the node from discrete components. It is essential to know the specifications of each element to ensure electrical and logical compatibility.

## Main Module: Heltec LoRa32 (ESP32)

```{figure} ../../_static/aps_growth/nodo_heltec.png
---
width: 50%
align: center
---
Heltec WiFi LoRa 32 development module.
```

The brain of our environmental node is the **Heltec WiFi LoRa 32** development module.

- **SoC (System on Chip)**: Dual-core ESP32 at 240 MHz.
- **Connectivity**: WiFi (802.11 b/g/n), Bluetooth LE, and a LoRa transceiver chip (SX1276 or SX1262 depending on the version) integrated on the same board.
- **Integrated peripherals**: 0.96-inch SSD1306 OLED display (connected via I2C) and battery charge management circuit.
- **Power Consumption**: Although the ESP32 is powerful, it can enter *Deep Sleep* mode, reducing consumption to a few microamperes (µA). Disabling unused peripherals (like WiFi) and turning off the OLED via software is vital for continuous solar operations.

## Environmental Sensors

We will integrate a set of sensors to measure critical variables of the garden ecosystem:

### 1. Light Sensor (BH1750)

```{figure} ../../_static/aps_growth/sensor_bh1750.jpg
---
width: 40%
align: center
---
BH1750 digital light sensor module.
```

Digital ambient light sensor.
- **Interface**: I2C (Inter-Integrated Circuit).
- **Range**: Measures from 1 to 65535 lux.
- **Advantage**: Being digital, it offers precise and directly calibrated measurements without requiring complex equations on the microcontroller's ADC.

### 2. Soil Moisture Sensors

```{figure} ../../_static/aps_growth/sensor_electrolito.png
---
width: 40%
align: center
---
Capacitive soil moisture sensor.
```

To measure the amount of water available for the roots.
- **Interface**: Analog. It generates a variable voltage that we will connect to the ADC (Analog-to-Digital Converter) pins of the ESP32.
- The dry and water saturation values will have to be calibrated empirically.

### 3. Ambient Temperature Sensors (DS18B20)

```{figure} ../../_static/aps_growth/sensor_ds18b20.jpg
---
width: 40%
align: center
---
DS18B20 digital waterproof temperature sensor.
```

They allow recording the thermal fluctuations that affect the germination and growth of crops in the garden. The microcontroller will periodically request the value of this sensor before packing the frame.
- **Interface**: OneWire. This digital protocol allows connecting multiple sensors to the same data bus using a single pin on the ESP32, which is very efficient in wiring.



## Infrastructure and Energy Management

### Solar Panel and Battery
The goal of a remote sensor node is absolute autonomy. For this, we use:

```{figure} ../../_static/aps_growth/panel_solar.png
---
width: 40%
align: center
---
5V solar panel.
```

- **5V Solar Panel**: Provides enough energy to recharge the system during the day.

```{figure} ../../_static/aps_growth/bateria_lipo.png
---
width: 40%
align: center
---
3.7V 1000 mAh LiPo Battery.
```

- **3.7V 1000 mAh LiPo Battery**: Stores excess energy to support nighttime consumption and keep the node alive during prolonged periods of rain or cloudiness.

### Transparent Waterproof Box
To protect the electronics from rain, humidity, and environmental dust, all elements are placed inside a plastic enclosure. The transparent cover allows ambient light to penetrate the case, giving us the advantage of installing the light sensor (BH1750) inside, keeping it perfectly protected from the weather.

```{figure} ../../_static/aps_growth/caja_estanca.png
---
width: 50%
align: center
---
Transparent waterproof box for node protection.
```

---

### Complete Node Architecture

The following diagram illustrates how all the components (microcontroller, radio modules, and sensors) are logically interconnected within our monitoring node:

```{figure} ../../_static/generated/diagrams/es/lorawan_hardware.svg
---
width: 100%
align: center
---
IoT node hardware block diagram.
```

### Heltec HT-M7603 Indoor LoRaWAN Gateway

To receive the data from our nodes and forward it to The Things Network via the Internet, we use the **Heltec HT-M7603 Indoor LoRaWAN Gateway**. This device will act as the bridge between our local radio frequency (RF) network and the global network.

```{figure} ../../_static/aps_growth/heltec_mt7603.png
---
width: 60%
align: center
---
Heltec HT-M7603 Indoor Gateway.
```

To give it a longer range, the Gateway will be connected to a high-gain **External LoRa Antenna** using an SMA extension cable.

```{figure} ../../_static/aps_growth/antena_lora_sma.jpg
---
width: 60%
align: center
---
External LoRa antenna with SMA cable.
```

- To maximize coverage, the antenna should be placed at the highest possible point (like the roof or the high facade of the building) and with a direct line of sight to the garden (*Line of Sight*), thus clearing the "Fresnel zone" of physical obstacles.

