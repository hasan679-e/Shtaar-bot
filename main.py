import os
import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("تحدي", callback_data="challenge"),
        InlineKeyboardButton("عدد النقاط", callback_data="points"),
        InlineKeyboardButton("تخصصي", callback_data="specialty")
    )
    await message.answer(f"أهلًا {message.from_user.first_name}! مرحبًا بك في بوت شطار للتحدي الدراسي.", reply_markup=keyboard)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
