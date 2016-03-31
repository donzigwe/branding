from django.contrib import admin
from brandid.models import *

class LogoComapnyAdmin(admin.ModelAdmin):
    pass

class LogoProjectAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)
admin.site.register(LogoComapny, LogoComapnyAdmin)
admin.site.register(LogoProject, LogoProjectAdmin)