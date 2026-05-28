# Configuración de la Infraestructura de Red

Antes de que nuestro nodo pueda transmitir datos útiles, necesitamos establecer la infraestructura que escuchará y procesará esos datos. En este taller utilizaremos un **Network Server** (como The Things Network - TTN o una instancia privada de ChirpStack) para gestionar nuestra flota de dispositivos.

## 1. Puesta en marcha del Gateway Heltec

El Gateway es el puente entre el espectro electromagnético (LoRa) y la red IP (Internet).
- **Conexión a Internet**: Configuraremos el Gateway para que se conecte a la red WiFi de la Facultad o mediante Ethernet.
- **Packet Forwarder**: El software interno del Gateway (generalmente basado en el *Semtech UDP Packet Forwarder* o *Basic Station*) debe configurarse para apuntar a la dirección IP o dominio de nuestro Network Server. Se debe especificar el puerto (ej. 1700 para UDP) y el EUI del Gateway para identificarlo en el servidor.
- **Frecuencias**: Asegurarse de que el Gateway está configurado para escuchar en el plan de frecuencias correcto (EU868 para Europa).

## 2. Uso de The Things Network (TTN)

Para este taller utilizaremos **The Things Network (TTN)**, la mayor red pública y colaborativa de LoRaWAN a nivel mundial, mantenida por The Things Industries (TTI). A continuación, se detallan los pasos para configurar nuestra infraestructura en su consola (Console).

### 2.1. Alta del Gateway

1. Accede a la [Consola de TTN (Europe 1)](https://eu1.cloud.thethings.network/console/) e inicia sesión.
2. Ve a **Gateways** y haz clic en **Register gateway**.
3. Introduce el **Gateway EUI** (un código único de 8 bytes que suele venir en la pegatina del Heltec o se lee por puerto serie).
4. Asigna un nombre identificativo y asegúrate de seleccionar el plan de frecuencias **Europe 863-870 MHz (SF9 for RX2)**.
5. Haz clic en **Register gateway**.

*(Pendiente: Insertar captura de pantalla de la interfaz "Register gateway" de TTN)*
![Captura: Añadir Gateway en TTN](_static/ttn_add_gateway.png)

### 2.2. Creación de la Aplicación

En TTN, los nodos no se añaden sueltos, sino que deben pertenecer a una **Aplicación** que agrupe sus datos.

1. Ve al menú superior **Applications** y haz clic en **Create application**.
2. Rellena el **Application ID** (debe ser único, sin espacios ni mayúsculas, ej. `aps-growth-huerto-01`).
3. Haz clic en **Create application**.

*(Pendiente: Insertar captura de pantalla de "Create application")*
![Captura: Crear Aplicación en TTN](_static/ttn_create_app.png)

### 2.3. Dar de Alta el Nodo (End Device)

Dentro de la aplicación recién creada, procedemos a registrar el microcontrolador ESP32:

1. Haz clic en **Register end device**.
2. En *Input Method*, selecciona **Enter end device specifics manually** (ya que nuestro nodo es "casero" y no está en la base de datos de fabricantes comerciales).
3. Selecciona:
   - **Frequency plan**: Europe 863-870 MHz (SF9 for RX2).
   - **LoRaWAN version**: LoRaWAN Specification 1.0.3 (la soportada por la librería LMIC).
4. El método de aprovisionamiento será **Over the air activation (OTAA)**.
5. Haz clic en **Generate** en los apartados de **JoinEUI** y **DevEUI** si no tienes unos preasignados.
6. Haz clic en **Generate** para crear la **AppKey** secreta.
7. Haz clic en **Register end device**.

*(Pendiente: Insertar captura de pantalla de "Register end device" y generación de claves)*
![Captura: Registrar Nodo en TTN](_static/ttn_add_node.png)

## 3. Registro de Dispositivos (OTAA)

Para añadir nuestro nodo ESP32 a la aplicación, debemos registrarlo utilizando el método **OTAA (Over-The-Air Activation)**. El Network Server generará o nos pedirá tres claves fundamentales que deberemos copiar en el código de nuestro nodo:

1. **Device EUI (`DevEUI`)**: Un identificador único global de 64 bits para nuestro ESP32 (similar a una dirección MAC). A veces lo genera el propio chip, a veces lo asignamos manualmente.
2. **Application EUI / Join EUI (`AppEUI`)**: Un identificador de 64 bits que identifica a qué aplicación pertenece el dispositivo.
3. **Application Key (`AppKey`)**: Una clave criptográfica AES-128 secreta. ¡Nunca debe transmitirse por la red! Se usa para negociar las claves de sesión de forma segura durante el *Join Request*.

```{figure} ../../_static/generated/diagrams/es/lorawan_otaa.svg
---
width: 100%
align: center
---
Secuencia de activación OTAA (Join Procedure).
```

Con el dispositivo registrado en la consola y las claves listas, el siguiente paso es inyectar estas claves en el firmware del ESP32.

## 4. Activación por Personalización (ABP)

Existe un segundo método de registro en la red llamado **ABP (Activation By Personalization)**. A diferencia de OTAA, donde las claves de sesión se negocian dinámicamente, en ABP **grabamos directamente en el código del microcontrolador** la dirección del dispositivo (`DevAddr`) y las claves de sesión definitivas (`NwkSKey` y `AppSKey`).

```{figure} ../../_static/generated/diagrams/es/lorawan_abp.svg
---
width: 100%
align: center
---
Secuencia de envío de datos mediante ABP (sin Join Procedure).
```

- **Ventajas**: El dispositivo no necesita hacer el *Join Procedure*, lo que ahorra batería al encenderse y evita que falle si la cobertura es marginal (ya que OTAA requiere una respuesta bidireccional del Gateway).
- **Desventajas**: Es mucho menos seguro, ya que las claves de cifrado nunca rotan. Además, si cambiamos de Network Server (ej. de TTN a ChirpStack), tendremos que reprogramar todos los nodos a mano, mientras que con OTAA solo se debe renegociar el Join. Por ello, **OTAA es el método estándar y recomendado para entornos reales**.
