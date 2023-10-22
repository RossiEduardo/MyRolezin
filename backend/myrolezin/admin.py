from django.contrib import admin
from .models import MyRolezin

class MyRolezinAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(MyRolezin, MyRolezinAdmin)