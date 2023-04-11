from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get("/")
def root():
    return {"message":"Welcome to my API"}

@app.get("/posts")
def get_posts():
    return {"data":"This is your post."}

@app.post("/createposts")
def create_posts(new_posts: Post):
    print(new_posts)
    return {"data":new_posts}
    # Title string, content string