import uvicorn, os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from fastapi import FastAPI, APIRouter
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/loadtest"

app = FastAPI()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    def _get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    return next(_get_db())

router = APIRouter(prefix="/router")

@router.get("/test") 
def test():
    port = os.getenv('PORT')
    return {"message": f"this is from api {port}"}

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=os.getenv('PORT', 8000))