# Interconnection PCB

After learning about the available hardware and sensors, it is necessary to assemble all the components. To facilitate the connection of the sensors and the Heltec node, we use a custom-designed Printed Circuit Board (PCB) for the project.

## PCB Faces

The board has two distinct faces that will guide us during assembly:

1. **Front face (with silkscreen):** This is the face that includes descriptive text (such as "SEN_1", "SEN_2", etc.), indicating the location of each sensor. This face is shown in {numref}`fig-pcb-front-en`.
2. **Back face:** This is the opposite side, which has no text, as seen in {numref}`fig-pcb-back-en`.

As we will see, some components must be soldered on one side and others on the other. Therefore, before soldering, we must check that we are doing it on the correct side, as soldering on the wrong side will cause the pins not to match.

```{figure} ../../_static/pcb/2.png
---
name: fig-pcb-front-en
width: 60%
align: center
---
Front face of the PCB with silkscreen (text indicators).
```

```{figure} ../../_static/pcb/1.png
---
name: fig-pcb-back-en
width: 60%
align: center
---
Back face of the PCB (no text).
```

## Step-by-Step Assembly

The recommended order for soldering the different components is detailed below.

### 1. Headers for the Heltec node

The first step is to solder the female pin headers that will be used to attach the Heltec module. As seen in {numref}`fig-pcb-heltec-pins-en`, these pins must be inserted and placed on the **back face** of the PCB.

```{figure} ../../_static/pcb/3.png
---
name: fig-pcb-heltec-pins-en
width: 60%
align: center
---
Female pin headers for connecting the Heltec node.
```

### 2. Connectors for sensors

The next step is to add the connectors where the sensors will be plugged in. According to {numref}`fig-pcb-connectors-en`, we will also place these connectors on the **back face**:

- A **5-pin XTH** connector for the light sensor.
- A **3-pin XTH** connector for the ambient temperature sensor.
- **4-pin terminals** for the humidity sensor converter.

```{figure} ../../_static/pcb/4.png
---
name: fig-pcb-connectors-en
width: 60%
align: center
---
XTH connectors and terminals for the humidity converter.
```

### 3. Humidity converter module

Once the 4-pin terminals are soldered, we can connect the soil moisture converter module into that socket, as shown in {numref}`fig-pcb-converter-en`. Remember that these pins and terminals go on the back face.

```{figure} ../../_static/pcb/5.png
---
name: fig-pcb-converter-en
width: 60%
align: center
---
Humidity converter module connected to the PCB.
```

### 4. Pull-up resistor (OneWire)

In the corresponding location (shown in {numref}`fig-pcb-resistor-en`), we include a $10\text{ k}\Omega$ resistor. This pull-up resistor is necessary for the OneWire communication interface, which is used by some of the project's sensors.

```{figure} ../../_static/pcb/6.png
---
name: fig-pcb-resistor-en
width: 60%
align: center
---
10 kΩ pull-up resistor for the OneWire interface.
```

### 5. Heltec node insertion

Finally, to complete the assembled PCB, we can plug the Heltec module into the corresponding side ({numref}`fig-pcb-heltec-final-en`).

```{figure} ../../_static/pcb/7.png
---
name: fig-pcb-heltec-final-en
width: 60%
align: center
---
Fully assembled PCB with the Heltec module.
```
