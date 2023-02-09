import requests
import re

def buscar_emails(url):
    req = requests.get(url)
    html = req.text
    return re.findall(r"[\w\-.]+@[\w\-]+\.\w+\.?\w*", html)
