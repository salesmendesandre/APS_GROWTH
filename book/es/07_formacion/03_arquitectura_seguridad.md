# Teoría III: Arquitectura y Seguridad

Para entender el ecosistema completo del taller, es imperativo conocer la arquitectura global y los mecanismos criptográficos de LoRaWAN.

## Arquitectura *Star-of-Stars*

A diferencia de las redes en malla (*mesh*) como Zigbee, LoRaWAN utiliza una arquitectura **en estrella de estrellas** (*star-of-stars*).

1. **End Devices (Nodos)**: Como el nodo IoT ambiental que construiremos, equipado con sensores y un módulo de radio LoRa. Se comunican por radiofrecuencia (LoRa).
2. **Gateways**: Receptores multicanal y multispreading factor. Actúan como puentes transparentes (*Packet Forwarders*). Escuchan todo el espectro LoRa y reenvían cualquier trama válida a la red (vía Ethernet, WiFi o 4G). Un nodo no está asociado a un Gateway específico; su mensaje puede ser recibido por múltiples Gateways simultáneamente.
3. **Network Server (NS)**: El cerebro de la red (ej. The Things Network o ChirpStack). Filtra paquetes duplicados, verifica la autenticidad, gestiona el ADR (Adaptive Data Rate) y enruta los datos.
4. **Application Server (AS)**: El servidor del cliente que descifra el paquete de datos (*payload*) y lo almacena o procesa.

## Seguridad y Criptografía

La seguridad es un pilar nativo de LoRaWAN. Todo mensaje transmitido está protegido por partida doble mediante criptografía simétrica **AES-128**.

1. **Network Session Key (NwkSKey)**: Utilizada por el nodo y el *Network Server* para firmar matemáticamente el mensaje mediante un código de integridad **MIC** (Message Integrity Code). Evita la alteración o suplantación.
2. **Application Session Key (AppSKey)**: Utilizada para **cifrar** el *payload* de extremo a extremo (End-to-End). El Gateway y el Network Server no pueden leer el contenido de los sensores; solo el Application Server posee la clave para descifrarlo.

## Procedimientos de Activación (Unión a la red)

Para que el nodo ambiental obtenga estas claves de sesión y se asocie a la red, existen dos métodos:

### ABP (Activation by Personalization)
Las claves de sesión (`NwkSKey`, `AppSKey`) y la dirección de dispositivo (`DevAddr`) se programan estáticamente en el firmware (código C++) del nodo en la fábrica.
- *Ventaja*: El nodo no necesita negociar su conexión, puede transmitir inmediatamente.
- *Desventaja*: Es menos seguro. Si se pierde la sincronización de contadores de tramas (Frame Counters), la red descartará los paquetes para evitar ataques de repetición (*Replay attacks*).

### OTAA (Over-The-Air Activation)
El método recomendado y el que implementaremos en el taller. El nodo inicia una negociación dinámica (*Join Request*) enviando sus credenciales globales estáticas (`DevEUI`, `AppEUI` y `AppKey`).
El servidor verifica la identidad, genera aleatoriamente un identificador temporal (`DevAddr`) y negocia las claves de sesión (`NwkSKey` y `AppSKey`) enviándoselas cifradas en un *Join Accept*.

*En el taller de montaje configuraremos las credenciales OTAA en PlatformIO para unir nuestro nodo de manera segura al Network Server.*
