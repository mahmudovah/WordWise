from django.db.models.signals import post_save
from django.dispatch import receiver
from botapp.models import BotUser
from bot.loader import bot


@receiver(post_save, sender=BotUser)
def notify_about_new_botuser(sender, created, instance, **kwargs):
    if created:
        bot.send_message(
            chat_id="-1003875715863",
            #"-1003813831969"
            text=f'Yangi user yaratildi!\n'\
            f'Ism: {instance.full_name}\n'\
            f'Username: {instance.username}'
        )
    pass