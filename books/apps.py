from django.apps import AppConfig


class BooksConfig(AppConfig):
    name = 'books'





    def ready(self):
        # import signal handlers
        from . import  signals