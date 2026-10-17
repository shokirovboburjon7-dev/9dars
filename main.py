import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandStart
from aiogram.types import BotCommand

TOKEN = "TOKENINGizni_shu_YERGA_YOZING"
ADMIN_ID = 8984302315:AAEsFPi5pCOkeVTAT2hcY6cUCdSlnxH6ff4

dp = Dispatcher()

async def set_main_menu(bot: Bot):
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="help", description="Yordam olish"),
        BotCommand(command="about", description="Biz haqimizda"),
        BotCommand(command="settings", description="Sozlamalar"),
        BotCommand(command="contact", description="Bog'lanish")
    ]
    await bot.set_my_commands(commands)

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Assalomu alaykum!")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Yordam bo'limi.")

@dp.message(Command("about"))
async def cmd_about(message: types.Message):
    await message.answer("Biz haqimizda.")

@dp.message(Command("settings"))
async def cmd_settings(message: types.Message):
    await message.answer("Sozlamalar.")

@dp.message(Command("contact"))
async def cmd_contact(message: types.Message):
    await message.answer("Bog'lanish.")

@dp.message(F.text | F.photo | F.video | F.audio | F.contact | F.location)
async def handle_content(message: types.Message, bot: Bot):
    if message.from_user.id != ADMIN_ID:
        await bot.forward_message(
            chat_id=ADMIN_ID,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )
    await message.answer("Xabaringiz adminga yuborildi!")

async def main():
    bot = Bot(token=TOKEN)
    await set_main_menu(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
