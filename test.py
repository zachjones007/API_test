from fastapi import FastAPI

app = FastAPI()

@app.get("https://randomfox.ca/floof")
async def root():
    return {"message": "Hello World"}
