import pickle

from database import *
from email_sender import *
from crawler import *
import time


url = "https://www.google.com/search?q=vaga+desenvolvedor+c%23&rlz=1C1ISCS_pt-PT&sxsrf=AJOqlzUmfASLH4EIXiwXElsRVm0g30e4QQ%3A1675968262080&ei=Bj_lY7zQBKG05OUP3bGRkA4&oq=vaga+dese&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgQIIxAnMgUIABCABDIFCAAQgAQyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQyBQgAEIAEOgsILhCDARCxAxCABDoRCC4QgAQQsQMQgwEQxwEQ0QM6CAguELEDEIMBOgsILhCABBCxAxCDAToICAAQsQMQgwE6CAgAEIAEELEDOgcIIxCxAhAnOg0ILhCDARCxAxCABBAKOgoIABCABBCxAxAKOgcIABCABBAKOg0IABCABBCxAxCDARAKOgoIABCxAxCDARBDOgQIABBDSgQIQRgASgQIRhgAUABYyh5gsyRoA3ABeACAAYUBiAHRCZIBBDAuMTCYAQCgAQHAAQE&sclient=gws-wiz-serp"

while True:
    try:
        soup = obter_html_soup(url)
        urls_alvo = encontrar_novas_urls(url)

        for alvo in urls_alvo:
            emails = encontrar_emails(alvo)
            print("Procurando emails na url -> {}".format(alvo))
            for email in emails:
                print("\n\nEmail encontrado -> {}\n\n".format(email))

        break
    except Exception as ex:
        print(ex)
    

