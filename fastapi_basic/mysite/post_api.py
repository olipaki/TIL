# mysite/post_api.py

from fastapi import APIRouter
from .post import Post

router = APIRouter()

# 게시글 객체들을 저장하는 리스트
posts = []
post_id = 0


@router.get("/posts/create")
def create_post():
    # 식별자 1 증가
    global post_id
    post_id += 1
    # 새로운 게시글 객체 생성
    post = Post(post_id, "제목", "내용")
    # 리스트에 추가
    posts.append(post)
    print(posts)
    return post


# mysite/post_api.py 내부에 추가

# 초기 데이터 추가를 위한 구문
posts.append(Post(1, "기본 제목", "기본 내용"))
post_id = 1


@router.get("/posts")
def read_posts():
    # 게시글 리스트 전체를 반환
    return posts


# mysite/post_api.py 내부에 추가


@router.get("/posts/{id}")
def read_post_by_id(id: int):
    # 리스트 내 객체들을 하나씩 검사
    for post in posts:
        # 객체의 식별자와 입력받은 식별자가 일치하는지 확인
        if post.id == id:
            return post
    return None
