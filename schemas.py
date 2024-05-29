from pydantic import BaseModel, EmailStr

class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str
    password_confirm: str

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    token: str

    class Config:
        orm_mode = True