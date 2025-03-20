import paho.mqtt.client as mqtt

broker = "localhost"
port = 9999
topic = "sensor/tem"
username = 'mqtt-subscriber'
password = 'mqtt-subscriber'

def on_message(client, userdata, message):
    data = message.payload.decode("utf-8")
    print(f"Received: {data}")

client = mqtt.Client(client_id='cloud processing service')
# authentication purposes
client.username_pw_set(username=username, password=password)
client.connect(host=broker, port=port, keepalive=50)
client.subscribe(topic)

client.on_message = on_message
client.loop_forever()