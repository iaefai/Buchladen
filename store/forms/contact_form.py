from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    name.label = "From"
    email = forms.EmailField()
    email.label = "From Email"
    email.required = True
    message = forms.CharField(widget=forms.Textarea)
    message.label = "Message"

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
