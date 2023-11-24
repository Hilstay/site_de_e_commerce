from django.contrib.auth.forms import UserCreationForm
from ecom.settings import AUTH_USER_MODEL


class ConnextionForm(UserCreationForm):
    model = AUTH_USER_MODEL
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "password1",
        "password2"
    ]