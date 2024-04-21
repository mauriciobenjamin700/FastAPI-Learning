CREATE TABLE IF NOT EXISTS Historical_character (
    id VARCHAR(11),
    name VARCHAR(30),
    description VARCHAR(100),
    gender VARCHAR(6),
    country VARCHAR(100),
    occupation VARCHAR(50),
    birth INTEGER,
    death INTEGER,
    cause_death VARCHAR(30),
    age_death INTEGER
)

-- #TODO:  por hora vou desconsiderar id como chave primaria por causa do dataset, quanto eu terminar a limpeza nos dados, resolvo isso