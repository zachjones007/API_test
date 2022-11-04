from fastapi import FastAPI
#https://www.youtube.com/watch?v=-ykeT6kk4bk
app = FastAPI()
#uvicorn test:app --reload
@app.get("https://randomfox.ca/floof")
async def root():
    return {"message": "Hello World"}
 