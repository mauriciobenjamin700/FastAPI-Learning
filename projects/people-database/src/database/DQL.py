"""
DQL (Data Query Language): Algumas pessoas também se referem à parte da linguagem SQL que lida apenas com consultas como DQL. Isso inclui apenas o comando SELECT para recuperar dados de tabelas.
"""


def get_all_registers(table: str = "Historical_character") -> str:

    query = f"SELECT * FROM {table}"

    return query


def get_registers(name: str, table: str = "Historical_character") -> str:

    query = f"SELECT * FROM {table} WHERE name = '{name}'"

    return query


def add_register(table: str = "Historical_character") -> str:

    query = f"""
    INSERT INTO {table} 
    (
        id,
        name, 
        description, 
        gender, 
        country, 
        occupation, 
        birth, 
        death, 
        cause_death, 
        age_death
    ) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    return query


def delet_register(
    column: str, value: int | str, table: str = "Historical_character"
) -> str:

    if value is str:
        query = f"DELETE FROM {table} WHERE {column} = '{value}'"
    else:
        query = f"DELETE FROM {table} WHERE {column} = {value}"

    return query
