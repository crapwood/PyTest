from django.contrib import admin
from .models import Bot


# Register your models here.
# class BotAdmin(admin.ModelAdmin):
#     list_display = ['name', 'display_name', 'provider', 'credentials']


admin.site.register(Bot)
