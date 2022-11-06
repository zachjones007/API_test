from fastapi import FastAPI, Path
import uvicorn
#https://www.youtube.com/watch?v=-ykeT6kk4bk
#24:54
app = FastAPI()
#how to load up a :8000
#http://localhost:8080
#uvicorn main:app --port 8086  --reload


@app.get("/")
async def root():
    return {"message": "Hello_World"}


@app.get("/about")
def about():
    return{"Data":"about"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')

