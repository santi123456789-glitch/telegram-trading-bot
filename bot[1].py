import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

TOKEN = "PEGÁ_ACÁ_TU_TOKEN"
bot = telebot.TeleBot(TOKEN)

monedas = ["EUR/USD", "BTC/USD", "USD/JPY"]

def generar_senal():
    return random.choice(["📈 BUY (Compra)", "📉 SELL (Venta)"])

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    for m in monedas:
        markup.add(InlineKeyboardButton(m, callback_data=m))
    bot.send_message(message.chat.id, "Elegí una moneda 👇", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    senal = generar_senal()
    bot.send_message(call.message.chat.id, f"📊 Señal para {call.data}:
{senal}")

bot.polling()
