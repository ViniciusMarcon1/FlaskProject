from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/upload_file', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        save_path = os.path.join(app.root_path, 'static', 'img', filename)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Garante que a pasta exista
        f.save(save_path)
        return f"Arquivo {filename} salvo com sucesso!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)