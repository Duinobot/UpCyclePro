from django.apps import AppConfig


class PriceTableConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'price_table'

    def ready(self):
        import price_table.signals
