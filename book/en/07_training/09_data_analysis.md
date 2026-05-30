# Data Extraction and Analysis

```{admonition} Learning Objectives
:class: tip

At the end of this section, you should be able to:
- Write a payload decoder (Payload Formatter) in JavaScript.
- Configure integrations (MQTT/Webhooks) to extract data from the Network Server.
- Understand the utility of tools like InfluxDB and Grafana to visualize the final result.
```

Once the node transmits to the Network Server and the data arrives correctly in our console, we will encounter an incomprehensible *uplink* packet (e.g., `00F50A52`). This is due to our binary *payload* optimization.

## 1. Payload Formatters (Uplink Decoders)

The first step is to decode the binary packet back to its original physical magnitudes. This is done on the Network Server by writing a JavaScript function (`Decoder` or `Uplink Formatter`).

```javascript
function decodeUplink(input) {
  var data = {};
  var bytes = input.bytes;
  
  // We reconstruct the temperature (2 bytes) and divide by 10
  var tempInt = (bytes[0] << 8) | bytes[1];
  data.temperature = tempInt / 10.0;
  
  // We reconstruct the light (2 bytes)
  data.light = (bytes[2] << 8) | bytes[3];

  return {
    data: data,
    warnings: [],
    errors: []
  };
}
```

## 2. Integration (Webhooks / MQTT)

With the data deciphered on the server, we don't want it to just sit there. We will use the **Integrations** module:
- **MQTT**: The quintessential lightweight messaging protocol for IoT. We can subscribe our own server (e.g., a Python script) to a *topic* provided by the Network Server to receive real-time data every time the node transmits.
- **Webhooks**: The Network Server will make an HTTP POST request to our backend with the full JSON every time there is an *Uplink*.

## 3. Dashboard Visualization

For the project to have an impact on garden users and students, visualization is critical.
- **Database**: It is recommended to store decoded data in a time-series database, such as **InfluxDB**.
- **Dashboard**: Tools like **Grafana** allow connecting to InfluxDB to create interactive charts, alerts (e.g., "Alert if humidity drops below 20%"), and real-time gauges.

```{figure} ../../_static/generated/diagrams/en/lorawan_data.svg
---
width: 100%
align: center
---
Data extraction and integration architecture.
```

In this way, the data cycle is completed: from the magnetic field of the LoRa *chirp* emitted in the garden, to a control panel accessible from any web browser.

```{admonition} Self-Assessment
:class: dropdown

**1. What programming language is typically used to write the Payload Formatter in a LoRaWAN Network Server?**
JavaScript is normally used. A `decodeUplink` function is provided which receives an array of bytes and returns a structured object.

**2. If the Network Server is capable of graphing some basic data, why do we need to connect it to an external tool like Grafana?**
Network Servers are designed to route packets and manage connectivity, not for massive historical storage or creating complex control panels for end-users. A time-series database coupled with Grafana offers much more flexibility, long-term retention, and customizable views.
```
