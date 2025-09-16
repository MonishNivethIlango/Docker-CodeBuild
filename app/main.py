from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/fail")
def fail():
    raise HTTPException(status_code=400, detail="This endpoint always fails.")
