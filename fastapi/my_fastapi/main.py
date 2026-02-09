from fastapi import FastAPI

# from product.product_api import router
from product_adv.routers.product_router import router as product_router


app = FastAPI()

# app.include_router(router)
app.include_router(product_router)


@app.get("/")
def read_root():
    return {"Hello": "asd"}
