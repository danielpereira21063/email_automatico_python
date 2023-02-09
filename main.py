import pickle

from database import *
from email_sender import *
from crawler import *
import time

sender = EmailSender("", "")

def enviar_email(email):    
    if not email_existe(email):
        email_enviado = sender.enviar_email(email, "TESTE", "<h1>Email teste</h1>")
        if email_enviado:
            salvar_email(email)
    else:
        print("Email já enviado anteriormente para {}".format(email))
        
    

url = "https://rcasistemas.com.br/site_2019/"

emails = buscar_emails(url)

for email in emails:
    # enviar_email(email)
    print(email)
    time.sleep(.2)