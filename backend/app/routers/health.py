from fastapi import APIRouter


router = APIRouter(tags=["Health"])


@router.get("/health")
async def health():
    return {"ok": True}