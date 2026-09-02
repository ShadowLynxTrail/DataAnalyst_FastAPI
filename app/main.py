
from fastapi import FastAPI
from pydantic import EmailStr
import uvicorn

from app.api_routers.users import router as users_router
from app.api_routers.items import router as items_router
from app.api_routers.analytics import router as analytics_router

app = FastAPI(title = "My API", version = "0.1.0")

app.include_router(users_router, prefix="/users")
app.include_router(items_router, prefix="/items")
app.include_router(analytics_router, prefix="/analytics")



from app.database import engine, Base



Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"data": "message"}

@app.post('/user')
def creat_user(email: EmailStr):
    return {"message":"success",
            "email": email,}


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)



