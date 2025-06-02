# app.py
from flask import Flask, render_template, redirect, url_for, request
from login import login 
from sensors import sensors
from actuators import actuators

app= Flask(__name__)

actuator_dict = {}
sensors_dict = {}

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensors, url_prefix='/')
app.register_blueprint(actuators, url_prefix='/')

@app.route('/')
def index():
    return render_template('login.html')
   
@app.route('/list_users')
def list_users():
    global users
    return render_template("users.html", devices=users)
    
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/actuators')
def actuators():
    return render_template("actuators.html", atuadores=actuator_dict)

@app.route('/sensors')
def sensors():
    return render_template("sensors.html", sensores=sensors_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)