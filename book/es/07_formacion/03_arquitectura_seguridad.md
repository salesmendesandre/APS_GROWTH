# Teoría III: Arquitectura y Seguridad

Para entender el ecosistema completo del taller, es imperativo conocer la arquitectura global y los mecanismos criptográficos de LoRaWAN.

## Arquitectura *Star-of-Stars*

A diferencia de las redes en malla (*mesh*) como Zigbee, LoRaWAN utiliza una arquitectura **en estrella de estrellas** (*star-of-stars*).

1. **End Devices (Nodos)**: Como el nodo IoT ambiental que construiremos, equipado con sensores y un módulo de radio LoRa. Se comunican por radiofrecuencia (LoRa).
2. **Gateways**: Receptores multicanal y multispreading factor. Actúan como puentes transparentes (*Packet Forwarders*). Escuchan todo el espectro LoRa y reenvían cualquier trama válida a la red (vía Ethernet, WiFi o 4G). Un nodo no está asociado a un Gateway específico; su mensaje puede ser recibido por múltiples Gateways simultáneamente.
3. **Network Server (NS)**: El cerebro de la red (ej. The Things Network o ChirpStack). Filtra paquetes duplicados, verifica la autenticidad, gestiona el ADR (Adaptive Data Rate) y enruta los datos.
4. **Application Server (AS)**: El servidor del cliente que descifra el paquete de datos (*payload*) y lo almacena o procesa.

```{figure} ../../_static/generated/diagrams/es/lorawan_architecture.svg
---
width: 100%
align: center
---
Arquitectura en Estrella de Estrellas (Star-of-Stars) de LoRaWAN.
```

## Seguridad y Criptografía

La seguridad es un pilar nativo de LoRaWAN. Todo mensaje transmitido está protegido por partida doble mediante criptografía simétrica **AES-128**.

1. **Network Session Key (NwkSKey)**: Utilizada por el nodo y el *Network Server* para firmar matemáticamente el mensaje mediante un código de integridad **MIC** (Message Integrity Code). Evita la alteración o suplantación.
2. **Application Session Key (AppSKey)**: Utilizada para **cifrar** el *payload* de extremo a extremo (End-to-End). El Gateway y el Network Server no pueden leer el contenido de los sensores; solo el Application Server posee la clave para descifrarlo.

```{figure} ../../_static/generated/diagrams/es/lorawan_security.svg
---
width: 90%
align: center
---
Flujo de cifrado End-to-End y autenticación de integridad (MIC).
```

## Procedimientos de Activación (Unión a la red)

Para que el nodo ambiental obtenga estas claves de sesión y se asocie a la red, existen dos métodos:

### OTAA (Over-The-Air Activation)
El método recomendado y el que implementaremos en el taller. El nodo inicia una negociación dinámica (*Join Request*) enviando sus credenciales globales estáticas:

1. **Device EUI (`DevEUI`)**: Un identificador único global de 64 bits (similar a una dirección MAC).
2. **Application EUI / Join EUI (`AppEUI`)**: Identifica a qué aplicación de la red pertenece el dispositivo.
3. **Application Key (`AppKey`)**: Una clave criptográfica secreta. Nunca debe transmitirse por la red. Se usa para negociar las claves de sesión de forma segura durante el *Join Request*.

El servidor verifica la identidad, genera aleatoriamente un identificador temporal (`DevAddr`) y negocia las claves de sesión (`NwkSKey` y `AppSKey`) enviándoselas cifradas en un *Join Accept*.

```{figure} ../../_static/generated/diagrams/es/lorawan_otaa.svg
---
width: 100%
align: center
---
Secuencia de activación OTAA (Join Procedure).
```

### ABP (Activation by Personalization)
A diferencia de OTAA, donde las claves se negocian dinámicamente, en ABP **grabamos directamente en el código del microcontrolador** la dirección del dispositivo (`DevAddr`) y las claves de sesión definitivas (`NwkSKey` y `AppSKey`).

```{figure} ../../_static/generated/diagrams/es/lorawan_abp.svg
---
width: 100%
align: center
---
Secuencia de envío de datos mediante ABP (sin Join Procedure).
```

### Comparativa OTAA vs ABP

A modo de resumen, estas son las principales diferencias entre ambos métodos de activación:

| Característica | OTAA (Recomendado) | ABP |
|---|---|---|
| **Negociación de claves** | Dinámica (*Join Request/Accept*) | Estática (Grabadas en firmware) |
| **Seguridad** | Alta (claves de sesión rotativas) | Baja (claves fijas, riesgo de *replay attack*) |
| **Consumo inicial** | Mayor (requiere confirmación bidireccional al encender) | Menor (puede transmitir inmediatamente) |
| **Flexibilidad de red** | Alta (fácil migración a otro *Network Server*) | Baja (requiere reprogramar todos los nodos) |
| **Tolerancia a fallos** | El *Join* puede fallar si la cobertura es marginal | No hay *Join*, pero se descartan paquetes si se desincroniza |

*En el taller de montaje configuraremos las credenciales OTAA en PlatformIO para unir nuestro nodo de manera segura al Network Server.*
