from django.forms import ModelForm
from django.http import HttpResponseForbidden

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']
