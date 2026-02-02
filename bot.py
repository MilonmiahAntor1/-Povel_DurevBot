from aiogram import Bot, Dispatcher, executor, types
import os

BOT_TOKEN = os.getenv("8511833951:AAGlHDR8FiiPe-zLWUmfzqeoUAnQnixqucU")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("🤖 Bot is running on Railway!")

if __name__ == "__main__":
    executor.start_polling(dp)
