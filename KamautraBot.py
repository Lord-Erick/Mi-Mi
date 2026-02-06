import os
import random
import time
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ===============================
#   CONFIGURAÇÃO
# ===============================

TOKEN = "8007201060:AAG6_BJCrR-idxGNHzzVaaaCJcVJGLecSHQ"
bot = telebot.TeleBot(TOKEN)

# SUA LISTA DE FILE_ID
KamaRandom = [
    "AgACAgEAAxkBAAIJu2mGGDFT-yFi1gQylzT2bduMY1E6AALhrTEbp8RpRUCIrNllXcLcAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJummGGDERpeRKs2zxDaznTT-3LcWaAALgrTEbp8RpRS3b-fNe9uGqAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJvGmGGDE2ua0f9tfZ2NpeURtYtVx2AALirTEbp8RpReZjvYuyiNuZAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJvWmGGDH-homDH3ug4xGO2ST1Zk6_AALjrTEbp8RpRbsVN7Tu23sAAQEAAwIAA3gAAzgE",
    "AgACAgEAAxkBAAIJvmmGGDGvmywUtyTXr9TTmw6ny1XKAALkrTEbp8RpRUZiPc-vfSKlAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJv2mGGDHtxlQFJX9n0NU5S9wipmCRAALlrTEbp8RpRf2RHCPGXM6FAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJwGmGGDGIPOpNOqfOsQGQLL11Rs02AALmrTEbp8RpRdWn2eGGfw28AQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJwWmGGDE9JCBElcZmpeVoP0A1ECjPAALnrTEbp8RpRRdff7I_iW51AQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJwmmGGDFlC6-ys-tkQpxS9QaEnnp3AALorTEbp8RpRZ2faQ5katu3AQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJw2mGGDHIuOMinBg0xog2ZhF5OJ1oAAIkrjEbn3RpRTTyBpFWVCvkAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJxGmGGDF4gVdsOu4VWboZI16HjvUmAALprTEbp8RpRfH5GOXgnrvpAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJxWmGGDHecRY8rQqIwtmvTLrLaKCDAAIlrjEbn3RpRQAB887yYwb9LgEAAwIAA3gAAzgE",
    "AgACAgEAAxkBAAIJxmmGGDE_kUnKzQmH10wXBjcgRg2iAALqrTEbp8RpRYNI3OakBc2ZAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJx2mGGDGA--DjYfr0OCAIlT0bGS3kAALrrTEbp8RpRfKz5SOkAAGnugEAAwIAA3gAAzgE",
    "AgACAgEAAxkBAAIJyGmGGDEMq_Tu1Wc3KqsovSEH0S04AALsrTEbp8RpRSEe9dGzJaxVAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJyWmGGDGoj3BBtseWDAPcZq28d8aIAALtrTEbp8RpRTWoTZcMoJOVAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJymmGGDF0RoYNJvNufA4CcjYfN6SDAALurTEbp8RpRe5E9sfgES3eAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJy2mGGDE_s8pcfTqXKNH_SFxUIRhnAALvrTEbp8RpRYWk8ieDKBcvAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJzGmGGDGpLwthW_Plf41eBJ2BzB_5AALwrTEbp8RpRXEZ_QdOsHQ1AQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJzWmGGDG4QmLEy9UzA-hoJOLDSZaTAALxrTEbp8RpRRny3orwecSrAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJzmmGGDF3bIXCQRIVLO5Tdpf1rqkIAALyrTEbp8RpRXPlmhANxePMAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJz2mGGDG01z8LQXKLuAVY9Su5F84LAAImrjEbn3RpRVBM-c3n8ZqrAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJ0GmGGDHAjez0UfKkxKYjNI0odmG5AALzrTEbp8RpRWOkG4lzCpRJAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJ0WmGGDFuHcREL5T6CzShYYCTuAOHAAL0rTEbp8RpRSXXMIM2F2g3AQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJ0mmGGDE7ZqGAyNdw3ni9wW-bri9oAAL3rTEbp8RpRWglw7wBryLsAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJ02mGGDFCZ96csl3slOZnTsYpfx0KAALesTEbuk04RafEn8X5JNNyAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJ1GmGGDFHMdMpp6Lppcro6m-sn_ZKAALfsTEbuk04Relmzd3CUjLoAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJ1WmGGDFiqg3Vxqdn8zGzgwvxQDxNAALgsTEbuk04RXDPX2D7ZajAAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJ1mmGGDH0DeXJN43ZwW5DNc9HfORVAALhsTEbuk04RU-8ayUQUPMWAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJ12mGGDHDtcTBIxfVz7Ghv92TB5FdAALisTEbuk04RTZv2p1svbLDAQADAgADeAADOAQ",
    "AgACAgEAAxkBAAIJ2GmGGDGuk5ym8y0LjKRUEwABYD73QAAC47ExG7pNOEW7tdWuTmcwCQEAAwIAA3gAAzgE",
    "AgACAgEAAxkBAAIJ2WmGGDHIUerLiG2IYY9yAc1tMY_BAALksTEbuk04RZ0257QhlEM3AQADAgADeAADOAQ"
]

# Lista interna de desafios picantes
Desafios = [
    "😈 Quero ver você recriar essa posição… do seu jeitinho.",
    "🔥 Segure essa posição por 10 segundos… e me diga como se sentiu.",
    "💋 E se você tentasse deixar isso ainda mais picante?",
    "😏 Recrie essa energia agora… eu quero imaginar.",
    "👀 O que essa imagem te dá vontade de fazer?",
    "🫦 Me descreve em detalhes o que você faria agora…",
    "🍑 Essa deu calor… continua?",
    "🔞 Você faria isso comigo…?",
    "🔥 Tenta fazer igual e me conta se conseguiu.",
    "😈 Que nota você dá pra essa posição? E por quê?"
]

# ===============================
#   TECLADOS
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
#   FUNÇÕES
# ===============================

def sortear_imagem():
    return random.choice(KamaRandom)

def sortear_desafio():
    return random.choice(Desafios)

def super_sorteio_chance():
    return random.random() < 0.10  # 10%

# ===============================
#   HANDLERS
# ===============================

@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(
        msg.chat.id,
        "🔥 *Bem-vindo ao nosso joguinho privado…*\n\n"
        "Toque em um dos botões abaixo pra começar 😏",
        reply_markup=teclado_principal(),
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda c: True)
def callback(c):
    cid = c.message.chat.id

    if c.data == "sortear":
        file_id = sortear_imagem()

        if super_sorteio_chance():
            bot.send_message(cid, "💦 *Super Sorteio!* Você deu sorte…", parse_mode="Markdown")
            time.sleep(0.8)

        bot.send_photo(cid, file_id, caption="🔥 Gostou dessa? 😏")
        bot.send_message(cid, "Quer continuar?", reply_markup=teclado_principal())

    elif c.data == "desafio":
        file_id = sortear_imagem()
        desafio = sortear_desafio()

        bot.send_photo(cid, file_id, caption="😈 Preparado?")
        time.sleep(1)
        bot.send_message(cid, f"🔥 *Desafio:* {desafio}", parse_mode="Markdown")
        bot.send_message(cid, "E aí… topa continuar?", reply_markup=teclado_principal())

    elif c.data == "surpresa":
        bot.send_sticker(cid, "CAACAgIAAxkBAAEB9YtmGiaatZuJYppvR12BjRdt3AACTBoAAm2VmUnUOJ4EWMqx7jME")
        time.sleep(1)
        bot.send_message(cid, "😏 Hmmm… isso te deixou animado, né?")
        time.sleep(1)
        bot.send_message(cid, "Vamos continuar então…", reply_markup=teclado_principal())


@bot.message_handler(func=lambda m: True)
def bloquear_digitado(msg):
    bot.send_message(msg.chat.id, "😈 Só use os botões comigo…", reply_markup=teclado_principal())

# ===============================
#   RUN
# ===============================

bot.infinity_polling(timeout=60, long_polling_timeout=10)
