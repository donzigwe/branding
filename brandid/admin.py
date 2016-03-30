from django.contrib import admin
from brandid.models import *

class TalkAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Talk, TalkAdmin)
admin.site.register(Contact, ContactAdmin)