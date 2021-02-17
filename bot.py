# import PytelegramBotAPI
import telebot
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='epos'
)
# cek database sudah bisa diakses apa belum
# print(mydb)
# memberi input ke SQL
sql = mydb.cursor()

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


@bot.message_handler(commands=['penjualan'])
def penjualan(message):
    # print(message)
    texts = message.text.split(' ')
    # parameter tanggal
    date = texts[1]
    # ambil data transaksi dari table sale berdasarkan tanggal
    try:
        sql.execute(
            "SELECT invoice, customer_id, total_price, discount, final_price, cash, remaining, date from t_sale where date ='{}'".format(date))

        hasil_sql = sql.fetchall()
        pesan = []

        for x in hasil_sql:
            a = """Invoice : {0}\n
                id Customer : {1}\n
                Total Price : {2}\n
                Discount : {3}\n
                Final Price: {4}\n
                Cash: {5}\n
                Remaining: {6}\n
                Date: {7}\n""".format(
                x[0],
                x[1],
                x[2],
                x[3],
                x[4],
                x[5],
                x[6],
                x[7])
            pesan.append(a)

        spasi = " \n"
        pesan_balasan = spasi.join(pesan)
        bot.reply_to(message, pesan_balasan)

    except:
        pesan_balasan = 'Transaksi Tidak ada'
        bot.reply_to(message, pesan_balasan)


@bot.message_handler(commands=['input'])
def penjualan(message):
    # print(message)
    texts = message.text.split(' ')
    invoice = texts[1]
    customer_id = texts[2]
    Total_Price = texts[3]
    Discount = texts[4]
    Final_price = texts[5]
    Cash = texts[6]
    Remaining = texts[7]
    Date = texts[8]
    try:
        insert = 'insert into t_sale (invoice, customer_id, total_price, discount, final_price, cash, remaining, date) values ( %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (invoice, customer_id, Total_Price, Discount,
               Final_price, Cash, Remaining, Date)
        sql.execute(insert, val)
        mydb.commit()
        bot.reply_to(message, 'Data berhasil diinput')
        print(sql.rowcount, "Record added")
    except:
        pesan_balasan = 'Data yang dimasukkan salah'
        bot.reply_to(message, pesan_balasan)


@bot.message_handler(commands=['edit'])
def penjualan(message):
    # print(message)
    texts = message.text.split(' ')
    invoice = texts[1]
    customer_id = texts[2]
    Total_Price = texts[3]
    Discount = texts[4]
    Final_price = texts[5]
    Cash = texts[6]
    Remaining = texts[7]
    Date = texts[8]

    update = "UPDATE t_sale SET invoice = %s, customer_id = %s, total_price = %s, discount = %s, final_price = %s, cash = %s, remaining = %s, date = %s WHERE invoice = '{}'".format(
        invoice)
    val = (invoice, customer_id, Total_Price, Discount,
           Final_price, Cash, Remaining, Date)
    sql.execute(update, val)
    mydb.commit()
    bot.reply_to(message, 'Data berhasil diupdate')
    print(sql.rowcount, "Record(s) Updated")


@bot.message_handler(commands=['hapus'])
def penjualan(message):
    # print(message)
    texts = message.text.split(' ')
    invoice = texts[1]

    delete = "DELETE FROM t_sale WHERE invoice = '{}'".format(invoice)
    val = (invoice)
    sql.execute(delete, val)
    mydb.commit()
    bot.reply_to(message, 'Data berhasil dihapus')
    print(sql.rowcount, "Record(s) Deleted")


print('bot start running')
bot.polling()
