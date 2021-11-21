from sqlalchemy import Column, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, nullable=False)
    first_name = Column(String, default="")
    last_name = Column(String, default="")
    phone = Column(String, default="")
