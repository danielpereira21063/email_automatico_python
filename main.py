import pickle
from database import *
from email_sender import *
from crawler import *
import time
import threading

sender = EmailSender("", "")

def enviar_email(email, assunto, conteudo, arquivo=None):
    if not email_existe(email):
        email_enviado = sender.enviar_email(email, assunto, conteudo, arquivo)
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
    lines = []
    str_arquivo = ""
    with open("emails.txt", "r") as f:
        for line in f:
            lines.append(line.strip())

    return lines

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


def carregar_arquivo(path):
    with open(path, "rb") as file:
        return file.read()


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



emails = ler_emails_arquivo()

assunto = "Candidato para oportunidade de Desenvolvedor Full-Stack"
conteudo = """<p>Olá,

Meu nome é Daniel e sou um Desenvolvedor FullStack altamente capacitado, com forte conhecimento em .NET e na construção de páginas web com HTML, CSS e JavaScript.

Deve estar se perguntando como consegui seu endereço de e-mail. Construí uma aplicação em Python que extrai e-mails de sites de vagas de emprego e provavelmente aplicação encontrou o seu em alguma página Web. Queria mostrar que tenho um alto conhecimento técnico e que posso ser um grande valor para uma empresa.</p>

<p>Vim de uma família humilde e aprendi a programar sozinho. Desde cedo sempre tive curiosidade sobre como os sistemas funcionavam e adoro estudar e aprender coisas novas. No meu trabalho atual, trabalho com desenvolvimento e manutenção de aplicações web usando .NET e Vue.js, mas tenho experiência também com outras tecnologias como Angular e React em meus estudos.

Além disso, sou habilidoso em Cloud Computing e tenho duas máquinas na Oracle onde hospedo meus projetos, incluindo meu portfólio que pode ser acessado em https://danielsanchesdev.com.br. Com minha habilidade e experiência, estou confiante de que posso resolver problemas complexos de forma eficiente e contribuir para o sucesso da empresa.</p>

<p>Se você é um recrutador, por favor não deixe de me contatar para que possamos conversar e eu possa mostrar mais sobre minhas habilidades e como posso ser um valor para sua equipe. Caso não seja, peço perdão pelo incômodo e por favor ignore esse e-mail.</p>

<p>Anexei meu currículo para referência.</p>

<p>Agradeço pela sua atenção e espero ouvir de você em breve.</p>

<p>Att,</p>
<p>Daniel Sanches</p>"""



def run():
    for (i, email) in enumerate(emails):
        print("Enviando email para {} - {} enviado(s) em um total de {}".format(email, i+1, len(emails)))
        enviar_email(email, assunto, conteudo, "cv_daniel-pereira-sanches.pdf")


run()
# THREADS = []

# for i in range(100):
#     t = threading.Thread(target=run)
#     THREADS.append(t)
#     t.start()

# for t in threads:
#     t.join()
# alvos = encontrar_novas_urls(url)

# for i, alvo in enumerate(alvos):
#     print("Buscando emails do alvo {} - {} de {}".format(alvo, i, len(alvos)))
#     executar_crawler(alvo, 3)

