# app.py
from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    index = {'Sensores': '/sensors', 'Atuadores': '/actuators'}
    return render_template("index.html", index=index)

@app.route('/sensors')
def sensors():
    sensores = {'T1':56, 'T2':25, 'T3':15}
    return render_template("sensors.html", sensores=sensores)

@app.route('/actuators')
def actuators():
    actuators = {'Servo Motor 1': 1, 'Servo Motor 2': 0, 'Lâmpada': 1}
    return render_template("actuators.html", actuators=actuators)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)