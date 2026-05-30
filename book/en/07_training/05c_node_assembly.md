# Physical Node Assembly

Once the interconnection PCB is ready, the next step is to physically assemble all the components inside the waterproof enclosure to protect the electronics and sensors from the outdoor weather. Below is the step-by-step process.

## Enclosure and Cable Preparation

### 1. Empty enclosure
We begin with the empty waterproof enclosure, which already has the three cable gland holes on one of its sides ({numref}`fig-assembly-1-en`).

```{figure} ../../_static/assembly/1.png
---
name: fig-assembly-1-en
width: 60%
align: center
---
Empty waterproof enclosure with the three cable holes.
```

### 2. Cable glands placement
We must place the cable glands in these holes to guarantee a proper seal for the incoming cables ({numref}`fig-assembly-2-en`).

```{figure} ../../_static/assembly/2.png
---
name: fig-assembly-2-en
width: 60%
align: center
---
Cable glands placed in the enclosure's holes.
```

### 3. Cable distribution
To maintain a neat layout, we define which cable passes through which gland ({numref}`fig-assembly-3-en`):
- **Top left:** Solar panel cable.
- **Top right:** Temperature probe cable.
- **Bottom:** Soil moisture sensor cable.

```{figure} ../../_static/assembly/3.png
---
name: fig-assembly-3-en
width: 60%
align: center
---
Cable distribution through the cable glands.
```

## Preliminary Soldering and Connections

### 4. USB Jack and sensors
We solder the USB Jack connector that will allow us to plug the solar panel into the Heltec node. In addition, we prepare the temperature probe by soldering its corresponding XTH connector ({numref}`fig-assembly-4-en`).

```{figure} ../../_static/assembly/4.png
---
name: fig-assembly-4-en
width: 60%
align: center
---
Prepared connections (USB Jack for the solar panel and XTH connector for temperature).
```

### 5. Light sensor
This step also involves soldering. The light sensor cables are connected to the XTH terminal, ensuring the proper color correspondence is maintained ({numref}`fig-assembly-5b-en`).

```{figure} ../../_static/assembly/5_b.png
---
name: fig-assembly-5b-en
width: 60%
align: center
---
Light sensor cables soldered to the XTH connector.
```

### 6. Battery cables
We also prepare the connector and the corresponding cables that will go to the node's battery ({numref}`fig-assembly-6-en`).

```{figure} ../../_static/assembly/6.png
---
name: fig-assembly-6-en
width: 60%
align: center
---
Prepared wiring for the battery.
```

## 3D Bracket Mounting

To secure the board and the battery inside the enclosure, we use a 3D-printed bracket.

### 7. Battery bracket
{numref}`fig-assembly-7-en` shows the assembly and appearance of the 3D bracket, which will house the battery.

```{figure} ../../_static/assembly/7.png
---
name: fig-assembly-7-en
width: 60%
align: center
---
3D bracket designed for the battery and the board.
```

### 8. Bracket assembly
We screw the PCB (with the Heltec module already mounted) onto the 3D bracket ({numref}`fig-assembly-8-en`). It should be placed directly in the correct position as shown in {numref}`fig-assembly-9-en`.

```{figure} ../../_static/assembly/8.png
---
name: fig-assembly-8-en
width: 60%
align: center
---
PCB and Heltec module screwed onto the 3D bracket.
```

```{figure} ../../_static/assembly/9.png
---
name: fig-assembly-9-en
width: 60%
align: center
---
Correct position of the board on the bracket.
```

## Final Assembly

### 9. Light sensor installation
To install the light sensor in the enclosure, we must apply a drop of adhesive and place it in its final position, connecting it to the board as shown in the following figures ({numref}`fig-assembly-10-en` and {numref}`fig-assembly-11-en`).

```{figure} ../../_static/assembly/10.png
---
name: fig-assembly-10-en
width: 60%
align: center
---
Applying an adhesive drop to install the light sensor.
```

```{figure} ../../_static/assembly/11.png
---
name: fig-assembly-11-en
width: 60%
align: center
---
Position and connection of the light sensor to the board.
```

### 10. Antenna connection (SMA)
We install the antenna by connecting the elbow of the SMA connector ({numref}`fig-assembly-12-en`).

```{figure} ../../_static/assembly/12.png
---
name: fig-assembly-12-en
width: 60%
align: center
---
Connecting the SMA connector elbow to the antenna.
```

### 11. Sensor and panel connections
We connect the USB cable (for the solar panel), as well as the temperature probe and soil moisture sensor cables to the board ({numref}`fig-assembly-13-en`).

```{figure} ../../_static/assembly/13.png
---
name: fig-assembly-13-en
width: 60%
align: center
---
USB cable, temperature probe and humidity sensor connected to the node.
```

### 12. Placement in the enclosure
Once the electronics are connected, we place the bracket with the board inside the waterproof enclosure and secure it by installing the two fixing screws ({numref}`fig-assembly-14-en`).

```{figure} ../../_static/assembly/14.png
---
name: fig-assembly-14-en
width: 60%
align: center
---
Bracket secured inside the waterproof enclosure with the two screws.
```

### 13. Solar panel support
Next, we screw the solar panel support to the printed part ({numref}`fig-assembly-15-en`).

```{figure} ../../_static/assembly/15.png
---
name: fig-assembly-15-en
width: 60%
align: center
---
Solar panel support screwed to the printed part.
```

### 14. Completed node
Finally, we close the enclosure. {numref}`fig-assembly-16-en` shows what the fully assembled physical node looks like in the end.

```{figure} ../../_static/assembly/16.png
---
name: fig-assembly-16-en
width: 60%
align: center
---
Final look of the completely assembled node.
```
