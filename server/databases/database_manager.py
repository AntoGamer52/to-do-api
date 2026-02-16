import sqlite3
from .categories import CategoriesDatabase
from .tasks import TasksDatabase
from .sub_task import SubTasksDatabase
from enum import Enum

class DatabaseManager():

    class DatabaseTable(Enum):
        Categories = "categories"
        Tasks = "tasks"
        Sub_Tasks = "subtasks"
    
    def __init__(self,path : str):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row

        self.categories = CategoriesDatabase(self.conn)
        self.tasks = TasksDatabase(self.conn)
        self.subtask = SubTasksDatabase(self.conn)

        self.tables = 3
    
    def get_all_of(self,*tables) -> dict[str , list[sqlite3.Row]]:
        result = dict()
        dict[str,str]

        if tables:
            for table in tables:
                tab = self._get_table_instance(table)
                if tab:
                    result[str(table.value)] = tab.get_all()
                else:
                    print(f"Tabla {table} no existe.")
        else:
            result["categories"] = self.categories.get_all()
            result["tasks"] = self.tasks.get_all()
            result["subtasks"] = self.subtask.get_all()
        
        return result
    
    def _get_table_instance(self, table: DatabaseTable):
        mapping = {
            self.DatabaseTable.Categories: self.categories,
            self.DatabaseTable.Tasks: self.tasks,
            self.DatabaseTable.Sub_Tasks: self.subtask,
        }
        return mapping.get(table)
    
    def delete_category(self,id:int):
        tasks = self.tasks.get_tasks_of_category_id(id)
        if tasks:
            for task in tasks:
                self.delete_task(task.id)
        self.categories.remove_category(id)
    
    def delete_task(self,id:int):
        subtasks = self.subtask.get_subtasks_of_task_id(id)
        if subtasks:
            for subtask in subtasks:
                self.subtask.remove_subtask(subtask.id)
        self.tasks.remove_task(id)
    
    def delete_subtask(self,id:int):
        self.subtask.remove_subtask(id)