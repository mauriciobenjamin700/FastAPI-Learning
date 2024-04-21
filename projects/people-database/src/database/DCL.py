"""
DCL (Data Control Language): A DCL é usada para controlar os privilégios de acesso aos objetos de banco de dados. Isso inclui comandos para conceder ou revogar permissões de acesso, como GRANT e REVOKE.
"""
from sqlite3 import connect

class DataBase():
    def __init__(self, databasePATH: str = "historic.db") -> None:
        
        self.database = databasePATH
        self.isconnet = False
        self.conn = None
        self.cursor = None
        
        self.connect()
        
    
    def connect(self) -> bool:
        
        if self.isconnet == False:
        
            self.conn = connect(self.database)
            self.cursor = self.conn.cursor()
            self.isconnet = True
        
        return self.isconnet
        
    def disconnect(self) -> bool:
        
        if self.isconnet == True:
        
            self.cursor.close()
            self.conn.close()
            
            self.conn = None
            self.cursor = None
            self.isconnet = False
        
        return self.isconnet
        
              
    def execute(self, query: str):
        result = self.cursor.execute(query)
        self.conn.commit()
        
        return result
    