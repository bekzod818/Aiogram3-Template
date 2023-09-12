from aiogram import Router

from filters import ChatPrivateFilter, IsBotAdminFilter

from data.config import ADMINS


def setup_routers() -> Router:
    from .users import admin, start, help, echo
    from .errors import error_handler

    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating
    # start.router.message.filter(ChatPrivateFilter(chat_type=["private"]))
    # admin.router.message.filter(IsBotAdminFilter(user_id=ADMINS))

    router.include_routers(admin.router, start.router, help.router, echo.router, error_handler.router)

    return router
