from django import forms
from brandid.models import *

class TalkForm(forms.ModelForm):
    name =          forms.CharField()
    email =         forms.EmailField()
    phone_number =  forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                    error_message = (" No Wrong format, please enter your phone number correctly"),
                    )
        
    class Meta:
        model = Talk
        fields = ('name', 'email', 'phone_number')
    

class ContactForm(forms.ModelForm):
    name =          forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    email =         forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                                 error_message = ("Wrong format, please enter your phone number correctly"),
                    required=False, widget=forms.TextInput(attrs={'placeholder': 'Search'}),
                    )
    #phone_number =  forms.CharField()
    description =       forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Tell Us what you want'}))
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone_number', 'description')
    