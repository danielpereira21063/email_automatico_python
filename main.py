import pickle

from database import *
from email_sender import *
from crawler import *
import time
import threading


# sender = EmailSender("", "")

def enviar_email(email):
    if not email_existe(email):
        email_enviado = sender.enviar_email(email, "TESTE", "<h1>Email teste</h1>")
        if email_enviado:
            salvar_email(email)
    else:
        print("Email já enviado anteriormente para {}".format(email))
        

# url = "https://www.trackawesomelist.com/lukasz-madon/awesome-remote-job/"
# url = "https://remoteintech.company"
# url = "https://www.trackawesomelist.com/lukasz-madon/awesome-remote-job/"
# url = "https://github.com/remoteintech/remote-jobs"
url = "https://github.com/guru-br/catalogo_empresas"

alvos = encontrar_novas_urls(url)


def ler_emails_arquivo():
    str_arquivo = ""
    with open("emails.txt", "r") as f:
        str_arquivo = f.read()

    return str_arquivo

def email_existe_arquivo(email):
    emails = ler_emails_arquivo()
    return email in emails


def salvar_email_arquivo(email):
    with open("emails.txt", "a") as f:
        if not email_existe_arquivo(email):
            print("salvando {}".format(email))
            f.write("{}\n".format(email))
        else:
            print("{} já salvo anteriormente".format(email))



# lock = threading.Lock()

def inicio():
    # lock.acquire()
    i = 1
    try:
        for alvo in alvos:
            print("Buscando emails do alvo {} de {}".format(i, len(alvos)))
            emails = encontrar_emails(alvo)
            print("{} encontrado{}".format(len(emails), "s" if len(emails) != 1 else ""))
            for email in emails:
                salvar_email_arquivo(email)
            print("\n")
            i+=1
            # time.sleep(1)
    except Exception as ex:
        print(ex)


inicio()

# THREADS = []

# for i in range(100):
#     thread = threading.Thread(target=inicio)
#     THREADS.append(thread)

# for thread in THREADS:
#     thread.start()
            
# for thread in THREADS:
#     thread.join()