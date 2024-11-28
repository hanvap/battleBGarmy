from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'histproject.accounts'

    def ready(self ):
        import histproject.accounts.signals