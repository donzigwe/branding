from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

  
class Contact(models.Model):
    name =          models.CharField(max_length=30)
    email =         models.EmailField()
    phone_regex =   RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Incorrect format, please enter your phone number correctly")
    phone_number =  models.CharField(validators=[phone_regex], blank=True, max_length=30)
    description =   models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return '%s %s' %(self.name, self.phone_number)
    
class LogoComapny(models.Model):
    full_name =         models.CharField(max_length=50)
    email =             models.EmailField()
    phone_number =      models.CharField(max_length=50)
    description =       models.TextField()
    old_logo =          models.BooleanField()
    upload_old_logo =   models.ImageField(upload_to="old_logo")
    reason_logo =       models.TextField()
    target_audience =   models.TextField()
    competition =       models.BooleanField()
    desc_competition =  models.TextField()
    
    def __init__(self):
        return '%s %s %s' %(self.full_name, self.phone_number)
    
class LogoProject(models.Model):
    tagline =           models.CharField(max_length=120)
    include_tagline =   models.BooleanField()
    imagery =           models.TextField()
    my_brand_colour =   models.BooleanField()
    brand_colours =     models.TextField()
    pref_colour =       models.BooleanField()
    list_pref_colour =  models.TextField()
    logo_adjective =    models.CharField(max_length=25)
    logo_message =      models.TextField()
    typography =        models.CharField(max_length=25)
    logo_location =     models.CharField(max_length=25)
    deadline =          models.DateField()
    budget =            models.CharField(max_length=50)
    other_services =    models.TextField()
    inspired_logos =    models.TextField()
    
    def __init__(self):
        return '%s %s %s %s %s' %(self.tagline, self.logo_adjective, self.typography,
                                  self.logo_location, self.budget)
    
    
    
    
    
