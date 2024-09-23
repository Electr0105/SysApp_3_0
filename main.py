from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import hmac
import configparser

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
    # startdate: str

@app.get("/")
async def test():
    return {"welcome":"welcome"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "description": "This is a test item."}

@app.get("/licenses")
async def licenses():
    return {"count":10}

@app.post("/create-user")
async def create_user(request: Request, user: User, authorization: Optional[str] = Header(None)):
    # Check if the Authorization header is present

    print(env_file["KEYS"]["Jackson"])

    print(user.model_dump_json())
    client_digest = hmac.new(''.encode(), user.model_dump_json().encode(), 'sha512').hexdigest()
    print(f"Client Digest {client_digest}")

    # Optionally, print the full request body
    body = await request.json()  # Read the body as JSON
    print("Request Body:", body)

    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header is missing")

    # You could also check the actual value of the token here (e.g., compare to a known token)
    if authorization != "jackson":
        raise HTTPException(status_code=403, detail="Unauthorized")

    # Process the user data (e.g., save to database, perform actions)
    user_data = user.model_dump()

    return {
        "message": "User created successfully",
        "user_data": user_data,
        "authorization": authorization
    }