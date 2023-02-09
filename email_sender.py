import smtplib
from email.mime.text import MIMEText
from datetime import datetime

class EmailSender:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(usuario, senha)

    
    def enviar_email(self, destinatario, assunto, conteudo):
        mensagem = MIMEText(conteudo, "html")
        mensagem["Subject"] = assunto
        mensagem["From"] = self.usuario
        mensagem["To"] = destinatario
        try:
            self.server.sendmail(self.usuario, destinatario, mensagem.as_string())
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print("{} - Email enviado para: {}".format(now, destinatario))
            return True
        except Exception as ex:
            print("Erro ao enviar email: {}".format(ex))
            return False


    def __del__(self):
        self.server.quit()
    