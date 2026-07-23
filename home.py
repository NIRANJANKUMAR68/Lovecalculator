from fastapi import FastAPI,HTTPException,Depends
from database import *
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_credentials =True,
                   allow_methods =["*"],
                   allow_headers =["*"]
      
)

class Student(BaseModel):
    name1:str
    name2:str
@app.post("/sregister")
def register(data: Student,db=Depends(get_db)):
    rec=db.query(Love).filter(Love.name1==data.name1,Love.name2==data.name2).first()
    if rec:
         return f"Data Already exists\n{rec.name1} and {rec.name2} ->{rec.percentage}"
    else:
        import random
        love_perc = random.randint(10, 100)
        record=Love(name1=data.name1,name2=data.name2,percentage=love_perc)
        db.add(record)
        db.commit()
        return f"{data.name1}, your love percentage is {love_perc}%"


