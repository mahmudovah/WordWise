from django.apps import AppConfig


class BotappConfig(AppConfig):
    name = 'botapp'

    def ready(self):
        from botapp import signals