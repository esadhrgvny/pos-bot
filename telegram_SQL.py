import telebot
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='epos'
)

api = '1654237983:AAF8eSpAQh6v5cv-lAAJjvdn2uRjjTYtzRU'
bot = telebot.TeleBot(api)

# cek database sudah bisa diakses apa belum
# print(mydb)
# memberi input ke SQL
sql = mydb.cursor()


@bot.message_handler(commands=['penjualan'])
def penjualan(message):
    # print(message)
    texts = message.text.split(' ')
    # parameter tanggal
    date = texts[1]
    print(texts)

    # ambil data transaksi dari table sale berdasarkan tanggal
    try:
        sql.execute(
            "SELECT invoice, customer_id, total_price, discount, final_price, cash, remaining, date from t_sale where date ='{}'".format(date))

        hasil_sql = sql.fetchall()
        pesan_balasan = ''

        for x in hasil_sql:
            print(x)
            pesan_balasan = pesan_balasan + str(x) + '\n'

            bot.reply_to(message, pesan_balasan)
    except:
        pesan_error = 'Tidak ada transaksi'
        bot.reply_to(message, pesan_error)


print('bot start running')
bot.polling()
