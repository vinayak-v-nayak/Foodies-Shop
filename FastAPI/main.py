from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class CourseType(BaseModel):
    name : str
    lname:str
    age: str



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/User/{user_id}")
async def user_data(user_id:int):
    return {user_id: f"this is the data {user_id}"}



@app.get("/User/{CourseType}")
async def user_data2(CourseType:str):
    return {user_id: f"this is the data {user_id}"}


