import logging
from typing import Any

from aiogram import Router
from aiogram.exceptions import (TelegramAPIError,
                                TelegramUnauthorizedError,
                                TelegramBadRequest,
                                TelegramNetworkError,
                                TelegramNotFound,
                                TelegramConflictError,
                                TelegramForbiddenError,
                                RestartingTelegram,
                                CallbackAnswerException,
                                TelegramEntityTooLarge,
                                TelegramRetryAfter,
                                TelegramMigrateToChat,
                                TelegramServerError)
from aiogram.handlers import ErrorHandler


router = Router()


@router.errors()
class MyErrorHandler(ErrorHandler):
    async def handle(self, ) -> Any:
        """
        Exceptions handler. Catches all exceptions within task factory tasks.
        :param dispatcher:
        :param update:
        :param exception:
        :return: stdout logging
        """
        if isinstance(self.exception_name, TelegramUnauthorizedError):
            """
            Bot tokeni yaroqsiz bo'lsa, xatolik uyushtiriladi.
            """
            logging.info(f'Unauthorized: {self.exception_message}')
            return True

        if isinstance(self.exception_name, TelegramNetworkError):
            """
            Telegram tarmog'idagi barcha xatoliklar uchun xatolik uyushtiriladi.
            """
            logging.exception(f'NetworkError: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramNotFound):
            """
            Suhbat, xabar, foydalanuvchi va boshqalar topilmasa, xatolik uyushtiriladi.
            """
            logging.exception(f'NotFound: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramConflictError):
            """
            Bot tokeni takroran ishlatilinayotganida xatolik uyushtiriladi.
            """
            logging.exception(f'ConflictError: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramForbiddenError):
            """
            Bot chatdan chiqarib yuborilishi kabi holatlarda xatolik uyushtiriladi.
            """
            logging.exception(f'ForbiddenError: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, CallbackAnswerException):
            """
            Javob qaytmasligi kabi holatlarda xatolik uyushtiriladi.
            """
            logging.exception(f'CallbackAnswerException: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramMigrateToChat):
            """
            Suhbat superguruhga ko'chirilganda xatolik uyushtiriladi.
            """
            logging.exception(f'BadRequest: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramServerError):
            """
            Telegram serveri 5xx xatosini qaytarsa, xatolik uyushtiriladi.
            """
            logging.exception(f'BadRequest: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramAPIError):
            """
            Barcha Telegram API xatoliklari uchun xatolik uyushtiriladi.
            """
            logging.exception(f'EntityTooLarge: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramRetryAfter):
            """
            So'rovlar ko'payib ketganda xatolik uyushtiriladi.
            """
            logging.exception(f'BadRequest: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramEntityTooLarge):
            """
            So'rov paytida ma'lumotlar limitdan oshganda xatolik uyushtiriladi.
            """
            logging.exception(f'EntityTooLarge: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, TelegramBadRequest):
            """
            So'rov noto'g'ri formatda bo'lganda xatolik uyushtiriladi.
            """
            logging.exception(f'BadRequest: {self.exception_message} \nUpdate: {self.update}')
            return True

        if isinstance(self.exception_name, RestartingTelegram):
            """
            Telegram serverini qayta ishga tushirishda xatolik uyushtiriladi.
            """
            logging.exception(f'RestartingTelegram: {self.exception_message} \nUpdate: {self.update}')
            return True

        logging.exception(f'Update: {self.update} \n{self.exception_name}')
