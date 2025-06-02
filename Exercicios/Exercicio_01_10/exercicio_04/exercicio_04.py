from flask import Flask, render_template

app= Flask(__name__)

@app.route('/sensor_umidade')
def sensor_umidade():
    return render_template("sensor_umidade.html")

@app.route('/lamp_int')
def lamp_imp():
    return render_template("lamp_int.html")

@app.route('/sensor_luz')
def sensor_luz():
    return render_template("sensor_luz.html")

@app.route('/interruptor')
def interruptor():
    return render_template("interruptor.html")

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
