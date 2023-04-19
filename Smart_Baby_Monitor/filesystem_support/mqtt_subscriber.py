import paho.mqtt.client as mqtt


MQTT_SERVER = "Localhost"
MQTT_PORT = 8883

MQTT_TOPIC = "explorer/mics"

TLS_CERT = "mqtt_broker_certs/client.crt"
TLS_KEY = "mqtt_broker_certs/client.key"
TLS_CA_CERTS ="mqtt_broker_certs/ca.crt"

OUTPUT_FILE = "output.wav"

with open(OUTPUT_FILE, "wb") as f: #wb is used instead of w

    def on_message(client, userdata, message):
        f.write(message.payload.decode() + "\n")
        f.flush() #ensure all data makes it in the file?

    client = mqtt.Client()
    client.tls_set(TLS_CA_CERTS, certfile=TLS_CERT, keyfile=TLS_KEY)

    client.on_message = on_message
    client.connect(MQTT_SERVER, MQTT_PORT)

    client.subscribe(MQTT_TOPIC, qos=1)
    client.loop_forever()