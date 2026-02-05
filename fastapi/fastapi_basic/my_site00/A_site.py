from fastapi import APIRouter
from .A_site import PostCreate, Post

# 1. 라우터 설정 (가전 매장 전용 리모컨)
# 경로 접두사 설정
router = APIRouter(prefix="/posts-pydantic")

# 게시글 저장소 역할을 수행하는 리스트
posts = []
# 고유 식별자 생성을 위한 카운터
post_id = 0


@router.post("")
def create_post(post_data: PostCreate):
    # post_data에는 제목, 내용이라는 필드만 들어가야 합니다.
    # basemodel을 통해 제목, 내용만 들어있도록 강제한다.
    global post_id
    post_id += 1

    post = Post(post_id, post_data.title, post_data.content)
    posts.append(post)
    return post


# 데이터베이스 대신 쓰는 리스트
db = [{"id": 1, "name": "아이폰", "price": 5555550}]


# 주의: 주소에 "/products"를 빼고 적어도 됩니다. 나중에 main에서 한 번에 붙여줄 거거든요!
@router.get("products")
def read_products():
    # 저장된 모든 게시글 반환
    return {"message": "A_site 상품 등록 성공"}
