# Extracción y Análisis de Datos

Una vez el nodo transmite al Network Server y los datos llegan correctamente a nuestra consola, nos encontraremos con un paquete *uplink* incomprensible (ej. `00F50A52`). Esto se debe a nuestra optimización de *payload* binario.

## 1. Payload Formatters (Uplink Decoders)

El primer paso es decodificar el paquete binario de vuelta a sus magnitudes físicas originales. Esto se realiza en el Network Server escribiendo una función en JavaScript (`Decoder` o `Uplink Formatter`).

```javascript
function decodeUplink(input) {
  var data = {};
  var bytes = input.bytes;
  
  // Reconstruimos la temperatura (2 bytes) y la dividimos por 10
  var tempInt = (bytes[0] << 8) | bytes[1];
  data.temperatura = tempInt / 10.0;
  
  // Reconstruimos la luz (2 bytes)
  data.luz = (bytes[2] << 8) | bytes[3];

  return {
    data: data,
    warnings: [],
    errors: []
  };
}
```

## 2. Integración (Webhooks / MQTT)

Con los datos descifrados en el servidor, no queremos que se queden ahí. Utilizaremos el módulo de **Integrations**:
- **MQTT**: El protocolo de mensajería ligero por excelencia del IoT. Podemos suscribir nuestro propio servidor (ej. un script de Python) a un *topic* proporcionado por el Network Server para recibir los datos en tiempo real cada vez que el nodo transmita.
- **Webhooks**: El Network Server realizará una petición HTTP POST a nuestro backend con el JSON completo cada vez que haya un *Uplink*.

## 3. Visualización en Dashboards

Para que el proyecto tenga un impacto en los usuarios del huerto y los alumnos, la visualización es crítica.
- **Base de Datos**: Se recomienda almacenar los datos decodificados en una base de datos de series temporales, como **InfluxDB**.
- **Dashboard**: Herramientas como **Grafana** permiten conectarse a InfluxDB para crear gráficos interactivos, alertas (ej. "Avisar si la humedad baja del 20%") y medidores en tiempo real.

De esta manera, el ciclo del dato se completa: desde el campo magnético del *chirp* LoRa emitido en el huerto, hasta un panel de control accesible desde cualquier navegador web.
