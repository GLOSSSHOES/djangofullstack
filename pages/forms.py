from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Tu nombre", max_length=100)
    email = forms.EmailField(label="Tu correo electrónico")
    message = forms.CharField(label="Tu inquietud", widget=forms.Textarea)