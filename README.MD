# MQTT IoT Sensor Communication Project

## Overview
This project demonstrates how **low-powered IoT devices** (such as sensors) can communicate with a **cloud processing service** using the **MQTT protocol**. The project simulates a **temperature sensor** that periodically publishes data to an MQTT broker, while a cloud-based service subscribes to the sensor topic and processes the data.

## Features
- Simulates an **IoT sensor** publishing temperature data.
- Uses **MQTT broker** for message handling.
- Implements a **subscriber** that processes and logs sensor data.
- Lightweight and efficient communication using the **publish-subscribe model**.

## Architecture
### Components:
1. **IoT Sensor (Publisher)**
   - Simulated using a Python script.
   - Sends temperature data to an MQTT broker.
   
2. **MQTT Broker**
   - Handles message distribution between publishers and subscribers.
   - Example: `localhost:9999` (an eclipse mosquitto broker).
   - Can be installed by running:
```sh
sudo apt-get install mosquitto
```

3. **Cloud Processing Service (Subscriber)**
   - Listens for incoming sensor data.
   - Processes and logs received messages.

## Getting Started
### Prerequisites
- **Python 3.x** installed
- Install MQTT client library:
  ```sh
  pip install paho-mqtt
  ```

### Running the Publisher (Simulated Sensor)
```sh
python sensor.py
```

### Running the Subscriber (Cloud Processing Service)
```sh
python subscribe.py
```

## How It Works
1. The **Publisher** simulates a sensor sending temperature readings.
2. The **MQTT Broker** receives and forwards the message to all subscribers.
3. The **Subscriber** listens to the topic and processes the data in real-time.

## Next Steps
- Learn more on IOT devices

## License
This project is open-source under the **MIT License**.
Used for learning purpose

