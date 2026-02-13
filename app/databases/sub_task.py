import sqlite3

class SubTasksDatabase():

    def __init__(self,conn : sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()
        self._create_table()
    
    def _create_table(self):
        self.cursor.execute("""CREATE TABLE subtasks(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            task_id INTEGER NOT NULL,
                            FOREIGN KEY(task_id) REFERENCES subtasks(id)) """)
        self.conn.commit()
    
    def add_subtask(self,name:str,task_id:int):
        with self.conn:
            self.cursor.execute("INSERT INTO subtasks (name,task_id) VALUES (:name,:task_id)",{"name":name,"task_id":task_id})
    
    def get_subtask_of_id(self,id:int):
        self.cursor.execute("SELECT * FROM subtasks WHERE id=:id",{"id":id})
        return dict(self.cursor.fetchone())
    
    def get_subtasks_of_task_id(self,id:int):
        self.cursor.execute("SELECT * FROM subtasks WHERE task_id=:id",{"id":id})
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]
    
    def get_all(self):
        self.cursor.execute("SELECT * FROM subtasks")
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def remove_subtask(self,id:int):
        with self.conn:
            self.cursor.execute("DELETE from subtasks WHERE id=:id",{"id":id})