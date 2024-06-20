from django import forms
from django.core.exceptions import ValidationError

from core.services.user import is_active_email


class LoginForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self) -> str:
        email = self.cleaned_data["email"]
        if not is_active_email(email):
            raise ValidationError("Your email does not exist in the system. Please ask your manager to add it.")
        return email
