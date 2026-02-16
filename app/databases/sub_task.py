import sqlite3

class SubTasksDatabase():

    class SubTask():
        id:int
        name:str
        task_id:int

        def __init__(self,id:int,name:str,task_id:int):
            self.id = id
            self.name = name
            self.task_id = task_id

    def __init__(self,conn : sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()
        self._create_table()
    
    def _create_table(self):
        self.cursor.execute("""CREATE TABLE subtasks(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            task_id INTEGER NOT NULL,
                            FOREIGN KEY(task_id) REFERENCES tasks(id)) """)
        self.conn.commit()
    
    def add_subtask(self,name:str,task_id:int) -> None:
        with self.conn:
            self.cursor.execute("INSERT INTO subtasks (name,task_id) VALUES (:name,:task_id)",{"name":name,"task_id":task_id})
    
    def get_subtask_of_id(self,id:int) -> SubTask:
        self.cursor.execute("SELECT * FROM subtasks WHERE id=:id",{"id":id})
        return self._row_to_subtask(self.cursor.fetchone())
    
    def get_subtasks_of_task_id(self,id:int) -> list[SubTask]:
        self.cursor.execute("SELECT * FROM subtasks WHERE task_id=:id",{"id":id})
        rows = self.cursor.fetchall()
        result = list()
        for row in rows:
            result.append(self._row_to_subtask(row))
        return result
    
    def get_all(self) -> list[SubTask]:
        self.cursor.execute("SELECT * FROM subtasks")
        rows = self.cursor.fetchall()
        result = list()
        for row in rows:
            result.append(self._row_to_subtask(row))
        return result

    def remove_subtask(self,id:int) -> None:
        with self.conn:
            self.cursor.execute("DELETE from subtasks WHERE id=:id",{"id":id})
    
    def _row_to_subtask(self,row) -> SubTask:
        return self.SubTask(row.id,row.name,row.task_id)