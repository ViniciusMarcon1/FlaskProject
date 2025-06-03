# app.py
from flask import Flask, render_template, redirect, url_for, request
from login import login
from sensors import sensors
from actuators import actuators

app= Flask(__name__)

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensors, url_prefix='/')
app.register_blueprint(actuators, url_prefix='/')

@app.route('/')
def index():
    return render_template('login.html')
  
@app.route('/home')
def home():
    return render_template("home.html")

# @app.route('/actuators')
# def actuators():
#     return render_template("actuators.html", atuadores=atuadores)

# @app.route('/sensors')
# def sensors():
#     return render_template("sensors.html", sensores=sensores)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)