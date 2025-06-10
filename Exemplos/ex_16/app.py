# app.py
from flask import Flask, render_template, request, jsonify
from login import login
from sensors import sensors
from actuators import actuators
from flask_mqtt import Mqtt

import json

temperature = 10
huminity = 10
datas = {}

app = Flask(__name__)

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensors, url_prefix='/')
app.register_blueprint(actuators, url_prefix='/')

app.config['MQTT_BROKER_URL'] = 'broker.mqttdashboard.com'  # mesmo do MicroPython
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5000
app.config['MQTT_TLS_ENABLED'] = False

mqtt_client = Mqtt()
mqtt_client.init_app(app)

# Tópicos usados no MicroPython
topic_subscribe_temp = "/aula/temperature"
topic_subscribe_humi = "/aula/huminity"

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/logoff')
def logoff():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/tempo_real')
def tempo_real():
    global temperature, huminity
    values = {"temperature": temperature, "huminity": huminity}
    return render_template("tr.html", values=values)

@app.route('/publish')
def publish():
    return render_template('publish.html')

@app.route('/publish_message', methods=['GET', 'POST'])
def publish_message():
    request_data = request.get_json()
    publish_result = mqtt_client.publish(request_data['topic'], request_data['message'])
    return jsonify(publish_result)

@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Broker Connected successfully')
        mqtt_client.subscribe(topic_subscribe_temp)
        mqtt_client.subscribe(topic_subscribe_humi)
    else:
        print('Bad connection. Code:', rc)

@mqtt_client.on_disconnect()
def handle_disconnect(client, userdata, rc):
    print("Disconnected from broker")

@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    global temperature, huminity
    payload_str = message.payload.decode()
    print(f"Received message on topic {message.topic}: {payload_str}")
    try:
        data = json.loads(payload_str)
    except json.JSONDecodeError:
        print("Error decoding JSON from MQTT message")
        return

    if message.topic == topic_subscribe_temp:
        if 'valor' in data:
            temperature = data['valor']
            print(f"Temperature updated to: {temperature}")
    elif message.topic == topic_subscribe_humi:
        if 'valor' in data:
            huminity = data['valor']
            print(f"Humidity updated to: {huminity}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
