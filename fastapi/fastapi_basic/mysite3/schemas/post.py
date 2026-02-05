#데이터 모델
#request, response에 대한 dto
from pydantic import BaseModel


class Post:
    def __init__(self, title, content):
        self.id = None
        self.title = title
        self.content = content


class PostCreate(BaseModel):
    title: str
    content: str


class PostDetailResponse(BaseModel):
    id: int
    title: str
    content: str


class PostListResponse(BaseModel):
    id: int
    title: str

    