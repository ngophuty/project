from sqlalchemy import Column, Integer, String, DateTime

from database.connect_mysql import Base

class Users(Base):
    __tablename__ = "users"

    cognite_id = Column(String(length=255))
    name = Column(String(length=255))
    email = Column(String(length=255))
    affiliation = Column(String(length=255))
    job_title = Column(String(length=255))
    role = Column(String(length=255))
    deleted_at = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
