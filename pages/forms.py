from django import forms

from .models import StakeholderMessage


class StakeFolderMessageForm(forms.ModelForm):
    class Meta:
        model = StakeholderMessage
        exclude = [
            "id",
            "related_user",
            "user_is_anonymous",
        ]

    name = forms.CharField(label="Tu nombre", max_length=100)
    email = forms.EmailField(label="Tu correo electrónico")
    message = forms.CharField(label="Tu inquietud", widget=forms.Textarea)
