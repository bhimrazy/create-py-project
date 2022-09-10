from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["api"]
)


@router.get("/")
async def api():
    """Returns data from api"""
    return {"message": "Welcome to API"}
