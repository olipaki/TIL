from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/00100")
def read_root():
    return {"안녕 하시오"}


@app.get("/hello")
def hello():
    return "Hello World!"


@app.get("/hi")
def hi():
    return ["Hello", "World", "!!"]
