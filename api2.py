import uvicorn
from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter(prefix="/router")

@router.get("/test") 
def test():
    return {"message": "this is from api 2"}

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("api2:app", port=8001)