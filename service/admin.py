from django.contrib import admin
from service.models import Message, Log

# admin.site.register(Message)
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Настройки админки для рассылки.
    """
    list_display = ('theme', 'body', 'mailing_time', 'periodicity', 'status')

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('date_attempt', 'status', 'answer')

# Register your models here.
