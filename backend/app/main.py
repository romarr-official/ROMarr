from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import health, roms
from .database import init_db  # <-- add this

app = FastAPI(title="ROMarr API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Run DB init on startup
@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(health.router)
app.include_router(roms.router)

@app.get("/")
async def root():
    return {"status": "ROMarr backend running"}
