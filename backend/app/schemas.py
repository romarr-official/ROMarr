from pydantic import BaseModel
from typing import Optional


class RomBase(BaseModel):
    title: str
    system: str
    status: str = "missing"
    hash: Optional[str] = None


class RomCreate(RomBase):
    pass


class RomRead(RomBase):
    id: int


    class Config:
        from_attributes = True