from fastapi import FastAPI
from uuid import uuid4
from typing import List

from models import User,Gender,Role

app = FastAPI()

db: List[User] = [

    User(
        id = uuid4(),
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.male,
        roles=[Role.student]
    ),

    User(
        id = uuid4(),
        first_name="Alex",
        last_name= "Jones",
        gender= Gender.male,
        roles=[Role.admin, Role.user]
    )

]


@app.get("/")
async def root():

    return {"message": "Response from A First API"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;