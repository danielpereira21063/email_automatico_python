import requests
import re
from bs4 import BeautifulSoup

headers = {
    "Accept": "*/*",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,zh-CN;q=0.5,zh;q=0.4",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

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
        req = requests.get(url, headers, timeout=5)
        html = req.text
        return html
    except Exception as ex:
        print(ex)
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
        if "http" in str(link):
            url = link["href"]
            
            if "google." not in url and "youtube." not in url and "twitch." not in url and "tiktok." not in url and "facebook." not in url and "github." not in url and "twitter." not in url:
                url = url.replace("/url?q=", "")
                URLS.append(url)
        
    return URLS
