from fastapi import FastAPI, Path
#https://www.youtube.com/watch?v=-ykeT6kk4bk
#24:54
app = FastAPI()
#how to load up a :8000
#http://127.0.0.1:8000 
#uvicorn test:app --reload

@app.get("/get-item/{item_id}")
def home():
    return {"Data":"Test"}

