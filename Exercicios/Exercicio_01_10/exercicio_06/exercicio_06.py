from flask import Flask, render_template

app= Flask(__name__)

@app.route('/sensor_umidade')
def sensor_umidade():
    sensor_umidade = ['Sensor Umidade']
    return render_template("sensor_umidade.html", sensor_umidade=sensor_umidade)

@app.route('/lamp_int')
def lamp_imp():
    lampada = ['Lâmpada']
    return render_template("lamp_int.html", lampada=lampada)

@app.route('/sensor_luz')
def sensor_luz():
    sensor_luz = ['Sensor de Luminosidade']
    return render_template("sensor_luz.html", sensor_luz=sensor_luz)

@app.route('/interruptor')
def interruptor():
    interruptor = ['Interruptor']
    return render_template("interruptor.html", interruptor=interruptor)

@app.route('/banheiro')
def banheiro():
    return render_template("banheiro.html")

@app.route('/quarto')
def quarto():
    return render_template("quarto.html")

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)
