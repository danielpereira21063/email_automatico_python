import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders
import time

class EmailSender:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(usuario, senha)

    
    def enviar_email(self, destinatario, assunto, conteudo, arquivo=None):
        mensagem = MIMEMultipart("alternative")
        mensagem["Subject"] = assunto
        mensagem["From"] = self.usuario
        mensagem["To"] = destinatario

        part_html = MIMEText(conteudo, 'html')

        mensagem.attach(part_html)
        if arquivo:
            part_anexo = MIMEBase("application", "octet-stream")
            part_anexo.set_payload(open(arquivo, "rb").read())
            encoders.encode_base64(part_anexo)
            part_anexo.add_header('Content-Disposition', 'attachment', filename=arquivo)
            mensagem.attach(part_anexo)
        try:
            self.server.sendmail(self.usuario, destinatario, mensagem.as_string())
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print("{} - Email enviado para: {}".format(now, destinatario))
            return True
        except Exception as ex:
            print("Erro ao enviar email: {}".format(ex))
            if "please run connect" in ex:
                print("Erro 'run connect'. Aguardando 60 segundos...")
                time.sleep(60)
            return False