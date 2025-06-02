from flask import Flask, render_template

app= Flask(__name__)

@app.route('/sensor_umidade')
def sensor_umidade():
    sensor_umidade = {'Sensor Umidade': 'Sensor Umidade'}
    return render_template("sensor_umidade.html", sensor_umidade=sensor_umidade, link='/banheiro')

@app.route('/lamp_int')
def lamp_imp():
    lampada = {'Lâmpada': 'Lâmpada'}
    return render_template("lamp_int.html", lampada=lampada, link='/banheiro')

@app.route('/sensor_luz')
def sensor_luz():
    sensor_luz = {'Sensor de Luminosidade': 'Sensor de Luminosidade'}
    return render_template("sensor_luz.html", sensor_luz=sensor_luz, link='/quarto')

@app.route('/interruptor')
def interruptor():
    interruptor = {'Interruptor': 'Interruptor'}
    return render_template("interruptor.html", interruptor=interruptor, link='/quarto')

@app.route('/banheiro')
def banheiro():
    banheiro = {'Sensor de Umidade': '/sensor_umidade', 'Lâmpada Inteligente': '/lamp_int'}
    return render_template("banheiro.html", banheiro=banheiro, titulo='Banheiro')

@app.route('/quarto')
def quarto():
    quarto ={'Sensor de Luminosidade': '\sensor_luz', 'Interruptor': '/interruptor'}
    return render_template("quarto.html", quarto=quarto, titulo='Quarto')

@app.route('/')
def index():
    index = {'Banheiro': '/banheiro', 'Quarto': '/quarto'}
    return render_template("index.html", index=index)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)
