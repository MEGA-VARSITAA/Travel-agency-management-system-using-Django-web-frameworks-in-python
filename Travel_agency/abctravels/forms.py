from .models import Bus, Ticket
from django import forms

class Ticket_form(forms.ModelForm):
    class Meta:
        model=Ticket
        fields="__all__"
