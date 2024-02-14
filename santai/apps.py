from django.apps import AppConfig


class SantaiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'santai'

    def ready(self):
        import santai.signals