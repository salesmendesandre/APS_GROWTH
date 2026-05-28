# Hardware y Materiales

Para llevar a cabo la monitorización del huerto en este taller, construiremos el nodo a partir de componentes discretos. Es fundamental conocer las especificaciones de cada elemento para garantizar la compatibilidad a nivel eléctrico y lógico.

## Módulo Principal: Heltec LoRa32 (ESP32)

El cerebro de nuestro nodo ambiental es el módulo de desarrollo **Heltec WiFi LoRa 32**.

- **SoC (System on Chip)**: ESP32 dual-core a 240 MHz.
- **Conectividad**: WiFi (802.11 b/g/n), Bluetooth LE y un chip transceptor LoRa (SX1276 o SX1262 según versión) integrado en la misma placa.
- **Periféricos integrados**: Pantalla OLED SSD1306 de 0.96 pulgadas (conectada vía I2C) y circuito de gestión de carga para baterías.
- **Consumo**: Aunque el ESP32 es potente, puede entrar en modo *Deep Sleep*, reduciendo el consumo a unos pocos microamperios (µA). Desactivar periféricos no utilizados (como el WiFi) y apagar el OLED por software es vital para operaciones solares continuas.

## Sensores Ambientales

Integraremos un conjunto de sensores para medir variables críticas del ecosistema del huerto:

### 1. Sensor de Luz (BH1750)
Sensor digital de luminosidad ambiental.
- **Interfaz**: I2C (Inter-Integrated Circuit).
- **Rango**: Mide de 1 a 65535 lux.
- **Ventaja**: Al ser digital, ofrece medidas precisas y directamente calibradas sin requerir ecuaciones complejas en el ADC del microcontrolador.

### 2. Sensores de Humedad del Suelo
Para medir la cantidad de agua disponible para las raíces.
- **Interfaz**: Analógica. Genera una tensión variable que conectaremos a los pines ADC (Convertidor Analógico-Digital) del ESP32. 
- Habrá que calibrar empíricamente los valores en seco y en saturación de agua.

### 3. Sensores de Temperatura Ambiente
Permiten registrar las fluctuaciones térmicas que afectan a la germinación y el crecimiento de los cultivos en el huerto. El microcontrolador solicitará periódicamente el valor de este sensor antes de empaquetar la trama.

## Infraestructura y Gestión Energética

### Panel Solar y Batería
El objetivo de un nodo sensor remoto es la autonomía absoluta. Para ello, utilizamos:
- **Panel Solar 24V CC 6W**: Proporciona energía suficiente para recargar el sistema durante el día.
- **Batería de 7200 mAh**: Almacena el excedente energético para soportar los consumos nocturnos y mantener el nodo vivo en periodos de lluvia o nubosidad prolongada.

### Caja Estanca Transparente
Para proteger la electrónica de la lluvia, la humedad y el polvo ambiental, todos los elementos se introducen en una envolvente plástica. La tapa transparente permite observar la pantalla OLED durante el proceso de depuración sin necesidad de abrir la carcasa exponiendo los cables.

### Gateway LoRa Heltec LoRaWAN
El puente entre nuestra red LoRa RF y el Network Server en Internet.
- Estará equipado con una **Antena Exterior LoRa** de alta ganancia.
- Para maximizar la cobertura, la antena debe situarse en el punto más elevado posible y con visión directa al huerto (*Line of Sight*), despejando así la "zona de Fresnel" de obstáculos físicos.
