from flask import Flask

app= Flask(__name__)

@app.route('/sensor_umidade')
def sensor_umidade():
    return """
    <html>
        <body>
            <h1>Sensor de Umidade</h1>
            <p>Voltar para <a href="/banheiro">Voltar para Banheiro</a>! </p>
        </body>
    </html>
"""
@app.route('/lamp_int')
def lamp_imp():
    return """
    <html>
        <body>
            <h1>Lâmpada Inteligente</h1>
            <p>Voltar para <a href="/banheiro">Voltar para Banheiro</a>! </p>
        </body>
    </html>
"""
@app.route('/sensor_luz')
def sensor_luz():
    return """
    <html>
        <body>
            <h1>Sensor de Luminosidade</h1>
            <p>Voltar para <a href="/quarto">Voltar para Quarto</a>! </p>
        </body>
    </html>
"""
@app.route('/interruptor')
def interruptor():
    return """
    <html>
        <body>
            <h1>Interruptor</h1>
            <p>Voltar para <a href="/quarto">Voltar para Quarto</a>! </p>
        </body>
    </html>
"""


@app.route('/banheiro')
def banheiro():
    return """
        <html>
            <body>
                <h1>Banheiro</h1>
                <ul>
                    <li><a href="/sensor_umidade">Sensor de Umidade</a></li>
                    <li><a href="/lamp_int">Lâmpada Inteligente</a></li>
                </ul>
                <p>Voltar para <a href="/">página inicial</a>! </p>
            </body>
        </html>
"""

@app.route('/quarto')
def quarto():
    return """
        <html>
            <body>
                <h1>Quarto</h1>
                <ul>
                    <li><a href="/sensor_luz">Sensor de Luminosidade</a></li>
                    <li><a href="/interruptor">Interruptor</a></li>
                </ul>
                <p>Voltar para <a href="/">página inicial</a>! </p>
            </body>
        </html>
"""

@app.route('/')
def index():
    return """
        <html>
            <head>
                <title>Menu Principal</title>
            </head>
            <body>
                <h2>Minha Casa</h2>
                <h3>Acesse o menu:</h3>
                <ul>
                    <li><a href="/quarto">Ir para Quarto</a></li>
                    <li><a href="/banheiro">Ir para Banheiro</a></li>
                </ul>
            </body>
        </html> 
"""


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)
