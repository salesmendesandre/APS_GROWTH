# Hardware y Materiales

Para llevar a cabo la monitorización del huerto en este taller, construiremos el nodo a partir de componentes discretos. Es fundamental conocer las especificaciones de cada elemento para garantizar la compatibilidad a nivel eléctrico y lógico.

## Módulo Principal: Heltec LoRa32 (ESP32)

```{figure} ../../_static/aps_growth/nodo_heltec.png
---
width: 50%
align: center
---
Módulo de desarrollo Heltec WiFi LoRa 32.
```

El cerebro de nuestro nodo ambiental es el módulo de desarrollo **Heltec WiFi LoRa 32**.

- **SoC (System on Chip)**: ESP32 dual-core a 240 MHz.
- **Conectividad**: WiFi (802.11 b/g/n), Bluetooth LE y un chip transceptor LoRa (SX1276 o SX1262 según versión) integrado en la misma placa.
- **Periféricos integrados**: Pantalla OLED SSD1306 de 0.96 pulgadas (conectada vía I2C) y circuito de gestión de carga para baterías.
- **Consumo**: Aunque el ESP32 es potente, puede entrar en modo *Deep Sleep*, reduciendo el consumo a unos pocos microamperios (µA). Desactivar periféricos no utilizados (como el WiFi) y apagar el OLED por software es vital para operaciones solares continuas.

## Sensores Ambientales

Integraremos un conjunto de sensores para medir variables críticas del ecosistema del huerto:

### 1. Sensor de Luz (BH1750)

```{figure} ../../_static/aps_growth/sensor_bh1750.jpg
---
width: 40%
align: center
---
Módulo del sensor digital de luz BH1750.
```

Sensor digital de luminosidad ambiental.
- **Interfaz**: I2C (Inter-Integrated Circuit).
- **Rango**: Mide de 1 a 65535 lux.
- **Ventaja**: Al ser digital, ofrece medidas precisas y directamente calibradas sin requerir ecuaciones complejas en el ADC del microcontrolador.

### 2. Sensores de Humedad del Suelo

```{figure} ../../_static/aps_growth/sensor_electrolito.png
---
width: 40%
align: center
---
Sensor capacitivo de humedad del suelo.
```

Para medir la cantidad de agua disponible para las raíces.
- **Interfaz**: Analógica. Genera una tensión variable que conectaremos a los pines ADC (Convertidor Analógico-Digital) del ESP32. 
- Habrá que calibrar empíricamente los valores en seco y en saturación de agua.

### 3. Sensores de Temperatura Ambiente (DS18B20)

```{figure} ../../_static/aps_growth/sensor_ds18b20.jpg
---
width: 40%
align: center
---
Sensor de temperatura digital sumergible DS18B20.
```

Permiten registrar las fluctuaciones térmicas que afectan a la germinación y el crecimiento de los cultivos en el huerto. El microcontrolador solicitará periódicamente el valor de este sensor antes de empaquetar la trama.
- **Interfaz**: OneWire. Este protocolo digital permite conectar múltiples sensores al mismo bus de datos utilizando un único pin del ESP32, lo que resulta muy eficiente en cableado.



## Infraestructura y Gestión Energética

### Panel Solar y Batería
El objetivo de un nodo sensor remoto es la autonomía absoluta. Para ello, utilizamos:

```{figure} ../../_static/aps_growth/panel_solar.png
---
width: 40%
align: center
---
Panel solar de 5V.
```

- **Panel Solar 5V**: Proporciona energía suficiente para recargar el sistema durante el día.

```{figure} ../../_static/aps_growth/bateria_lipo.png
---
width: 40%
align: center
---
Batería LiPo de 3.7V y 1000 mAh.
```

- **Batería LiPo de 3.7V y 1000 mAh**: Almacena el excedente energético para soportar los consumos nocturnos y mantener el nodo vivo en periodos de lluvia o nubosidad prolongada.

### Caja Estanca Transparente
Para proteger la electrónica de la lluvia, la humedad y el polvo ambiental, todos los elementos se introducen en una envolvente plástica. La tapa transparente permite que la luz exterior penetre en la carcasa, lo que nos da la ventaja de poder instalar el sensor de luminosidad (BH1750) en su interior, manteniéndolo perfectamente protegido de la intemperie.

```{figure} ../../_static/aps_growth/caja_estanca.png
---
width: 50%
align: center
---
Caja estanca transparente para protección del nodo.
```

---

### Arquitectura Completa del Nodo

El siguiente diagrama ilustra cómo se interconectan lógicamente todos los componentes (microcontrolador, módulos de radio y sensores) dentro de nuestro nodo de monitorización:

```{figure} ../../_static/generated/diagrams/es/lorawan_hardware.svg
---
width: 100%
align: center
---
Diagrama de bloques del hardware del nodo IoT.
```

### Gateway LoRa Heltec HT-M7603 Indoor

Para recibir los datos de nuestros nodos y reenviarlos a The Things Network a través de Internet, utilizamos el **Heltec HT-M7603 Indoor LoRaWAN Gateway**. Este equipo actuará como el puente entre nuestra red de radiofrecuencia (RF) local y la red global.

```{figure} ../../_static/aps_growth/heltec_mt7603.png
---
width: 60%
align: center
---
Gateway Heltec HT-M7603 Indoor.
```

Para dotarlo de mayor alcance, al Gateway se le conectará una **Antena Exterior LoRa** de alta ganancia mediante un cable extensor SMA.

```{figure} ../../_static/aps_growth/antena_lora_sma.jpg
---
width: 60%
align: center
---
Antena exterior LoRa con cable SMA.
```

- Para maximizar la cobertura, la antena debe situarse en el punto más elevado posible (como el tejado o la fachada alta del edificio) y con visión directa al huerto (*Line of Sight*), despejando así la "zona de Fresnel" de obstáculos físicos.

