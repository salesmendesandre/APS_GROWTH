# Data Extraction and Analysis

Once the node transmits to the Network Server and the data arrives correctly at our console, we will encounter an incomprehensible *uplink* packet (e.g., `00F50A52`). This is due to our binary *payload* optimization.

## 1. Payload Formatters (Uplink Decoders)

The first step is to decode the binary packet back to its original physical magnitudes. This is done on the Network Server by writing a JavaScript function (`Decoder` or `Uplink Formatter`).

```javascript
function decodeUplink(input) {
  var data = {};
  var bytes = input.bytes;
  
  // Reconstruct temperature (2 bytes) and divide by 10
  var tempInt = (bytes[0] << 8) | bytes[1];
  data.temperature = tempInt / 10.0;
  
  // Reconstruct light (2 bytes)
  data.light = (bytes[2] << 8) | bytes[3];

  return {
    data: data,
    warnings: [],
    errors: []
  };
}
```

## 2. Integration (Webhooks / MQTT)

With the decrypted data on the server, we don't want it to stay there. We will use the **Integrations** module:
- **MQTT**: The quintessential lightweight messaging protocol of IoT. We can subscribe our own server (e.g., a Python script) to a *topic* provided by the Network Server to receive data in real time every time the node transmits.
- **Webhooks**: The Network Server will make an HTTP POST request to our backend with the complete JSON every time there is an *Uplink*.

## 3. Visualization in Dashboards

For the project to have an impact on garden users and students, visualization is critical.
- **Database**: It is recommended to store the decoded data in a time-series database, such as **InfluxDB**.
- **Dashboard**: Tools like **Grafana** allow connecting to InfluxDB to create interactive charts, alerts (e.g., "Warn if humidity drops below 20%"), and real-time gauges.

```{figure} ../../_static/generated/diagrams/es/lorawan_data.svg
---
width: 100%
align: center
---
Data extraction and integration architecture.
```

In this way, the data cycle is completed: from the magnetic field of the LoRa *chirp* emitted in the garden, to a control panel accessible from any web browser.
