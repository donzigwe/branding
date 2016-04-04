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


class LogoCompanyForm(forms.ModelForm):
    full_name =         forms.CharField()
    email =             forms.EmailField()
    phone_number =      forms.CharField()
    description =       forms.CharField(widget=forms.Textarea)
    old_logo =          forms.BooleanField()
    upload_old_logo =   forms.ImageField(required=False)
    reason_logo =       forms.CharField(widget=forms.Textarea)
    target_audience =   forms.CharField(widget=forms.Textarea)
    competition =       forms.BooleanField()
    desc_competition =  forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = LogoCompany
        fields = ('full_name', 'email', 'phone_number', 'description', 'old_logo',
                  'upload_old_logo', 'reason_logo', 'target_audience', 'competition',
                  'desc_competition')
    
    
    
class LogoProjectForm(forms.ModelForm):
    tagline =           forms.CharField()
    include_tagline =   forms.BooleanField()
    imagery =           forms.CharField(widget=forms.Textarea)
    my_brand_colour =   forms.BooleanField()
    brand_colours =     forms.CharField(widget=forms.Textarea)
    pref_colour =       forms.BooleanField()
    list_pref_colour =  forms.CharField(widget=forms.Textarea)
    logo_adjective =    forms.CharField()
    logo_message =      forms.CharField(widget=forms.Textarea)
    typography =        forms.CharField()
    logo_location =     forms.CharField()
    deadline =          forms.DateField()
    budget =            forms.CharField()
    other_services =    forms.CharField(widget=forms.Textarea)
    inspired_logos =    forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = LogoProject
        fields = ('tagline', 'include_tagline', 'imagery', 'my_brand_colour', 'brand_colours',
                  'pref_colour', 'list_pref_colour', 'logo_adjective', 'logo_message', 'typography',
                  'logo_location', 'deadline', 'budget', 'other_services', 'inspired_logos')
    