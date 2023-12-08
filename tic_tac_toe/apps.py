from django.apps import AppConfig


class TicTacToeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tic_tac_toe'

    def ready(self):
        import tic_tac_toe.signals
