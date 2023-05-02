from django.contrib import admin
from .models import Text

class TextAdmin(admin.ModelAdmin):
    list_display = ('text','url')

# Register your models here.
admin.site.register(Text,TextAdmin)