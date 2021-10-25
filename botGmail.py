import os
import smtplib
from email.message import EmailMessage


# Configurar email, senha
EMAIL_ADRESS = input(('Informe seu email: '))
EMAIL_PASSWORD = input('Informe sua senha: ')

# Criar um e-mail
msg = EmailMessage()
msg['Subject'] = str(input('Informe a descrição do email: '))
msg['From'] = EMAIL_ADRESS
msg['To'] = str(input('Informe o email do destinatario: '))
msg.set_content(input('Informe a menssagem a ser enviada: '))

# Enviar um e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
