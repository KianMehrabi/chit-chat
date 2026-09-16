from .models import Room
from django import forms

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Room title",
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Room description",
            }),
        }
