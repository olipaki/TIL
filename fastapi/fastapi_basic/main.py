from fastapi import FastAPI
from mysite2.post_api import router as pydantic_router

from mysite4.routers.post_router import router as db_router

##################################################
from database import engine, Base
from mysite4.models.post import Post  # 모델 파일이 import되어야 Base가 인식한다.

###################################################
Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# app = FastAPI()
# app.include_router(posr_router)
app.include_router(pydantic_router)
app.include_router(db_router)
