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

```{figure} ../../_static/ttn_add_gateway.png
---
width: 100%
align: center
name: fig-ttn-add-gateway
---
Interfaz de The Things Network para registrar un nuevo Gateway.
```

Una vez registrado, verás el panel general (*Overview*) del Gateway donde podrás comprobar su estado de conexión y la actividad reciente:

```{figure} ../../_static/ttn_gateway_overview.png
---
width: 100%
align: center
name: fig-ttn-gateway-overview
---
Panel general de estado y estadísticas del Gateway en TTN.
```

### 2.2. Creación de la Aplicación

En TTN, los nodos no se añaden sueltos, sino que deben pertenecer a una **Aplicación** que agrupe sus datos.

1. Ve al menú superior **Applications** y haz clic en **Create application**.
2. Rellena el **Application ID** (debe ser único, sin espacios ni mayúsculas, ej. `aps-growth-huerto-01`).
3. Haz clic en **Create application**.

```{figure} ../../_static/ttn_create_app.png
---
width: 100%
align: center
name: fig-ttn-create-app
---
Creación de una aplicación lógica en TTN para agrupar los nodos del huerto.
```

Una vez creada, accederás al panel general de la aplicación, desde donde podrás gestionar todos los dispositivos vinculados a ella:

```{figure} ../../_static/ttn_app_overview.png
---
width: 100%
align: center
name: fig-ttn-app-overview
---
Panel general de la aplicación recién creada en The Things Network.
```

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

```{figure} ../../_static/ttn_add_node.png
---
width: 100%
align: center
name: fig-ttn-add-node
---
Generación de claves OTAA (DevEUI, AppEUI, AppKey) al registrar el nodo.
```

Una vez finalizado el registro, accederás al panel de control del dispositivo (*Device overview*), donde podrás verificar su estado, los mensajes enviados (*Payload*) y otra información de diagnóstico:

```{figure} ../../_static/ttn_node_overview.png
---
width: 100%
align: center
name: fig-ttn-node-overview
---
Panel general de estado y actividad del nodo recién registrado en TTN.
```

Con el dispositivo registrado en la consola y las claves listas, el siguiente paso será inyectar estas claves OTAA en el firmware del ESP32 durante la fase de programación.
