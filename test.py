from fastapi import FastAPI, Path
import uvicorn
import io
from starlette.responses import StreamingResponse
#https://www.youtube.com/watch?v=-ykeT6kk4bk
#24:54
myapp = FastAPI()
#how to load up a :8000
#http://localhost:8080
#http://localhost:8080/get-by-name?name=Milk
#http://localhost:8080/docs
#http://localhost:8080/get-item/1/test
#http://localhost:8080/vector_image

#uvicorn main:app --port 8086  --reload
1

@myapp.get("/a")
async def root():
   return {"message": {"Hello_Wosrl1d":"googbye"}}

inventory = {
    1: {
        "name" : "Milk",
        "price" : 3.99,
        "brand" : "Regular"
    }
}



@myapp.get("/about")
async def root():
    return{"Data":"about"}

if __name__ == '__main__':
    uvicorn.run(myapp, port=8080, host='0.0.0.0')

inventory = {
    1: {
        "name" : "Milk",
        "price" : 3.99,
        "brand" : "Regular"
    }
}
@myapp.get("/get-item/{item_id}")
def get_item(item_id:int, name:str ):
    return inventory[item_id].update

@myapp.get("/")
def get_item(name:str ):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Date" : "not found"}




@myapp.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@myapp.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@myapp.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@myapp.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@myapp.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is created with title as {blog.title}"}