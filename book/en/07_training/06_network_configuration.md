# Network Infrastructure Configuration

Before our node can transmit useful data, we need to establish the infrastructure that will listen to and process that data. In this workshop we will use a **Network Server** (such as The Things Network - TTN or a private instance of ChirpStack) to manage our fleet of devices.

## 1. Setting up the Heltec Gateway

The Gateway is the bridge between the electromagnetic spectrum (LoRa) and the IP network (Internet).
- **Internet Connection**: We will configure the Gateway to connect to the Faculty's WiFi network or via Ethernet.
- **Packet Forwarder**: The Gateway's internal software (usually based on the *Semtech UDP Packet Forwarder* or *Basic Station*) must be configured to point to the IP address or domain of our Network Server. The port must be specified (e.g., 1700 for UDP) as well as the Gateway's EUI to identify it on the server.
- **Frequencies**: Ensure that the Gateway is configured to listen on the correct frequency plan (EU868 for Europe).

## 2. Using The Things Network (TTN)

For this workshop, we will use **The Things Network (TTN)**, the largest public and collaborative LoRaWAN network globally, maintained by The Things Industries (TTI). Below are the steps to configure our infrastructure in their Console.

### 2.1. Registering the Gateway

1. Log in to the [TTN Console (Europe 1)](https://eu1.cloud.thethings.network/console/).
2. Go to **Gateways** and click on **Register gateway**.
3. Enter the **Gateway EUI** (a unique 8-byte code usually found on the Heltec sticker or read via the serial port).
4. Assign an identifying name and ensure you select the **Europe 863-870 MHz (SF9 for RX2)** frequency plan.
5. Click **Register gateway**.

```{figure} ../../_static/ttn_add_gateway.png
---
width: 100%
align: center
name: fig-ttn-add-gateway-en
---
The Things Network interface for registering a new Gateway.
```

Once registered, you will see the Gateway's general panel (*Overview*) where you can check its connection status and recent activity:

```{figure} ../../_static/ttn_gateway_overview.png
---
width: 100%
align: center
name: fig-ttn-gateway-overview-en
---
General status and statistics panel of the Gateway in TTN.
```

### 2.2. Creating the Application

In TTN, nodes are not added individually; they must belong to an **Application** that groups their data.

1. Go to the top menu **Applications** and click **Create application**.
2. Fill in the **Application ID** (it must be unique, without spaces or capital letters, e.g., `aps-growth-garden-01`).
3. Click **Create application**.

```{figure} ../../_static/ttn_create_app.png
---
width: 100%
align: center
name: fig-ttn-create-app-en
---
Creation of a logical application in TTN to group the garden nodes.
```

Once created, you will access the application's general panel, from where you can manage all the devices linked to it:

```{figure} ../../_static/ttn_app_overview.png
---
width: 100%
align: center
name: fig-ttn-app-overview-en
---
General panel of the newly created application in The Things Network.
```

### 2.3. Registering the Node (End Device)

Inside the newly created application, we proceed to register the ESP32 microcontroller:

1. Click on **Register end device**.
2. Under *Input Method*, select **Enter end device specifics manually** (since our node is "homemade" and not in the commercial manufacturer database).
3. Select:
   - **Frequency plan**: Europe 863-870 MHz (SF9 for RX2).
   - **LoRaWAN version**: LoRaWAN Specification 1.0.3 (the one supported by the LMIC library).
4. The provisioning method will be **Over the air activation (OTAA)**.
5. Click **Generate** in the **JoinEUI** and **DevEUI** sections if you don't have pre-assigned ones.
6. Click **Generate** to create the secret **AppKey**.
7. Click **Register end device**.

```{figure} ../../_static/ttn_add_node.png
---
width: 100%
align: center
name: fig-ttn-add-node-en
---
OTAA keys generation (DevEUI, AppEUI, AppKey) when registering the node.
```

Once the registration is complete, you will access the device's control panel (*Device overview*), where you can verify its status, sent messages (*Payload*), and other diagnostic information:

```{figure} ../../_static/ttn_node_overview.png
---
width: 100%
align: center
name: fig-ttn-node-overview-en
---
General status and activity panel of the newly registered node in TTN.
```

With the device registered in the console and the keys ready, the next step will be to inject these OTAA keys into the ESP32 firmware during the programming phase.
