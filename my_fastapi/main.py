from fastapi import FastAPI

# My_site 폴더 안에 있는 A_site 파일을 불러옵니다
from My_site import A_site

app = FastAPI()
# 핵심: A_site의 라우터를 등록합니다.
app.include_router(post.router)
app.include_router(pydantic_router)


@app.get("/")
def root():
    return {"message": "메인 안내 데스크입니다. /products로 가보세요!"}
