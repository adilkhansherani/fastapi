from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import app.models as models
from app.database import engine
from .routers import post,auth,user,vote
from .config import settings

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get('/')
def root():
    return {'message':'hello there'}

'''@app.get('/posts', response_model=List[schemas.Post])
def post(db:Session=Depends(get_db)):
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    return posts

@app.get('/sqlalchemy')
def post(db:Session=Depends(get_db)):
    posts = db.query(models.Post).all()
    return {'data':posts}

@app.get('/posts/{id}', response_model=schemas.Post)
def get_post(id:int,db:Session=Depends(get_db)): 
    #cursor.execute("""SELECT * FROM posts WHERE id={%s}""",str(id))
    #post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post,id== id).all()

    if not post:
        raise HTTPException( status_code= status.HTTP_404_NOT_FOUND,
                            detail={'message': f'post with id :{id} was not found'})
    
    return {'message':f'hello there id is {id}','post_details':post}

@app.post('/createposts',status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post:schemas.PostCreate, db: Session=Depends(get_db)):
    #cursor.execute(""" INSERT INTO posts (title, content, published) VALUES ( %S, %S, %S) RETURNING *""",
    #               (post.title, post.content, post.published))
    #new_post = cursor.fetchone()
    #cursor.commit()
    new_post = models.Post(**post.model_dump())#title = post.title, content = post.content , published = post.published)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return  new_post


@app.delete('/posts/{id}')
def delete_post(id:int,db:Session=Depends(get_db)):
    #cursor.execute("""DELETE FROM posts WHERE id={%s} RETURNING * """,str(id))
    #deleted_post = cursor.fetchone()
    #cursor.commit()
    
    post = db.query(models.Post).filter(models.Post.id==id)

    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id : {id} does not exist')
    
    return {'message':'deleted'}

@app.put('/posts/{id}', response_model=schemas.Post)
def update_post(id:int, updated_post:schemas.PostCreate,db :Session=Depends(get_db)):

    #cursor.execute(""" UPDATE posts SET (title, content) VALUES ( %s, %s) WHERE id = %s RETURNING * """,
    #               (post.title, post.content, str(id)))
    #updated_post = cursor.fetchone()
    #cursor.commit()

    post_query = db.query(models.post).filter(models.Post.id==id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id : {id} does not exist')
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    
    return post_query.first()'''
