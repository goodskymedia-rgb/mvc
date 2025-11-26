from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {}

@app.put("/")
def root():
    return {}

@app.delete("/")
def root():
    return {}

@app.post("/")
def root():
    return {}
