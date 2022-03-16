from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message_body = f"Nome: {name}\nE-mail: {email}\n{message}"
        subject = "CK Estofados"
        sender = settings.DEFAULT_FROM_EMAIL
        recipient = settings.DEFAULT_FROM_EMAIL
        send_mail(subject, message_body, sender, [recipient])
