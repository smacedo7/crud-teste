from fastapi import FastAPI

from app.routes import router


app = FastAPI(title="CRUD API", version="0.1.0")
app.include_router(router)

@app.get('/')
def status():
    return {"status": "ok"}
