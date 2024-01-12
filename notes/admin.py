from django.contrib import admin
from . import models

# Register your models here.

class notesadmin(admin.ModelAdmin):
    list_display = ('text','notes','created',)


admin.site.register(models.notes,notesadmin)