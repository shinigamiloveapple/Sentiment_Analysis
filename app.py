import uvicorn
from pydantic import BaseModel
from Prediction import * # importing all the functions from Prediction.py
from fastapi import Depends, FastAPI, HTTPException, status

# Creating FastAPI instance
app = FastAPI()

# Creating data model using pydantic BaseModel
class query(BaseModel):
    txt: str


@app.post("/result") # assigning result as path parameter
def result(line:query):
    return predict(line.txt)



if __name__ =="__main__":
    uvicorn.run(app,host = "127.0.0.1",port =9000)