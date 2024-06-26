from django import forms

from user import models as user_models


class NewDeveloperRequestForm(forms.ModelForm):
    requested_by = forms.ModelChoiceField(queryset=user_models.Customer.objects.all(), empty_label='--Nothing--')

    class Meta:
        model = user_models.Developer
        fields = ['specialization', 'grade', ]


class DeveloperForm(forms.Form):
    developer = forms.ModelChoiceField(queryset=user_models.Developer.objects.all(), empty_label='--Nothing--')
