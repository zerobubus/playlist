from django import forms
import account.forms
from .models import Playlist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class PlaylistForm(forms.ModelForm):
    class Meta:

        model = Playlist
        fields = ["name", "track"]
        labels = {
            "name": "выберите название плейлиста",
            "track": "выберите треки"
        }
        widgets = {
            "track": forms.CheckboxSelectMultiple(),
            }


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):

        model = User
        fields = ("first_name", "last_name", "username", "email")


class SignupForm(account.forms.SignupForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["password_confirm"]
        self.fields["username"].label = "Имя"
