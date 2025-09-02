from sqlalchemy import Column, Integer, String, DateTime
import datetime
from .database import Base


class Rom(Base):
    __tablename__ = "roms"


    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    system = Column(String, index=True, nullable=False)
    status = Column(String, default="missing") # missing | have | downloading
    hash = Column(String, unique=True, index=True, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)