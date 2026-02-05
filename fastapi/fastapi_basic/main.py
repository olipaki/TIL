from fastapi import FastAPI
from mysite2.post_api import router as pydantic_router
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# app = FastAPI()
# app.include_router(posr_router)
app.include_router(pydantic_router)
