# Programación del Nodo IoT

El desarrollo del firmware para el ESP32 se realizará preferiblemente en **PlatformIO** o en el **Arduino IDE**, utilizando C/C++. El objetivo final es leer los sensores, empaquetar los datos de forma ultra-eficiente y enviarlos vía LoRaWAN, minimizando el tiempo que el microcontrolador pasa encendido.

## 0. Preconfiguración del Entorno (Arduino IDE)

Antes de escribir código, debemos preparar nuestro entorno de desarrollo para que reconozca la placa **Heltec LoRa32 V3** y disponga de las librerías necesarias:

1. **Gestor de Tarjetas ESP32**: En las preferencias de Arduino IDE, añade la URL del gestor de tarjetas de Espressif (`https://espressif.github.io/arduino-esp32/package_esp32_index.json`). Luego, ve a "Gestor de Tarjetas" e instala la plataforma **esp32**.
2. **Selección de Placa**: Selecciona la placa **Heltec WiFi LoRa 32(V3) / Wireless shell(V3)** en el menú `Herramientas > Placa`.
3. **Instalación de Librerías**: Ve a `Programa > Incluir Librería > Gestionar Librerías` e instala las siguientes dependencias base:
   - `MCCI LoRaWAN LMIC library` de IBM/MCCI (para el stack LoRaWAN).
   - `BH1750` de Christopher Laws (para el sensor de luz).
   - `OneWire` y `DallasTemperature` (para el sensor de humedad/temperatura).

*Nota: Si prefieres utilizar **PlatformIO** (VS Code), puedes añadir estas librerías directamente bajo `lib_deps` en tu archivo `platformio.ini`.*

## 1. Pruebas Previas de Sensores (Lectura Local)

Antes de integrar la comunicación de radiofrecuencia (LoRaWAN), es fundamental probar de manera aislada que el microcontrolador puede comunicarse con cada sensor y obtener lecturas válidas a través del Monitor Serie.

Por ejemplo, para comprobar el bus I2C y el sensor de luminosidad **BH1750**, crearemos un script básico (sin LoRa):

```cpp
#include <Wire.h>
#include <BH1750.h>

BH1750 luxSensor;

void setup() {
  Serial.begin(115200);
  Wire.begin(); // Inicializa el bus I2C (Pines SDA y SCL por defecto)
  
  if (luxSensor.begin()) {
    Serial.println("Sensor BH1750 iniciado correctamente.");
  } else {
    Serial.println("Error: No se detecta el BH1750.");
  }
}

void loop() {
  uint16_t lux = luxSensor.readLightLevel();
  Serial.print("Luz ambiente: ");
  Serial.print(lux);
  Serial.println(" lux");
  delay(2000);
}
```

*Este paso previo de validación local (hardware y cableado correctos) te ahorrará horas de depuración más adelante.*

## 2. Inclusión de Librerías y Lógica MAC
- **MCCI LoRaWAN LMIC library**: Es la implementación estándar de la pila LoRaWAN para microcontroladores. Aparte de los envíos de radio, maneja la lógica de la capa MAC, los tiempos de apertura de ventanas de recepción (RX1/RX2) y el cumplimiento estricto del Duty Cycle (tiempo en el aire permitido).
- **Wire.h**: Librería nativa para controlar el bus I2C de los sensores.

## 3. Empaquetado y Optimización del Payload

En LoRaWAN, cada byte extra enviado reduce drásticamente la batería y aumenta las probabilidades de colisión. **Nunca se deben enviar cadenas JSON o texto en claro**. Todo debe empaquetarse en binario.

Ejemplo de optimización mediante desplazamiento de bits (*bit shifting*):
Si la temperatura puede variar entre -10 y 50 ºC, en lugar de enviar un `float` (4 bytes), podemos enviar un `int16_t` (2 bytes) multiplicando el valor por 10 o 100.

```cpp
// Ejemplo: Temperatura 24.5 ºC -> 245
int16_t temp = (int16_t)(temperatura_leida * 10);
uint8_t payload[4];
payload[0] = temp >> 8;   // Byte más significativo
payload[1] = temp & 0xFF; // Byte menos significativo

// Igual para la luz o la humedad
uint16_t luz = leer_luxes();
payload[2] = luz >> 8;
payload[3] = luz & 0xFF;
```

## 4. Lógica Orientada a Eventos y LMIC

La librería LMIC funciona mediante callbacks (eventos). El flujo principal de nuestro programa será:
1. `setup()`: Inicializa el chip LoRa, los sensores I2C/ADC y programa las claves OTAA (`DevEUI`, `AppEUI`, `AppKey`).
2. Se encola un *Join Request*.
3. Evento `EV_JOINED`: El nodo se ha unido con éxito. Se habilitan los envíos periódicos.
4. Evento `EV_TXCOMPLETE`: El paquete se ha transmitido y se han cerrado las ventanas de recepción. **Este es el momento exacto para ir a dormir.**

## 5. Gestión Extrema de Energía (Deep Sleep)

En lugar de usar la función `delay()` (que mantiene la CPU consumiendo entre 40 y 80 mA), utilizaremos el **Deep Sleep** del ESP32.
En Deep Sleep, la memoria RAM y la CPU se apagan, reduciendo el consumo a < 10 µA. Solo el coprocesador RTC (Real Time Clock) se queda encendido para despertar al chip tras el tiempo estipulado (ej. 30 minutos).

Al despertar de un Deep Sleep, el ESP32 ejecuta la función `setup()` de nuevo. Para que LMIC no tenga que volver a hacer el proceso de *Join* (lo que gasta mucha batería), guardaremos las claves de sesión dinámicas en la memoria RTC RAM del ESP32 para recuperarlas al despertar.
