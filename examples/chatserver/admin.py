from django.contrib import admin
from chatserver.models import ChatMessage

class ChatMessageAdmin(admin.ModelAdmin):
    fields = ['msg_text']

admin.site.register(ChatMessage, ChatMessageAdmin)