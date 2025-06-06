from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form['nome']
    return render_template('confirmacao.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)
