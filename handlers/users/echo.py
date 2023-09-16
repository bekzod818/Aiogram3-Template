from aiogram import Router, types

router = Router()


@router.message()
async def start_user(message: types.Message):
    await message.answer(message.text)
