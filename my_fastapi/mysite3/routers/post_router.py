from fastapi import APIRouter

##################################
from fastapi import status
from mysite3.services.post_service import post_service
from mysite3.schemas.post import PostCreate, PostDetailResponse

########################################################
from mysite3.schemas.post import PostCreate, PostDetailResponse, PostListResponse

router = APIRouter(prefix="/posts-mvc")


#############################################post_service를 호출
@router.post("", response_model=PostDetailResponse, status_code=status.HTTP_201_CREATED)
def create_post(data: PostCreate):
    return post_service.create_post(data)


################################################3
@router.get("", response_model=list[PostListResponse])
def read_posts():
    return post_service.read_posts()
##################################################post_service를 호출
@router.get("/{id}", response_model=PostDetailResponse)
def read_post(id: int):
    return post_service.read_post_by_id(id)