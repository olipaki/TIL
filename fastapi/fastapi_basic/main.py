from fastapi import FastAPI
from mysite2.post_api import router as pydantic_router

from mysite4.routers.post_router import router as db_router

##################################################
from database import engine
from mysite4 import models

# 기존 테이블 지우기
# models.Base.metadata.drop_all(bind=engine)

# 정의된 모델들을 기반으로 DB에 테이블을 생성한다.
models.Base.metadata.create_all(bind=engine)
###################################################
# - 즉, 아래 코드는 삭제된다
#     from database import engine, Base # -> engine만 남게 된다.
#     from mysite4.models.post import Post  # 모델 파일이 import되어야 Base가 인식한다.
#     from mysite4.models.comment import Comment
####################################################
# models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# app = FastAPI()
# app.include_router(posr_router)
app.include_router(pydantic_router)
app.include_router(db_router)
