from flask import Blueprint, request, render_template, redirect, url_for

sensors = Blueprint("sensors",  __name__, template_folder="templates")

sensors_dict = {}

@sensors.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@sensors.route('/add_sensor', methods=['GET','POST'])
def add_sensor():
    global sensors_dict
    if request.method == 'POST':
        sensor = request.form['sensor']
        value = int(request.form['value'])
    else:
        sensor = request.args.get('sensor', None)
        value = int(request.args.get('value', None))
    
    sensors_dict[sensor] = value
    return render_template("sensors.html", sensores=sensors_dict)

@sensors.route('/remove_sensor')
def remove_sensor():
    return render_template("remove_sensor.html", sensores=sensors_dict)

@sensors.route('/del_sensor', methods=['GET','POST'])
def del_sensor():
    global sensors_dict
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
        
    sensors_dict.pop(sensor)
    return render_template("sensors.html", sensores=sensors_dict)