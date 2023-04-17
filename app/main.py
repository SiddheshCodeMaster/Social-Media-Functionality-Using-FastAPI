from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randint, randrange
from fastapi import Response 
from fastapi import status
from fastapi import HTTPException

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title":"title of post 1","content":"content of post 1", "id":1}, 
            {"title":"favorite foods", "content":"Pizza","id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
    
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def root():
    return {"message":"Welcome to the Social Media Functionality using FastAPI."}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} was not found")
    return {"post_detail":post}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data":post_dict}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # deleting post
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with {id} does not exist.")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with {id} does not exist.")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {'message':'updated post'}

# Database connectivity with Postgre SQL: