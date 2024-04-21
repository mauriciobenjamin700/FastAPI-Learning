"""
DDL (Data Definition Language): Esta parte da linguagem SQL é usada para definir e modificar a estrutura de objetos de banco de dados, como tabelas, índices, visões e assim por diante. Exemplos de comandos DDL incluem CREATE TABLE, ALTER TABLE, DROP TABLE, CREATE INDEX, CREATE VIEW, entre outros.
"""


class Register:
    """
    Atributos:
        - id: int,
        - name: str,
        - description: str,
        - gender: str,
        - country: str,
        - occupation: str,
        - birth: int,
        - death: int,
        - cause_death: str,
        - age_death: int,



    """

    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        gender: str,
        country: str,
        occupation: str,
        birth: int,
        death: int,
        cause_death: str,
        age_death: int,
    ) -> None:

        self.id = id
        self.name = name
        self.description = description
        self.gender = gender
        self.gender_country = country
        self.occupation = occupation
        self.birth = birth
        self.death = death
        self.cause_death = cause_death
        self.age_death = age_death

    def __str__(self) -> str:
        return f"Register(id={self.id}, name={self.name}, description={self.description}, gender={self.gender}, gender_country={self.gender_country}, occupation={self.occupation}, birth={self.birth}, death={self.death}, cause_death={self.cause_death}, age_death={self.age_death})"

    def __repr__(self) -> str:
        return f"Register(id={self.id}, name={self.name}, description={self.description}, gender={self.gender}, gender_country={self.gender_country}, occupation={self.occupation}, birth={self.birth}, death={self.death}, cause_death={self.cause_death}, age_death={self.age_death})"
