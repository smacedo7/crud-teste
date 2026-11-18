from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
def health() -> dict[str, str]:
    """Confirma que a API está respondendo; não verifica o banco."""
    return {"status": "ok"}
