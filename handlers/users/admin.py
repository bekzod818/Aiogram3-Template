import asyncio
import pandas as pd
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from loader import db, bot
from keyboards.inline.buttons import are_you_sure_markup
from states.test import AdminState

router = Router()


@router.message(Command('allusers'))
async def get_all_users(message: types.Message):
    users = await db.select_all_users()
    id = []
    name = []
    for user in users:
        id.append(user[-1])
        name.append(user[1])
    data = {
        "Telegram ID": id,
        "Name": name
    }
    pd.options.display.max_rows = 10000
    df = pd.DataFrame(data)
    if len(df) > 50:
        for x in range(0, len(df), 50):
            await bot.send_message(message.chat.id, df[x:x + 50])
    else:
        await bot.send_message(message.chat.id, df)


@router.message(Command('reklama'))
async def send_ad_to_users(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        user_id = user[-1]
        await bot.send_message(chat_id=user_id, text="@BekoDev va @chogirmali_blog kanallariga obuna bo'ling!")
        await asyncio.sleep(0.05)


@router.message(Command('cleandb'))
async def ask_are_you_sure(message: types.Message, state: FSMContext):
    msg = await message.reply("Haqiqatdan ham bazani tozalab yubormoqchimisiz?", reply_markup=are_you_sure_markup)
    await state.update_data(msg_id=msg.message_id)
    await state.set_state(AdminState.are_you_sure)


@router.callback_query(AdminState.are_you_sure)
async def clean_db(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg_id = data.get('msg_id')
    await bot.delete_message(chat_id=call.message.chat.id, message_id=msg_id)
    if call.data == 'yes':
        await db.delete_users()
        await call.message.answer('Baza tozalandi!')
    elif call.data == 'no':
        await call.message.answer("Baza tozalanmadi.")
    await state.finish()
