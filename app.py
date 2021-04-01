import uvicorn
from pydantic import BaseModel
from Prediction import *
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()

class query(BaseModel):
    txt: str


@app.post("/result")
def result(line:query):
    return predict(line.txt)



if __name__ =="__main__":
    uvicorn.run(app,host = "127.0.0.1",port =9000)