import sqlite3
import json
from datetime import datetime

conn = sqlite3.connect("data.db")
cursor = conn.cursor()


def salvar_email(email):
    data = (email, datetime.now())

    cursor.execute("""
        INSERT INTO emails (email, data_hora)
        VALUES (?, ?)
        """, data)

    conn.commit()

def email_existe(email):
    data = (email,)
    cursor.execute("""
        SELECT COUNT(0) FROM emails WHERE email = ?
        """, data)
    result = cursor.fetchone()
    return result[0] > 0

def criar_tabela_se_nao_existir():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        data_hora DATETIME
    )
    """)

    conn.commit()

criar_tabela_se_nao_existir()