import sqlite3

class TasksDatabase():

    class Task():
        id:int
        name:str
        category_id:int

        def __init__(self,id:int,name:str,category_id:int):
            self.id = id
            self.name = name
            self.category_id = category_id

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
    
    def get_task_of_id(self,id:int) -> Task:
        self.cursor.execute("SELECT * FROM tasks WHERE id=:id",{"id":id})
        return self._row_to_task(self.cursor.fetchone())
    
    def get_tasks_of_category_id(self,id:int) -> list[Task]:
        self.cursor.execute("SELECT * FROM TASKS WHERE category_id=:id",{"id":id})
        rows = self.cursor.fetchall()
        result = list()
        for row in rows:
            result.append(self._row_to_task(row))
        return result
    
    def get_all(self) -> list[Task]:
        self.cursor.execute("SELECT * FROM tasks")
        rows = self.cursor.fetchall()
        result = list()
        for row in rows:
            result.append(self._row_to_task(row))
        return result

    def remove_task(self,id:int) -> None:
        with self.conn:
            self.cursor.execute("DELETE from tasks WHERE id=:id",{"id":id})
    
    def _row_to_task(self,row) -> Task:
        return self.Task(row.id,row.name,row.category_id)