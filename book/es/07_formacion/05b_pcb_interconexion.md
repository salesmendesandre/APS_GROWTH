# PCB de Interconexión

Tras conocer el hardware y los sensores disponibles, es necesario ensamblar todos los componentes. Para facilitar la conexión de los sensores y el nodo Heltec, utilizamos una Placa de Circuito Impreso (PCB) diseñada a medida para el proyecto.

## Caras de la PCB

La placa tiene dos caras bien diferenciadas que nos guiarán durante el ensamblaje:

1. **Cara frontal (con serigrafía):** Es la cara que incluye el texto descriptivo (como "SEN_1", "SEN_2", etc.), donde se indica la ubicación de cada sensor. Esta cara se muestra en la {numref}`fig-pcb-frontal`.
2. **Cara trasera:** Es la cara opuesta, que no incluye texto, tal y como se puede observar en la {numref}`fig-pcb-trasera`.

Como veremos, algunos componentes deben soldarse por un lado y otros por el otro. Por tanto, antes de proceder a soldar debemos comprobar que lo estamos haciendo en el lado correcto, ya que si lo soldamos del lado incorrecto los pines no van a corresponder.

```{figure} ../../_static/pcb/2.png
---
name: fig-pcb-frontal
width: 60%
align: center
---
Cara frontal de la PCB con serigrafía (indicadores de texto).
```

```{figure} ../../_static/pcb/1.png
---
name: fig-pcb-trasera
width: 60%
align: center
---
Cara trasera de la PCB (sin texto).
```

## Ensamblaje paso a paso

A continuación se detalla el orden recomendado para soldar los diferentes componentes. 

### 1. Zócalos para el nodo Heltec

El primer paso es soldar las tiras de pines (zócalos) que servirán para encajar el módulo Heltec. Como se observa en la {numref}`fig-pcb-heltec-pins`, estos pines deben insertarse y colocarse en la **cara trasera** de la placa. 

```{figure} ../../_static/pcb/3.png
---
name: fig-pcb-heltec-pins
width: 60%
align: center
---
Pines hembra para la conexión del nodo Heltec.
```

### 2. Conectores para los sensores

El siguiente paso es añadir los conectores donde se enchufarán los sensores. Según la {numref}`fig-pcb-conectores`, insertaremos estos conectores también en la **cara trasera**:

- Un conector **XTH** de **5 pines** para el sensor de luz.
- Un conector **XTH** de **3 pines** para el sensor de temperatura ambiente.
- Unos **terminales de 4 pines** para el convertidor del sensor de humedad.

```{figure} ../../_static/pcb/4.png
---
name: fig-pcb-conectores
width: 60%
align: center
---
Conectores XTH y terminales para el convertidor de humedad.
```

### 3. Módulo convertidor de humedad

Una vez soldados los terminales de 4 pines, ya podemos conectar el módulo convertidor de humedad del suelo, como se aprecia en la {numref}`fig-pcb-convertidor`. Recuerda que estos pines y terminales van por la parte trasera.

```{figure} ../../_static/pcb/5.png
---
name: fig-pcb-convertidor
width: 60%
align: center
---
Módulo convertidor de humedad conectado a la PCB.
```

### 4. Resistencia pull-up (OneWire)

En la ubicación correspondiente (mostrada en la {numref}`fig-pcb-resistencia`), incluimos una resistencia de $10\text{ k}\Omega$. Esta resistencia de *pull-up* es necesaria para la interfaz de comunicación OneWire, que utilizan algunos de los sensores del proyecto.

```{figure} ../../_static/pcb/6.png
---
name: fig-pcb-resistencia
width: 60%
align: center
---
Resistencia de pull-up de 10 kΩ para la interfaz OneWire.
```

### 5. Inserción del nodo Heltec

Por último, para terminar la PCB ensamblada, podemos encajar el módulo Heltec en el lado correspondiente ({numref}`fig-pcb-heltec-final`).

```{figure} ../../_static/pcb/7.png
---
name: fig-pcb-heltec-final
width: 60%
align: center
---
PCB completamente ensamblada con el módulo Heltec.
```
