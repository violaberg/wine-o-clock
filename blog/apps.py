from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration class for the 'blog' application.

    This class inherits from Django's AppConfig and is used to configure
    the 'blog' application. It sets the default type of primary key for
    models in this application to 'BigAutoField' and specifies the name
    of the application as 'blog'.

    Attributes:
        default_auto_field (str): \
        Specifies the default auto-incrementing primary key field type.
        name (str): The name of the application, \
        which should be unique within the project.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
