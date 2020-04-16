import uvicorn
from fastapi import FastAPI, Query
from pydantic import BaseModel
from pymongo import MongoClient

client = MongoClient()
mydatabase = client.login1
data = mydatabase.myTable

app = FastAPI()


class User(BaseModel):
    email: str = Query(..., max_length=100, regex="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
    password: str = Query(..., min_length=6, max_length=15, regex="^(?=.*[0-9]+.*)(?=.*[a-zA-Z]+.*)[0-9a-zA-Z]{6,}$")


def compare(item: str):
    myquery = {"email": item}
    for x in data.find(myquery):
        return 0;
    return 1
    
def show():
    for x in data.find():
        print(x)


@app.post("/items/", response_model=User)
async def create_item(item: User):
    if item:
        if compare(item.email):
            rec = {
                "email": item.email,
                "password": item.password
            }
            data.insert_one(rec)
        else :
            print("userId already exist..")
        show()
        return item


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
