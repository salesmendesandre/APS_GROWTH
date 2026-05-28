# Configuración de la Infraestructura de Red

Antes de que nuestro nodo pueda transmitir datos útiles, necesitamos establecer la infraestructura que escuchará y procesará esos datos. En este taller utilizaremos un **Network Server** (como The Things Network - TTN o una instancia privada de ChirpStack) para gestionar nuestra flota de dispositivos.

## 1. Puesta en marcha del Gateway Heltec

El Gateway es el puente entre el espectro electromagnético (LoRa) y la red IP (Internet).
- **Conexión a Internet**: Configuraremos el Gateway para que se conecte a la red WiFi de la Facultad o mediante Ethernet.
- **Packet Forwarder**: El software interno del Gateway (generalmente basado en el *Semtech UDP Packet Forwarder* o *Basic Station*) debe configurarse para apuntar a la dirección IP o dominio de nuestro Network Server. Se debe especificar el puerto (ej. 1700 para UDP) y el EUI del Gateway para identificarlo en el servidor.
- **Frecuencias**: Asegurarse de que el Gateway está configurado para escuchar en el plan de frecuencias correcto (EU868 para Europa).

## 2. Registro en el Network Server

Una vez el Gateway está enrutando paquetes, debemos configurar el lado del servidor:
1. **Registro del Gateway**: Damos de alta el Gateway en la consola del Network Server usando su EUI. Si todo es correcto, veremos el estado como "Conectado" (Connected).
2. **Creación de la Aplicación**: Creamos una "Aplicación" lógica. Esta aplicación agrupará a todos los nodos ambientales que despleguemos en el huerto.

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
