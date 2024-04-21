from os.path import join
from sqlite3 import connect

# Conecta com um banco de dados existe ou cria um novo no diretório raiz
conn = connect("historic.db")

cursor = conn.cursor()

# Vamos criar um banco de dados com base na documentação que criamos

with open(join("docs","data","schema.sql"),'r') as file:
    schema = file.read()
    
# executa nosso script sql para criação do banco de dados e suas tabelas
cursor.executescript(schema)

# Commitar as alterações e fechar a conexão
conn.commit()
conn.close()
