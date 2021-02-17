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

    bot.reply_to(
        message, 'Hi {} \nKetikkan /help untuk melihat command '.format(first_name))


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
/penjualan -> Melihat data penjualan
/input -> Memasukkan data penjualan
/edit -> mengupdate data penjualan
/hapus -> Menghapus data penjualan
/penjualan_help -> Bantuan untuk melihat data penjualan
/input_help -> Bantuan untuk memasukkan data penjualan
/edit_help -> Bantuan untuk mengupdate data penjualan
/hapus_help -> Bantuan untuk menghapus data penjualan

    ''' .format(first_name, last_name))


@bot.message_handler(commands=['id'])
def send_welcome(message):
    nomor_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    bot.reply_to(message, '''
    Hi. Info Akun kamu:
ID = {}
Nama = {} {}
    '''.format(nomor_id, first_name, last_name))


@bot.message_handler(commands=['penjualan_help'])
def action_message(message):
    print(message)
    bot.reply_to(message, '''
    ketik /penjualan [tanggal] untuk melihat data penjualan pada tanggal tersebut.
    
Contoh: /penjualan 2021-01-18
    ''')


@bot.message_handler(commands=['input_help'])
def action_message(message):
    print(message)
    bot.reply_to(message, '''
    ketik /input [invoice] [id_customer] [total_harga] [discount] [harga_final] [cash] [kembalian] [tanggal]
    
Contoh: /input EP2102170002 4 20000 5000 15000 50000 35000 2021-01-18
    ''')


@bot.message_handler(commands=['edit_help'])
def action_message(message):
    print(message)
    bot.reply_to(message, '''
    ketik /edit [invoice yang akan diedit] [id_customer] [total_harga] [discount] [harga_final] [cash] [kembalian] [tanggal]
    
Contoh: /edit EP2102170002 4 20000 5000 15000 50000 35000 2021-01-18
    ''')


@bot.message_handler(commands=['hapus_help'])
def action_message(message):
    print(message)
    bot.reply_to(message, '''
    ketik /hapus [invoice yang akan dihapus] [id_customer] [total_harga] [discount] [harga_final] [cash] [kembalian] [tanggal]
    
Contoh: /hapus EP2102170002 4 20000 5000 15000 50000 35000 2021-01-18
    ''')


print('bot start running')
bot.polling()
