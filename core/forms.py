from django import forms
from .models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Full Name", "class": "form-control"}
            ),
            "email": forms.TextInput(
                attrs={"placeholder": "Email", "class": "form-control"}
            ),
            "subject": forms.TextInput(
                attrs={"placeholder": "Subject", "class": "form-control"}
            ),
            "message": forms.Textarea(
                attrs={"placeholder": "Message...", "rows": 5, "class": "form-control"}
            ),
        }
