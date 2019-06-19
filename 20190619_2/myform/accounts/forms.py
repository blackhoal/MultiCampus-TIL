from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class UserCustomChangeForm(UserChangeForm):
    class meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')