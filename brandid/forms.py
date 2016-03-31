from django import forms
from brandid.models import *

class ContactForm(forms.ModelForm):
    name =          forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    email =         forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                    required=False, widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    #phone_number =  forms.CharField()
    description =       forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Tell Us what you want'}))
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone_number', 'description')
    