from fastapi import HTTPException, status
from mysite3.repositories.post_repository import post_repository
from mysite3.schemas.post import PostCreate, Post


class PostService:
    pass


post_service = PostService()


#####################################여기서는 Validation 체크를 하고, post_repository를 호출
class PostService:
    def create_post(self, data: PostCreate):
        # Validation
        if not data.title:
            raise HTTPException(
                status.HTTP_422_UNPROCESSABLE_CONTENT, "title을 입력하세요."
            )
        if not data.content:
            raise HTTPException(
                status.HTTP_422_UNPROCESSABLE_CONTENT, "content를 입력하세요."
            )

        new_post = Post(title=data.title, content=data.content)

        return post_repository.save(new_post)


############################################
def read_posts(self):
    return post_repository.find_all()
#############################################post_repository 호출
def read_post_by_id(self, id: int):
    post = post_repository.find_by_id(id)
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "없는 id입니다.")
    return post