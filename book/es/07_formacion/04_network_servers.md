# Teoría IV: Network Servers y la Comunidad TTN

En el ecosistema LoRaWAN, el **Network Server (Servidor de Red)** es el cerebro de la red. Es el software encargado de recibir, gestionar y procesar todos los mensajes de radiofrecuencia (RF) que capturan los Gateways para posteriormente entregárselos, ya limpios y ordenados, a las aplicaciones finales.

## ¿Qué hace exactamente un Network Server?

Mientras que un Gateway simplemente escucha el espectro electromagnético y reenvía todo lo que capta hacia Internet, el Network Server realiza el trabajo pesado:

1. **De-duplicación de paquetes**: Si tienes varios Gateways cerca, es muy probable que todos escuchen el mismo mensaje de tu nodo ambiental. Todos lo enviarán a Internet. El Network Server detecta que es el mismo mensaje (misma marca de tiempo, mismo contador) y descarta los duplicados, quedándose con el que tiene mejor calidad de señal (SNR y RSSI).
2. **Enrutamiento (Routing)**: Determina a qué aplicación (Application Server) pertenece un dato en función de la dirección del dispositivo (`DevAddr`).
3. **Control MAC (MAC Commands)**: Gestiona comandos de red de bajo nivel (ocultos al usuario) para optimizar el canal.
4. **Adaptive Data Rate (ADR)**: Evalúa constantemente la calidad del enlace de radio de cada nodo. Si un nodo tiene una señal excelente, el Network Server le ordena (mediante comandos MAC) que transmita más rápido (mayor Data Rate) y con menos potencia. Esto ahorra batería y libera tiempo en el espectro.
5. **Autenticación y Seguridad**: Es responsable de ejecutar el procedimiento *Join* en OTAA, verificar la identidad del nodo con su `AppKey` y generar las claves de sesión temporales (`NwkSKey` y `AppSKey`).

## Integraciones y Extracción de Datos

Una vez que el Network Server ha descifrado y validado el mensaje, ¿qué hace con él? Lo pasa al **Application Server**, que suele ser un módulo integrado en la misma plataforma.

El Application Server se encarga de exponer estos datos para que otras plataformas puedan consumirlos. Esto se realiza mediante **Integraciones**:

- **MQTT (Message Queuing Telemetry Transport)**: El estándar de facto en el IoT. Permite suscribirse a un "topic" para recibir los datos de los sensores en tiempo real.
- **Webhooks (HTTP POST)**: El servidor envía automáticamente una petición HTTP a una URL externa cada vez que llega un paquete. Muy útil para inyectar datos directamente en bases de datos o paneles de control (como Grafana, Node-RED o aplicaciones personalizadas).
- **Integraciones Nativas**: Plataformas como AWS IoT Core, Azure IoT o Datacake ofrecen conectores nativos preconfigurados para recibir los flujos de datos sin programar una sola línea de código.

## El Ecosistema: The Things Network (TTN)

Para nuestro proyecto, utilizaremos **The Things Network (TTN)**. Pero, ¿qué es exactamente y por qué es tan relevante?

### Origen y Filosofía

The Things Network nació en Ámsterdam en 2015 con una premisa revolucionaria: **construir una red de datos para el Internet de las Cosas que sea abierta, descentralizada y propiedad de la comunidad (crowdsourced).** 

En lugar de depender de grandes operadoras de telecomunicaciones tradicionales (como Movistar, Vodafone o Orange) que cobran suscripciones mensuales por cada SIM, los fundadores propusieron que si suficientes personas y empresas compraban y conectaban un Gateway LoRaWAN en sus tejados, se podría cubrir una ciudad entera en cuestión de semanas. Y lo lograron: cubrieron Ámsterdam en menos de 6 semanas usando solo 10 Gateways comprados por voluntarios.

- **Objetivo de la Comunidad TTN**: Proporcionar conectividad gratuita y global para proyectos IoT, fomentando la innovación, el aprendizaje y las aplicaciones de impacto social o medioambiental (como nuestro huerto ecológico).
- **El Pacto**: Si tú aportas cobertura a la red instalando un Gateway, puedes usar la cobertura de los Gateways instalados por otras personas en cualquier parte del mundo.

### The Things Stack (V3)

Toda la infraestructura de software que hace funcionar a TTN se conoce como **The Things Stack** (actualmente en su versión 3 o "V3"). Existen distintas versiones del mismo software:

1. **The Things Network (Community Edition)**: Es gratuita, operada por *The Things Industries* y mantenida por la comunidad global. Es la que usaremos. Su política de uso razonable limita el tiempo de transmisión para evitar saturaciones, por lo que es perfecta para monitorización ambiental.
2. **The Things Enterprise Stack**: Versión de pago con acuerdos de nivel de servicio (SLA), ideal para empresas con despliegues comerciales masivos que requieren soporte oficial y servidores privados.

## Alternativas a TTN

Aunque TTN es la red colaborativa más grande, existen otras opciones para desplegar redes LoRaWAN:

- **ChirpStack**: Es un Network Server *Open Source*. En lugar de conectarte a un servidor global (como en TTN), puedes instalar ChirpStack en una Raspberry Pi local o en un servidor propio. Es ideal para redes privadas (por ejemplo, cubrir una finca aislada donde no hay Internet y todo se gestiona en red local).
- **AWS IoT Core for LoRaWAN**: Amazon Web Services ofrece un Network Server gestionado que se integra directamente con todo el ecosistema de computación en la nube de AWS.
- **Helium**: Una red comercial descentralizada donde los dueños de los Gateways reciben criptomonedas (HNT) como recompensa por proporcionar cobertura, y los usuarios pagan micro-transacciones por enviar datos.
- **Redes Comerciales**: Operadoras tradicionales (Orange, Actility, LORIOT) ofrecen LoRaWAN como un servicio de pago clásico para clientes corporativos.

En este curso apostamos por **The Things Network** por su carácter abierto, su fuerte comunidad (con miles de tutoriales) y su alineación perfecta con los valores educativos del proyecto APS-GROWTH.
