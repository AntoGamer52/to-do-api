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
    
    def add_task(self,name:str,category_id:int):
        with self.conn:
            self.cursor.execute("INSERT INTO tasks (name,category_id) VALUES (:name,:category_id)",{"name":name,"category_id":category_id})
    
    def get_task_of_id(self,id:int):
        self.cursor.execute("SELECT * FROM tasks WHERE id=:id",{"id":id})
        return dict(self.cursor.fetchone())
    
    def get_tasks_of_category_id(self,id:int):
        self.cursor.execute("SELECT * FROM TASKS WHERE category_id=:id",{"id":id})
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]
    
    def get_all(self):
        self.cursor.execute("SELECT * FROM tasks")
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def remove_task(self,id:int):
        with self.conn:
            self.cursor.execute("DELETE from tasks WHERE id=:id",{"id":id})