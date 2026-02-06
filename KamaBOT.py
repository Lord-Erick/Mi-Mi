import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request

# ===============================
# CONFIGURAÇÃO
# ===============================

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Render vai ler daqui
bot = telebot.TeleBot(TOKEN)

WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # URL que você vai colocar no Render

app = Flask(__name__)

# ===============================
# SUAS IMAGENS
# ===============================

KamaRandom = [
    "AgACAgEAAxkBAAIJu2mGGDFT-yFi1gQylzT2bduMY1E6AALhrTEbp8RpRUCIrNllXcLcAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJummGGDERpeRKs2zxDaznTT-3LcWaAALgrTEbp8RpRS3b-fNe9uGqAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJvGmGGDE2ua0f9tfZ2NpeURtYtVx2AALirTEbp8RpReZjvYuyiNuZAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJvWmGGDH-homDH3ug4xGO2ST1Zk6_AALjrTEbp8RpRbsVN7Tu23sAAQEAAwIAA3gAAzgE",
    ...
]

Desafios = [
    "😈 Quero ver você recriar essa posição…",
    "🔥 Segure essa posição por 10 segundos…",
    "💋 E se você tentasse deixar isso mais picante?",
    "😏 Recrie essa energia agora…",
]

# ===============================
# TECLADOS
# ===============================

def teclado_principal():
    k = InlineKeyboardMarkup()
    k.row(
        InlineKeyboardButton("🔥 Quero mais", callback_data="sortear"),
        InlineKeyboardButton("😈 Desafio", callback_data="desafio")
    )
    k.row(
        InlineKeyboardButton("💦 Surpresa", callback_data="surpresa")
    )
    return k

# ===============================
# FUNÇÕES INTERNAS
# ===============================

def rand_img():
    import random
    return random.choice(KamaRandom)

def rand_desafio():
    import random
    return random.choice(Desafios)

# ===============================
# BOT HANDLERS
# ===============================

@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(
        msg.chat.id,
        "🔥 *Bem-vindo ao joguinho privado...*\nToque nos botões 😏",
        reply_markup=teclado_principal(),
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda c: True)
def callback(c):
    cid = c.message.chat.id

    if c.data == "sortear":
        bot.send_photo(cid, rand_img(), caption="🔥 Gostou dessa?")
        bot.send_message(cid, "Quer continuar?", reply_markup=teclado_principal())

    elif c.data == "desafio":
        bot.send_photo(cid, rand_img(), caption="😈 Preparado?")
        bot.send_message(cid, f"🔥 *Desafio:* {rand_desafio()}", parse_mode="Markdown",
                         reply_markup=teclado_principal())

    elif c.data == "surpresa":
        bot.send_message(cid, "💦 Hmm… que calor…")
        bot.send_message(cid, "Vamos continuar?", reply_markup=teclado_principal())

@bot.message_handler(func=lambda m: True)
def bloquear_digitado(msg):
    bot.send_message(msg.chat.id, "😏 Só use os botões comigo...", reply_markup=teclado_principal())


# ===============================
# FLASK – RECEPTOR DO WEBHOOK
# ===============================

@app.route("/", methods=["POST"])
def webhook():
    update = request.get_data().decode("utf-8")
    bot.process_new_updates([telebot.types.Update.de_json(update)])
    return "OK", 200

# ===============================
# SET WEBHOOK
# ===============================

@app.route("/setwebhook", methods=["GET"])
def set_webhook():
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    return f"Webhook configurado em {WEBHOOK_URL}"

# ===============================
# RUN (Render inicia aqui)
# ===============================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))