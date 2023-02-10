import requests
import re
from bs4 import BeautifulSoup

def encontrar_emails(url):
    html = obter_html_text(url)
    EMAILS = []
    emails = re.findall(r"[\w\-.]+@[\w\-]+\.\w+\.?\w*", html)

    for email in emails:
        if ".com" in email and "nome@provedor" not in email and "@example" not in email and "wixpress.com" not in email and "@github" not in email:
            EMAILS.append(email)
    return EMAILS


def obter_html_text(url):
    try:
        req = requests.get(url)
        html = req.text
        return html
    except Exception as ex:
        return ""
    

def obter_html_soup(url):
    html = obter_html_text(url)
    soup = BeautifulSoup(html, "html.parser")
    return soup

def encontrar_links(soup):
    return soup.find_all("a")

def encontrar_novas_urls(url):
    soup = obter_html_soup(url)
    links = encontrar_links(soup)

    URLS = []
    for link in links:
        url = link["href"]

        if ("http://" in url or "https://" in url):
            if ".google." not in url:
                url = url.replace("/url?q=", "")
                URLS.append(url)
    
    return URLS
        