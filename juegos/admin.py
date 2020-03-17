from django.contrib import admin
from .models import User,cate_Jueg,cate_serv,mega_juego,servi_juego
from django import forms
# Register your models here.

class mega_juego(admin.ModelAdmin):
    class Meta:
        model = Product
        widgets = {
            'tags': admin.widgets.AdminTextareaWidget
        }

admin.site.register(cate_Jueg)
admin.site.register(mega_juego)
