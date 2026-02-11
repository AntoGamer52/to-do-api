import sqlite3
from categories import CategoriesDatabase
from tasks import TasksDatabase

class DatabaseManager():
    
    def __init__(self,path : str):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row

        self.categories = CategoriesDatabase(self.conn)
        self.tasks = TasksDatabase(self,self.conn)

DatabaseManager(":memory:")