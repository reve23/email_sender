from django import forms
from .models import Email_sender

class Email_senderForm(forms.ModelForm):
    class Meta:
        model = Email_sender
        fields = ["name","age","email","description"]