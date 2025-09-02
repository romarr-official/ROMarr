from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db, init_db
from .. import models, schemas


router = APIRouter(prefix="/roms", tags=["ROMs"])


@router.on_event("startup")
def on_startup():
    init_db()


@router.get("/", response_model=list[schemas.RomRead])
async def list_roms(db: Session = Depends(get_db)):
    return db.query(models.Rom).all()


@router.post("/", response_model=schemas.RomRead)
async def create_rom(payload: schemas.RomCreate, db: Session = Depends(get_db)):
    rom = models.Rom(**payload.dict())
    db.add(rom)
    db.commit()
    db.refresh(rom)
    return rom