from django.contrib import admin
from brandid.models import *

class LogoCompanyAdmin(admin.ModelAdmin):
    pass

class LogoProjectAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)
admin.site.register(LogoCompany, LogoCompanyAdmin)
admin.site.register(LogoProject, LogoProjectAdmin)