from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

class Talk(models.Model):
    name =          models.CharField(max_length=30)
    email =         models.EmailField()
    phone_regex =   RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Incorrect format, please enter your phone number correctly")
    phone_number =  models.IntegerField(validators=[phone_regex], blank=True, max_length=30)
    
    def __unicode__(self):
        return '%s' %(self.name)
    
        
class Contact(models.Model):
    name =          models.CharField(max_length=30)
    email =         models.EmailField()
    phone_regex =   RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Incorrect format, please enter your phone number correctly")
    phone_number =  models.CharField(validators=[phone_regex], blank=True, max_length=30)
    description =   models.TextField()
    
    def __unicode__(self):
        return '%s %s' %(self.name, self.phone_number)
