import uvicorn, os
from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter

load_dotenv()

app = FastAPI()

router = APIRouter(prefix="/router")

@router.get("/test") 
def test():
    port = os.getenv('PORT')
    return {"message": f"this is from api {port}"}

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=os.getenv('PORT', 8000))