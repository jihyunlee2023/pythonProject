# myapi/routes/__init__.py

from .auth import router as auth_router
from .main_page import router as main_page_router
from .politicians import router as politicians_router

__all__ = ["auth_router", "main_page_router", "politicians_router"]
