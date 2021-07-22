from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(required=True, label='Email:')
    subject = forms.CharField(max_length=200, required=True, label='Subject:')
    message = forms.CharField(widget=forms.Textarea(), max_length=400, required=True, label='Your Message:')
