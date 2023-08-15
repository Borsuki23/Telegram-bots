import logging
import random
import os
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5579061130:AAEiIBroucLkh0b6xarE52m81zH9XsyA_Hk'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

image_folder1 = r"C:\Users\Artur\Telegram bots\Baza -fundament\Dz\cosmos"
image_folder2 = r"C:\Users\Artur\Telegram bots\Baza -fundament\Dz\nature"
image_folder3 = r"C:\Users\Artur\Telegram bots\Baza -fundament\Dz\people"

def get_random_image(folder):
    images = os.listdir(folder)
    random_image = random.choice(images)
    return os.path.join(folder, random_image)

async def send_random_image(message, folder_name):
    image_path = get_random_image(folder_name)
    with open(image_path, 'rb') as photo:
        await message.reply_photo(photo)

@dp.message_handler(lambda message: 'космос' in message.text.lower() or
                    'космосом' in message.text.lower() or
                    'космосу' in message.text.lower())
async def send_cosmos_image(message: types.Message):
    await send_random_image(message, image_folder1)

@dp.message_handler(lambda message: 'природа' in message.text.lower() or
                    'прородою' in message.text.lower() or
                    'природи' in message.text.lower())
async def send_nature_image(message: types.Message):
    await send_random_image(message, image_folder2)

@dp.message_handler(lambda message: 'люди' in message.text.lower() or
                    'людьми' in message.text.lower() or
                    'людей' in message.text.lower())
async def send_people_image(message: types.Message):
    await send_random_image(message, image_folder3)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
























