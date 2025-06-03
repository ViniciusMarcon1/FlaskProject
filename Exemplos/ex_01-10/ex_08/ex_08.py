# app.py
from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sensors')
def sensors():
    sensores = {'T1':56, 'T2':25, 'T3':15}
    return render_template("sensors.html", sensores=sensores)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)