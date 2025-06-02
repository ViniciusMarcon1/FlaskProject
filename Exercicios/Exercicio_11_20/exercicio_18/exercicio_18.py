# app.py
from flask import Flask, render_template, redirect, url_for, request
from login import login 
from sensors import sensors

app= Flask(__name__)

actuator_dict = {}
sensors_dict = {}

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensors, url_prefix='/')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register_actuator')
def register_actuator():
    return render_template("register_actuator.html")

@app.route('/add_actuator', methods=['GET','POST'])
def add_actuator():
    global actuator_dict
    if request.method == 'POST':
        actuator = request.form['actuator']
        value = int(request.form['value'])
    else:
        actuator = request.args.get('actuador', None)
        value = int(request.args.get('value', None))
    
    actuator_dict[actuator] = value
    return render_template("actuators.html", atuadores=actuator_dict)

@app.route('/remove_actuator')
def remove_actuator():
    return render_template("remove_actuator.html", atuadores=actuator_dict)

@app.route('/del_actuator', methods=['GET','POST'])
def del_actuator():
    global sensors_dict
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
        
    actuator_dict.pop(actuator)
    return render_template("actuators.html", atuadores=actuator_dict)
    
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