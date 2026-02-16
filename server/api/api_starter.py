from fastapi import FastAPI
from server.databases.database_manager import DatabaseManager

class ServerAPI():

    def __init__(self,app:FastAPI,DatabaseManager:DatabaseManager):
        self.app = app
        self.DatabaseManager = DatabaseManager
        self.setUp()
    
    def setUp(self):

        # =================== GET =====================

        @self.app.get("/categories")
        def get_categories():
            return self.DatabaseManager.get_all_of(self.DatabaseManager.DatabaseTable.Categories)

        @self.app.get("/tasks")
        def get_tasks():
            return self.DatabaseManager.get_all_of(self.DatabaseManager.DatabaseTable.Tasks)
        
        @self.app.get("/subtasks")
        def get_subtasks():
            return self.DatabaseManager.get_all_of(self.DatabaseManager.DatabaseTable.Sub_Tasks)
        
        @self.app.get("/all")
        def get_all():
            return self.DatabaseManager.get_all_of()
        
        # =================== POST =====================

        @self.app.post("/create_category")
        def set_category(name:str):
            self.DatabaseManager.categories.add_category(name)
            return

        @self.app.post("/create_tasks")
        def set_tasks(name:str,category_id:int):
            self.DatabaseManager.tasks.add_task(name,category_id)
            return
        
        @self.app.post("create_subtasks")
        def set_subtasks(name:str,tasks_id:int):
            self.DatabaseManager.subtask.add_subtask(name,tasks_id)
            return

        # =================== DELETE =====================

        @self.app.delete("/delete_category")
        def delete_category(id:int):
            self.DatabaseManager.delete_category(id)
            return
        
        @self.app.delete("/delete_task")
        def delete_task(id:int):
            self.DatabaseManager.delete_task(id)
            return
        
        @self.app.delete("/delete_subtask")
        def delete_subtask(id:int):
            self.DatabaseManager.delete_subtask(id)
            return
