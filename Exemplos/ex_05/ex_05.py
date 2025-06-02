from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/sensors')
def sensors():
    return render_template("sensors.html")
