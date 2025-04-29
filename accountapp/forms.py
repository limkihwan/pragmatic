from django import forms
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountUpdateForm(SetPasswordForm):
    username = forms.CharField(
        label="Username",
        disabled=True,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)  # user를 명시적으로 전달
        self.fields['username'].initial = user.username