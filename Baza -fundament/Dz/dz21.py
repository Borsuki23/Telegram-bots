import logging
import random
import os
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5579061130:AAEiIBroucLkh0b6xarE52m81zH9XsyA_Hk'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

answers = {
    "hi": r"C:\Users\Artur\Telegram bots\Baza -fundament\Dz\hi.txt",
    "hwru": r"C:\Users\Artur\Telegram bots\Baza -fundament\Dz\hwru.txt",
    "myname": r"C:\Users\Artur\Telegram bots\Baza -fundament\Dz\myname.txt",
    "old": r"C:\Users\Artur\Telegram bots\Baza -fundament\Dz\old.txt",
    "timing": r"C:\Users\Artur\Telegram bots\Baza -fundament\Dz\time.txt",
    "wether": r"C:\Users\Artur\Telegram bots\Baza -fundament\Dz\wether.txt"
}

def get_random_answer(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return random.choice(lines).strip()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привіт, я бот. Задавай мені питання!")

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def respond_to_question(message: types.Message):
    text = message.text.lower()

    if 'привіт' in text:
        answer = get_random_answer(answers['hi'])
    elif 'як справи' in text:
        answer = get_random_answer(answers['hwru'])
    elif 'погода' in text:
        answer = get_random_answer(answers['wether'])
    elif 'як тебе звати' in text:
        answer = get_random_answer(answers['myname'])
    elif 'скільки тобі днів' in text:
        answer = get_random_answer(answers['old'])
    elif 'котра година' in text:
        answer = get_random_answer(answers['timing'])
    else:
        answer = "Вибачаюсь, не зрозумів питання."
    
    await message.reply(answer)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)



