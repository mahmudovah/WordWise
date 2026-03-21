from bot.loader import bot
from telebot import types


@bot.message_handler()
def newword_handler(message: types.Message):
   if message.text.startswith("/newword"):
        text = message.text
        text_data = text.split("\n")
        if len(text_data) < 3:
            bot.send_message(message.chat.id, "Noto'g'ri format\n" \
            "To'g'ri format quyidagicha:\n" \
            "<code>So'z\nTarjimasi\nIzoh</code>", parse_mode="HTML")
            return
        w = text_data[1]
        t = text_data[2]
        if len(text_data) > 3:
            d = "".join(text_data[3:])
        else:
            d = ""
        word = Word.objects.create(
            word=w,
            translated=t,
            definition=d
        )
        bot.send_message(message.from_user.id, "So'z yaratildi!")