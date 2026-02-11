import sqlite3

class TasksDatabase():

    def __init__(self,conn : sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()
        self._create_table()
    
    def _create_table(self):
        self.cursor.execute("""CREATE TABLE tasks(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            category_id INTEGER NOT NULL,
                            FOREIGN KEY(category_id) REFERENCES categories(id)) """)
        self.conn.commit()
    
    def add_task(self,name:str):
        with self.conn:
            self.cursor.execute("INSERT INTO tasks (name) VALUES name=:name",{"name":name})
    
    def get_task_of_id(self,id:int):
        self.cursor.execute("SELECT * FROM tasks WHERE id=:id",{"id":id})
        return self.cursor.fetchone()

    def remove_task(self,id:int):
        with self.conn:
            self.cursor.execute("DELETE from tasks WHERE id=:id",{"id":id})