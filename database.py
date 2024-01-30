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

def inserir_dados(empresa, companhia_de_voo, preco_total, taxa_de_embarque, taxa_de_servico, tempo_de_voo, data_hora_ida, data_hora_volta):
    conn = sqlite3.connect('dados_voos.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO voos (empresa, companhia_de_voo, preco_total, taxa_de_embarque, taxa_de_servico, tempo_de_voo_minutes, data_hora_ida, data_hora_volta)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (empresa, companhia_de_voo, preco_total, taxa_de_embarque, taxa_de_servico, tempo_de_voo, data_hora_ida, data_hora_volta))
    conn.commit()
    conn.close()