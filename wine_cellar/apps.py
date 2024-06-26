from django.apps import AppConfig


class WineCellarConfig(AppConfig):
    """
    Configuration class for the Wine Cellar app.

    This class sets the default primary key field type and specifies the
    name of the app. It inherits from Django's AppConfig.

    Attributes:
        default_auto_field (str): Specifies the type of primary key to use
            for models in this app. \
            Defaults to 'django.db.models.BigAutoField'.
        name (str): The name of the app. Used by Django to identify the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wine_cellar'
