from django.apps import AppConfig


class LaxmiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Laxmi'

    def ready(self):  # method just to import the signals
        # everytime server restarts
        import Laxmi.signals