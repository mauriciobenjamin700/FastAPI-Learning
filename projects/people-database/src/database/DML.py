"""
DML (Data Manipulation Language): A DML é usada para manipular dados dentro de objetos de banco de dados. Isso inclui operações como inserir, atualizar, excluir e recuperar dados de tabelas. Exemplos de comandos DML incluem SELECT, INSERT, UPDATE, DELETE.
"""

def get_all_registers() -> str:
    
    query = "SELECT * FROM Historical_character"
    
    return query