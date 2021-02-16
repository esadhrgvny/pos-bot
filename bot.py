# import PytelegramBotAPI
import telebot

api = '1654237983:AAF8eSpAQh6v5cv-lAAJjvdn2uRjjTYtzRU'
bot = telebot.TeleBot(api)


@bot.message_handler(commands=['start'])
def action_start(message):
    print(message)
    # print(message.chat.id)
    # print(message.from_user.id)

    first_name = message.from_user.first_name

    bot.reply_to(message, 'Hi {}'.format(first_name))


@bot.message_handler(commands=['help'])
def send_welcome(message):
    nomor_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    bot.reply_to(message, '''
    Hi {} {}, Ini list command nya :
    /start -> Menyapa Bot
    /id -> Check id kamu
    /help -> List Command Bot
    ''' .format(first_name, last_name))


@bot.message_handler(commands=['id'])
def send_welcome(message):
    nomor_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    bot.reply_to(message, '''
    Hi. Akun kamu
    ID = {}
    Nama = {} {}
    '''.format(nomor_id, first_name, last_name))


print('bot start running')
bot.polling()
