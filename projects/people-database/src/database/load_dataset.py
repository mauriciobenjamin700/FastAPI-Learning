import csv
import sqlite3
from os.path import join


csv_file = join("docs", "data","AgeDataset-V1.csv")

conn = sqlite3.connect('historic.db')

cursor = conn.cursor()


with open(csv_file, newline='', encoding='utf-8') as csvfile:
    
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Pular cabeçalho, neste caso há cabeçalho e não é do nosso interesse

    
    cursor.executemany('''
        INSERT INTO Historical_character VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', csv_reader)

# Commitar as alterações e fechar a conexão
conn.commit()
conn.close()

print("Registros do CSV foram inseridos no banco de dados com sucesso!")
