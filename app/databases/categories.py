import sqlite3

class CategoriesDatabase():

    def __init__(self,conn : sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()
        self._create_table()
    
    def _create_table(self):
        self.cursor.execute("""CREATE TABLE categories(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL)""")
        self.conn.commit()
    
    def add_category(self,name:str):
        with self.conn:
            self.cursor.execute("INSERT INTO categories (name) VALUES name=:name",{"name":name})
    
    def get_category_of_id(self,id:int):
        self.cursor.execute("SELECT * FROM categories WHERE id=:id",{"id":id})
        return self.cursor.fetchone()

    def remove_category(self,id:int):
        with self.conn:
            self.cursor.execute("DELETE from categories WHERE id=:id",{"id":id})