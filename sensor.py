import paho.mqtt.client as mqtt
import json
import random
import time

broker = "localhost"
port = 9999
topic = "factory/sensors/temperature"

client = mqtt.Client(client_id='sensor-9999')
client.connect(host=broker, port=port, keepalive=50)

while True:
    temperature = round(random.uniform(20, 50), 2)
    payload = {
        "sensor_id": "temp_sensor_9999",
        "temperature": temperature,
        "unit": "C",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    client.publish(topic, json.dumps(payload))
    print(f"Published: {payload}")
    time.sleep(10)  # Publish every 5 seconds
