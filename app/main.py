from fastapi import FastAPI
import json
from databases.database_manager import DatabaseManager,DatabaseTable

manager = DatabaseManager(":memory:")
manager.categories.add_category("test")
manager.categories.add_category("2test")
manager.tasks.add_task("tarea_1",1)
manager.tasks.add_task("tarea_2",1)
manager.tasks.add_task("tarea_3",2)

app = FastAPI()

@app.get("/")
def root():
	return {"Status" : "Working"}