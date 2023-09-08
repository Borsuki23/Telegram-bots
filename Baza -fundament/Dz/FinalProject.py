import telebot
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot('5579061130:AAEiIBroucLkh0b6xarE52m81zH9XsyA_Hk')

user_state = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = telebot.types.KeyboardButton("Отримати оголошення!")
    markup.add(item)
    bot.send_message(message.chat.id, "Привіт! Я бот з оголошеннями ОЛХ натискай кнопку Отримати оголошення і ти побачиш на що я здатний)", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Отримати оголошення!")
def send_olx_info(message):
    user_id = message.chat.id

    session = requests.Session()
    answ = session.post('https://www.olx.ua')
    html = BeautifulSoup(answ.content, 'html.parser')
    plitki = html.find_all('li', attrs={'class': 'wrap'})

    if not plitki:
        bot.send_message(message.chat.id, "На жаль, оголошень не знайдено.")
        return
    plit = plitki[0]
    title = plit.find('img').get('alt')
    image_url = plit.find('img').get('src')
    price = plit.find('div', attrs={'class': 'price'}).text.strip() 
    location = plit.find('ul', attrs={'class': 'date-location'}).text.split('\n')[1]
    link = "https://www.olx.ua" + plit.find('a', attrs={'class': 'link'})['href']

    text = f"{title}\nЦіна: {price}\nМісце: {location}\nПосилання: {link}"
    bot.send_photo(message.chat.id, image_url, caption=text)

    user_state[user_id] = {'title': title, 'price': price, 'location': location, 'link': link}

bot.polling()







