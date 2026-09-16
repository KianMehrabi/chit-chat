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

class CodeForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Room code",
        })
    )


    def clean_code(self):
        code = str(self.cleaned_data.get("code"))
        room = Room.objects.filter(code = code)

        if  len(code) != 8:
            raise forms.ValidationError("not valid code")
        if not room.exists():
            raise forms.ValidationError("room tag is wrong or room didnt exist")

        return code

