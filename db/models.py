from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .database import Base


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, nullable=True)