from mysite3.schemas.post import Post, PostCreate


class PostRepository:
    def __init__(self):
        self.posts = []
        self.post_id = 0


post_repository = PostRepository()


##########################################
class PostRepository:
    def __init__(self):
        self.posts = []
        self.post_id = 0

    def save(self, new_post: Post):
        self.post_id += 1
        new_post.id = self.post_id
        self.posts.append(new_post)
        return new_post


##########################################게시글 조회에 대한 로직을 담당
def find_all(self):
    return self.posts


#######################################게시글 수정 로직 담당
def modify(self, id: int, data: PostCreate):
    for post in self.posts:
        if post.id == id:
            post.title = data.title
            post.content = data.content
            return post
    return None
