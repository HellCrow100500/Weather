import requests
from telegram.ext import Updater, CommandHandler

# Функция-обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот погоды. Введите команду /weather <город>, чтобы узнать текущую погоду.")

# Функция-обработчик команды /weather
def weather(update, context):
    if len(context.args) == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Пожалуйста, укажите город.")
        return

    city = ' '.join(context.args)
    api_key = '56b30cb255.3443075'  # Замените на ваш API-ключ погоды
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data['cod'] == '404':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Город не найден.")
        return

    temperature = data['main']['temp']
    weather_desc = data['weather'][0]['description']
    message = f"Текущая погода в {city}: {temperature}°C, {weather_desc}."

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Инициализация бота и добавление обработчиков команд
updater = Updater(token='6568139398:AAGJQnWWrYGZkgH-djue2F5PSmKjMJ_5yaY', use_context=True)  # Замените на токен вашего бота

start_handler = CommandHandler('start', start)
weather_handler = CommandHandler('weather', weather)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(weather_handler)

# Запуск бота
updater.start_polling()
