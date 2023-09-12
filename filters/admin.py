from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsBotAdminFilter(BaseFilter):
    def __init__(self, user_id: Union[str, list]):
        self.user_id = user_id

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.user_id, str):
            return message.from_user.id == int(self.user_id)
        elif isinstance(self.user_id, list):
            return message.from_user.id in self.user_id
