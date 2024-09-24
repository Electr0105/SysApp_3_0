from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import hmac
import configparser
from azure_api import get_number_of_available_licenses
import asyncio

app = FastAPI()
env_file = configparser.ConfigParser()
env_file.read('.env')
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow any HTTP method
    allow_headers=["*"],  # Allow any headers
)

class User(BaseModel):
    name: str
    manager: str
    state: str
    department: str
    # startdate: D

@app.get("/")
async def test():
    return {"welcome":"welcome"}

@app.get("/licenses")
async def licenses():
    num_of_licenses = await get_number_of_available_licenses()
    return {"availableLicenses": num_of_licenses}

@app.post("/create-user")
async def create_user(request: Request, user: User, authorization: Optional[str] = Header(None)):
    # Check if the Authorization header is present

    username, client_digest = authorization.split(":")

    try:
        user_key = env_file["API KEYS"][username]
    except:
        raise HTTPException(status_code=403, detail="Username not found")

    server_digest = hmac.new(user_key.encode(), user.model_dump_json().encode(), 'sha512').hexdigest()

    # Optionally, print the full request body
    body = await request.json()  # Read the body as JSON
    print("Request Body:", body)

    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header is missing")

    if client_digest != server_digest:
        raise HTTPException(status_code=403, detail="Unauthorized")

    # Process the user data (e.g., save to database, perform actions)
    user_data = user.model_dump()

    return {
        "message": "User created successfully",
        "user_data": user_data,
        "authorization": authorization
    }