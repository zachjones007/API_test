from fastapi import FastAPI, Path
import uvicorn
#https://www.youtube.com/watch?v=-ykeT6kk4bk
#24:54
app = FastAPI()
#how to load up a :8000
#http://localhost:8080
#http://localhost:8080/docs
#http://localhost:8080/get-item/1/test
#uvicorn main:app --port 8086  --reload
1

@app.get("/")
async def root():
   return {"message": "Hello_Wosrl1d"}



@app.get("/about")
async def root():
    return{"Data":"about"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')

inventory = {
    1: {
        "name" : "Milk",
        "price" : 3.99,
        "brand" : "Regular"
    }
}
@app.get("/get-item/{item_id}")
def get_item(item_id:int, name:str ):
    return inventory[item_id].update