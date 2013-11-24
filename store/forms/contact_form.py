from django import forms
from django.core.validators import RegexValidator

class ContactForm(forms.Form):
    reply_email = forms.EmailField()
    reply_email.label = "Your Email*"
    reply_email.required = True
    phone = forms.RegexField(max_length=10, min_length=10, regex=r'[0-9]+', error_message = ("Please enter a valid phone number."))
    phone.label = "Your Phone"
    availability = forms.CharField(widget=forms.Textarea)
    availability.label = "Availability*"
    message = forms.CharField(widget=forms.Textarea)
    message.label = "Message*"

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
