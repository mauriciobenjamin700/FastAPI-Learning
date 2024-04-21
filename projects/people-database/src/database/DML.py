"""
DML (Data Manipulation Language): A DML é usada para manipular dados dentro de objetos de banco de dados. Isso inclui operações como inserir, atualizar, excluir e recuperar dados de tabelas. Exemplos de comandos DML incluem SELECT, INSERT, UPDATE, DELETE.
"""

from os.path import dirname, abspath
import sys
from sqlite3 import Cursor
from uuid import uuid1

sys.path.insert(0, dirname(abspath(__file__)))

from DQL import *
from DDL import *


def get_database(result: Cursor):
    """
    Retorna uma lista de tuplas, onde cada tupla é um registro do banco de dados
    """
    return result.fetchall()


def search_item(cursor: Cursor):
    """"""

    result = cursor.fetchall()

    return result


def delete_item(column: str, value: int | str, table: str = "Historical_character"):
    query = delet_register(column, value, table)


def add_item(
    name: str,
    description: str,
    gender: str,
    country: str,
    occupation: str,
    birth: int,
    death: int,
    cause_death: str,
    age_death: int,
) -> tuple:
    """
    Retorna uma tupla com todos os atributos necessário para criar um registro
    """
    return (
        str(uuid1())[0:12],
        name,
        description,
        gender,
        country,
        occupation,
        birth,
        death,
        cause_death,
        age_death,
    )
