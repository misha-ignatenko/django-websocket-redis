# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

class ChatMessage(models.Model):
    msg_text = models.TextField(default="")


@receiver(pre_delete, sender=ChatMessage, dispatch_uid='chatmessage_delete_signal')
def log_deleted_chatmessage(sender, instance, using, **kwargs):
    print "RIGHT BEFORE DELETING CHAT MESSAGEEEE"
    print "RIGHT BEFORE DELETING CHAT MESSAGEEEE"
    print "RIGHT BEFORE DELETING CHAT MESSAGEEEE"
    print "RIGHT BEFORE DELETING CHAT MESSAGEEEE"
    print "RIGHT BEFORE DELETING CHAT MESSAGEEEE"
    print "RIGHT BEFORE DELETING CHAT MESSAGEEEE"
    print "RIGHT BEFORE DELETING CHAT MESSAGEEEE"
    print "RIGHT BEFORE DELETING CHAT MESSAGEEEE"
    print "RIGHT BEFORE DELETING CHAT MESSAGEEEE"