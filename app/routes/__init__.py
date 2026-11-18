from fastapi import APIRouter

from app.routes.health import router as health_router
from app.routes.clientes import router_clientes

router = APIRouter()
router.include_router(health_router)
router.include_router(router_clientes)