from django.contrib.auth.forms import UserCreationForm
from app1.models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=UserCreationForm.Meta.fields+('email','phone')