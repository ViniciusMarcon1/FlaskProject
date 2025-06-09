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

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(401)
def page_not_found(error):
    return render_template('401.html'), 401

@app.errorhandler(403)
def page_not_found(error):
    return render_template('403.html'), 403

@app.errorhandler(408)
def page_not_found(error):
    return render_template('408.html'), 408

@app.errorhandler(429)
def page_not_found(error):
    return render_template('429.html'), 429

@app.errorhandler(500)
def page_not_found(error):
    return render_template('500.html'), 500

@app.errorhandler(503)
def page_not_found(error):
    return render_template('500.html'), 503

@app.errorhandler(405)
def page_not_found(error):
    return "Não autorizado", 405

@app.errorhandler(401)
def page_not_found(error):
    return "Usuário não autorizado", 401


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)