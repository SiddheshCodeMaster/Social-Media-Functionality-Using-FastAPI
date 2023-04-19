from typing import Optional
from fastapi import Depends, FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randint, randrange
from fastapi import Response 
from fastapi import status
from fastapi import HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session

from . import models
from .database import engine
from .database import get_db
models.Base.metadata.create_all(bind = engine)

app = FastAPI()
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

# Database connectivity with Postgre SQL:
while True:
    try:
        conn =psycopg2.connect(host='localhost',
                           database='fastapi', 
                           user='postgres', 
                           password='password1234',
                           cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull.")
        break
    except Exception as error:
        print("Connecting to the database failed")
        print("Error: ", error)
        time.sleep(2)


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

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}

@app.get("/")
def root():
    return {"message":"Welcome to the Social Media Functionality using FastAPI."}

@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    # print(posts)
    return {"data":posts}

@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
    # test_post = cursor.fetchone()
    posts = db.query(models.Post).filter(models.Post.id == id).first()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    return {"post_detail":posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post,db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
    #                 (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    #print(**post.dict()) # unpack the dictionary
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data":new_post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    
    # cursor.execute("""DELETE FROM posts WHERE id =  %s RETURNING *""", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    
    if deleted_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id {id} does not exist.")
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, updated_post: Post, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", 
    #                (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id {id} does not exist.")
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return {'message':post_query.first()}


