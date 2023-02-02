from datetime import datetime
from fastapi import FastAPI, Path, Query, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI();
class Todos(BaseModel):
    title : str
    description : str
    deadline : datetime
    status : bool 

class UpdateTodos(BaseModel):
    title : Optional[str] = None
    description : Optional[str] = None
    deadline : Optional[datetime] = None
    status : Optional[bool] = None


todoDictionary = {
   
}

#To get todo detials by id using path parameter
@app.get("/get-by-id/{todo_id}")
def get_todo(todo_id : int = Path(None, description="The id of the item you need to view")) :
    return todoDictionary[todo_id]

#To get todo detials by name using Query parameter
@app.get("/get-by-title")
def get_todo(title : str):
    for todo_id in todoDictionary:
        if todoDictionary[todo_id].title == title:
            return todoDictionary[todo_id]
    raise HTTPException(status_code = 404, detail = "todo title not found") 

#To post todo detials using request body and path parameter
@app.post("/create-todo/{todo_id}")
def create_todo(todo_id:int,todo : Todos):
    if todo_id in todoDictionary:
        return {"Error" : "Todo ID already exixts"}
    #returning the object into the dictionary
    todoDictionary[todo_id] = todo
    return todoDictionary[todo_id]

##To update todo detials using Path parameter
@app.put("/update-todo/{todo_id}")
def update_todo(todo_id : int,todo :UpdateTodos):
    if todo_id not in todoDictionary:
        raise HTTPException(status_code = 404, detail = "todo id not found") 
    if todo.title != None:
        todoDictionary[todo_id].title = todo.title
    if todo.description != None:
        todoDictionary[todo_id].description = todo.description
    if todo.deadline != None:
        todoDictionary[todo_id].deadline = todo.deadline
    if todo.status != None:
        todoDictionary[todo_id].status = todo.status
    return todoDictionary[todo_id]
 
 ##To delete todo detials by using Query parameter
@app.delete("/delete-todo")
def delete_todo(todo_id : int):
    if todo_id not in todoDictionary:
        return {"Error" : "Todo ID does not exixts"}
        
    del todoDictionary[todo_id]
    return{"success" : "item deleted"}