from fastapi import APIRouter

from . import routers

router = APIRouter(prefix="/users")
router.include_router(routers.users.router)
router.include_router(routers.token_auth.router)
