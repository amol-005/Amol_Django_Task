from django.apps import AppConfig


class CustAuthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    # name = "cust_auth"
    name = __name__.rpartition('.')[0]
