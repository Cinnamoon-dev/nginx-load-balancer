import uvicorn
from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter(prefix="/router")

@router.get("/test") 
def test():
    return {"message": "this is from api 3"}

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("api3:app", port=8002)