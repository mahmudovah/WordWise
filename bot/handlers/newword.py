from bot.loader import bot
from telebot import types
from asosiy.models import Word, Subject

@bot.message_handler()
def newword_handler(message: types.Message):
    if message.text.startswith("/newword"):
        text = message.text
        text_data = text.split("\n")
        
        if len(text_data) < 4:
            bot.send_message(
                message.chat.id,
                "Noto'g'ri format ❌\n\n"
                "To'g'ri format quyidagicha:\n\n"
                "<code>/newword\nSubject nomi\nSo'z\nTarjimasi\nIzoh(ixtiyoriy)</code>",
                parse_mode="HTML"
            )
            return
        
        s = text_data[1]
        w = text_data[2]
        t = text_data[3]
        d = text_data[4] if len(text_data) > 4 else None

        try:
            subject = Subject.objects.get(title=s)
        except Subject.DoesNotExist:
            bot.send_message(message.chat.id, f"'{s}' nomli subject topilmadi!")
            return

        word = Word.objects.create(
            subject=subject,
            word=w,
            translated=t,
            definition=d
        )
        bot.send_message(message.chat.id, "So'z yaratildi! ✅")