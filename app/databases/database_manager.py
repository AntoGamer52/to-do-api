import sqlite3
from databases.categories import CategoriesDatabase
from databases.tasks import TasksDatabase
from databases.sub_task import SubTasksDatabase
from enum import Enum

class DatabaseTable(Enum):
    Categories = "categories"
    Tasks = "tasks"
    Sub_Tasks = "subtasks"

class DatabaseManager():
    
    def __init__(self,path : str):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row

        self.categories = CategoriesDatabase(self.conn)
        self.tasks = TasksDatabase(self.conn)
        self.subtask = SubTasksDatabase(self.conn)

        self.tables = 3
    
    def get_all_of(self,*tables) -> dict[str : list[sqlite3.Row]]:
        result = dict()

        if tables:
            for table in tables:
                result[str(table.value)] = self._get_table_instance(table).get_all()
        else:
            result["categories"] = self.categories.get_all()
            result["tasks"] = self.tasks.get_all()
            result["subtasks"] = self.subtask.get_all()
        
        return result
    
    def _get_table_instance(self, table: DatabaseTable):
        mapping = {
            DatabaseTable.Categories: self.categories,
            DatabaseTable.Tasks: self.tasks,
            DatabaseTable.Sub_Tasks: self.subtask,
        }
        return mapping.get(table)