import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient

from source.login1 import User

client = MongoClient()
mydatabase = client.login1
data = mydatabase.myTable

app = FastAPI()
def compare(item: str,passw:str):
    myquery = {"email": item,"password":passw}
    for x in data.find(myquery):
        print(x)
        return 1;
    return 0
@app.post("/items/", response_model=User)
async def create_item(item: User):
    if item:
        if compare(item.email,item.password):
            print("you login successfully")
        else :
            print("userId or password not match..")
    return item


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
