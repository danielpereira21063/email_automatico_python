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
        

# url = "https://contrata-se-devs.lucascaton.com.br/"
# url = "https://remoteintech.company"
# url = "https://www.trackawesomelist.com/lukasz-madon/awesome-remote-job/"
# url = "https://github.com/remoteintech/remote-jobs"
# url = "https://github.com/guru-br/catalogo_empresas"
# url = "https://github.com/AfonsoFeliciano/Empresas-Brasileiras-Trabalho-Remoto"
# url = "https://github.com/leogregianin/mato-grosso-tech-companies"
# url = "https://github.com/pythonbrasil/pyBusinesses-BR"
# url = "https://github.com/clj-br/vagas"
# url = "https://github.com/guia-de-sistemas-embarcados/lista-de-empresas/"
# url = "https://www.jivochat.com.br/blog/marketing/agencias-de-marketing-digital.html"


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


def executar_crawler(alvo, nivel=2):
    try:    
        emails = encontrar_emails(alvo)
        print("{} encontrado{}".format(len(emails), "s" if len(emails) != 1 else ""))
        for email in emails:
            salvar_email_arquivo(email)
        
        if nivel == 3:
            alvos = encontrar_novas_urls(alvo)
            for i, alvo in enumerate(alvos):
                print("Buscando emails do alvo {} - Nível {} ({} de {})".format(alvo, nivel, i, len(alvos)))
                executar_crawler(alvo)


        print("\n")
        # time.sleep(1)
    except Exception as ex:
        print(ex)


alvos = encontrar_novas_urls(url)

for i, alvo in enumerate(alvos):
    print("Buscando emails do alvo {} - {} de {}".format(alvo, i, len(alvos)))
    executar_crawler(alvo, 3)