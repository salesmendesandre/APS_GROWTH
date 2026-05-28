# Physical Assembly and Deployment

With the firmware validated in the lab, the next step is the physical integration of the node and its field deployment.

## 1. Electrical Schematic

Before soldering or connecting wires, it is imperative to review the connection schematic.
- **I2C Bus**: The SDA and SCL pins of the Heltec module must go to the equivalent pins of the BH1750 (Light Sensor), adding pull-up resistors if the sensor module does not integrate them.
- **Sensor power supply**: It is preferable to power the sensors from a GPIO pin that acts as a power switch (`Vext` on some Heltec boards). In this way, before sleeping, the ESP32 completely turns off the sensors by cutting their VCC, saving milliamperes.

## 2. Integration in a Waterproof Box

Harsh weather conditions are the main enemy of an IoT node.
- The Heltec module and the battery will be placed in a **transparent waterproof box**.
- The use of cable glands (waterproof cable pass-throughs) is vital in the holes where the cables for the soil moisture and ambient temperature sensors exit.
- The LoRa antenna (usually a U.FL to SMA pigtail) must be screwed firmly to the chassis of the box, ensuring that it is vertical and out of the interference of the solar panel.

## 3. Solar Panel Connection

The 24V DC 6W solar panel cannot be connected directly to the Heltec module, as the voltage would fry the internal regulator of the ESP32.
- **MPPT/Step-down Regulator**: An intermediate module is necessary to reduce and stabilize the panel voltage to the charging parameters of the lithium battery (typically 4.2V max), protecting against overcharging and over-discharging.

## 4. Deployment in the Garden

In the educational garden:
1. **Location**: The solar panel should face South (in the northern hemisphere) with an optimal inclination to maximize winter insolation.
2. **Sensors**: The capacitive moisture sensor is buried in the soil near the roots of a representative crop. The ambient temperature sensor must be in the shade or protected from direct radiation to avoid falsely high readings.
3. The light sensor (BH1750) will remain inside the transparent waterproof box pointing towards the sky.
