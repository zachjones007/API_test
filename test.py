from fastapi import FastAPI, Path
#https://www.youtube.com/watch?v=-ykeT6kk4bk
#24:54
app = FastAPI()
#how to load up a :8000
#http://127.0.0.1:8000 
#uvicorn test:app --reload

inventory = {
    1:{
        "name" : "MILK",
        "price " : 3.99,
        "brand " : " regular"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None,description = "the id of the idem ")):

    async def root():
        return {"message": "Hello World"}
        return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return {"Data" : "not Found"}

