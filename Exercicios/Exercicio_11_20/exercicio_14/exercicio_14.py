# app.py
from flask import Flask, render_template, request
app= Flask(__name__)

users = {
'user1': '1234',
'user2': '1234'
}

sensors_dict = {

}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        print(user, password)
        if user in users and users[user] == password:
            return render_template('home.html')
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('login.html')

@app.route('/register_user')
def register_user():
    return render_template("register_user.html")

@app.route('/add_user', methods=['GET','POST'])
def add_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
    
    users[user] = password
    return render_template("users.html", devices=users)
    
@app.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@app.route('/add_sensor', methods=['GET','POST'])
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
    
@app.route('/list_users')
def list_users():
    global users
    return render_template("users.html", devices=users)
    
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/actuators')
def actuators():
    atuadores = {'Servo Motor': 122, 'Lâmpada': 1}
    return render_template("actuators.html", atuadores=atuadores)

@app.route('/sensors')
def sensors():
    return render_template("sensors.html", sensores=sensors_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)