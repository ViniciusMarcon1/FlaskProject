# app.py
from flask import Flask, render_template, redirect, url_for, request
from login import login

app= Flask(__name__)

app.register_blueprint(login, url_prefix='/')

@app.route('/')
def index():
    return render_template('login.html')
  
@app.route('/home')
def home():
    return render_template("home.html")

# @app.route('/actuators')
# def actuators():
#     atuadores = {'Servo Motor': 122, 'Lâmpada': 1}
#     return render_template("actuators.html", atuadores=atuadores)

# @app.route('/sensors')
# def sensors():
#     sensores = {'T1':56, 'T2':25, 'T3':15}
#     return render_template("sensors.html", sensores=sensores)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)