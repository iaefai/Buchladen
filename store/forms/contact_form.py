from django import forms

class ContactForm(forms.Form):
    message = forms.CharField()
    message.label = "Message"
    reply_email = forms.EmailField()
    reply_email.label = "Your Email"
    reply_email.required = True