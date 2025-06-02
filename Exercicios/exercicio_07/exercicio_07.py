# app.py
from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    menu = ['sensors', 'actuators']
    return render_template("index.html", menu=menu)

@app.route('/sensors')
def sensors():
    sensores = {'Umidade': 1036, 'Temperatura': 28, 'Luminosidade': 100}
    return render_template("sensors.html", sensores=sensores)

@app.route('/actuators')
def actuators():
    atuadores = {'Servo Motor': 122, 'Lâmpada': 1}
    return render_template("actuators.html", atuadores=atuadores)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)