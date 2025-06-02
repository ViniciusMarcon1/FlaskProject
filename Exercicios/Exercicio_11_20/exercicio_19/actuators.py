from flask import Blueprint, request, render_template, redirect, url_for

actuators = Blueprint("actuators",  __name__, template_folder="templates")

actuator_dict = {}

@actuators.route('/register_actuator')
def register_actuator():
    return render_template("register_actuator.html")

@actuators.route('/add_actuator', methods=['GET','POST'])
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

@actuators.route('/remove_actuator')
def remove_actuator():
    return render_template("remove_actuator.html", atuadores=actuator_dict)

@actuators.route('/del_actuator', methods=['GET','POST'])
def del_actuator():
    global sensors_dict
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
        
    actuator_dict.pop(actuator)
    return render_template("actuators.html", atuadores=actuator_dict)
 