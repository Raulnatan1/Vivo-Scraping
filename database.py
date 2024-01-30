import sqlite3

conn = sqlite3.connect('dados_voos.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE produtos (
        id INTEGER PRIMARY KEY,
        modelo TEXT,
        capacidade_gb INTEGER,
        tamanho_tela TEXT,
        preco_total REAL,
        valor_parcela REAL,
        cor TEXT,
        ultimas_pecas INTEGER
    );''')

def inserir_dados(modelo, capacidade_gb, tamanho_tela, preco_total, valor_parcela, cor, ultimas_pecas):
    conn = sqlite3.connect('dados_voos.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO produtos (modelo, capacidade_gb, tamanho_tela, preco_total, valor_parcela, cor, ultimas_pecas)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (modelo, capacidade_gb, tamanho_tela, preco_total, valor_parcela, cor, ultimas_pecas))
    conn.commit()
    conn.close()