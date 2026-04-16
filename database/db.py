import sqlite3
from pathlib import Path

class dataBase:

    PATH = Path(__file__).parent

    def __init__(self):
        """Conecta ao banco de dados e cria as tabelas se não existirem."""
        self.con = sqlite3.connect(self.PATH / "database.db", check_same_thread=False)
        self.cur = self.con.cursor()
        self.create_tables()

    def create_tables(self):
        """Cria a tabela Athletes no banco de dados."""
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS Athletes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(40),
                icon_path VARCHAR(255)
            )
        """)

    def query(self, query: str, data=tuple()):
        """Executa uma consulta no banco de dados."""
        try:
            self.cur.execute(query, data)
            self.con.commit()
        except Exception as err:
            self.con.rollback()
            raise err