from bot.loader import bot
from telebot import types
from asosiy.models import Word
import random



def get_random_word():
    return Word.objects.order_by("?").first()


def get_options(word: Word, count=3):
    all_options = list(
        Word.objects.exclude(id=word.id)
        .values_list("translated", flat=True)
    )

    options = random.sample(all_options, count)
    options.append(word.translated)

    random.shuffle(options)

    return options


@bot.message_handler(commands=["quiz"])
def quiz_handler(message: types.Message):
    random_word = get_random_word()

    if not random_word:
        bot.send_message(message.from_user.id, "So‘zlar mavjud emas ❗")
        return
    
    if not random_word.translated:
        bot.send_message(message.from_user.id, "Tarjima mavjud emas ❗")
        return

    question = f"{random_word.word} tarjimasi?"

    options = get_options(random_word)

    correct_option_id = options.index(random_word.translated)

    bot.send_poll(
        message.chat.id,
        question,
        options,
        is_anonymous=False,
        correct_option_id=correct_option_id,
        type="quiz"
    )