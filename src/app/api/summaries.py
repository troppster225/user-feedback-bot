from fastapi import APIRouter

router = APIRouter(prefix="/summaries", tags=["summaries"])

@router.get("/ping")
def ping():
    return{"ok": True, "message": "summaries router is alive"}