from fastapi import FastAPI
import json
from databases.database_manager import DatabaseManager
from api.api_starter import ServerAPI

manager = DatabaseManager("databases/file.db")
manager.categories.add_category("test")
manager.categories.add_category("2test")
manager.tasks.add_task("tarea_1",1)
manager.tasks.add_task("tarea_2",1)
manager.tasks.add_task("tarea_3",2)

manager.subtask.add_subtask("subtarea_1",2)
manager.subtask.add_subtask("subtarea_2",2)
manager.subtask.add_subtask("subtarea_3",2)
manager.subtask.add_subtask("subtarea_4",1)
manager.subtask.add_subtask("subtarea_5",3)
manager.subtask.add_subtask("subtarea_6",3)

app = FastAPI()

@app.get("/")
def root():
	return {"Status" : "Working"}

server = ServerAPI(app,manager)

server = ServerAPI(app,manager)

