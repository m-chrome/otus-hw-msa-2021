from pydantic import BaseModel, EmailStr, constr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    username: constr(max_length=256)
    first_name: str = ""
    last_name: str = ""
    phone: str


class UserUpdate(UserBase):
    first_name: str = ""
    last_name: str = ""
    phone: str


class User(UserCreate):
    class Config:
        orm_mode = True
