from sqlalchemy import Column, VARCHAR, DateTime

from database.connect_mysql import Base

class Users(Base):
    __tablename__ = "users"

    cognite_id = Column(VARCHAR(length=255))
    name = Column(VARCHAR(length=255))
    email = Column(VARCHAR(length=255))
    affiliation = Column(VARCHAR(length=255))
    job_title = Column(VARCHAR(length=255))
    role = Column(VARCHAR(length=255))
    deleted_at = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)