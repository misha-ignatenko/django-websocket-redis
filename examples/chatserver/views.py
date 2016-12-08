# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher
from . import models
import json
from django.core import serializers

from django.http import JsonResponse

def get_historic_chat_messages(request):
    print "INSIDE get_historic_chat_messages"
    all_chat_msgs = models.ChatMessage.objects.all()

    data = {
        "user": "current_user",
        "messages": json.loads(serializers.serialize('json', all_chat_msgs))
    }

    return JsonResponse(data)

class BroadcastChatView(TemplateView):
    template_name = 'broadcast_chat.html'

    def get(self, request, *args, **kwargs):
        # add msg to the database and then re-create that message in Redis

        new_msg_text = "Welcome"
        new_chat_msg = models.ChatMessage(msg_text= new_msg_text)
        print "gonna create this new chat msg BroadcastChatView GET:"
        print new_chat_msg
        new_chat_msg.save()


        welcome = RedisMessage(new_chat_msg.msg_text)  # create a welcome message to be sent to everybody
        RedisPublisher(facility='foobar', broadcast=True).publish_message(welcome)
        return super(BroadcastChatView, self).get(request, *args, **kwargs)


class UserChatView(TemplateView):
    template_name = 'user_chat.html'

    def get_context_data(self, **kwargs):
        context = super(UserChatView, self).get_context_data(**kwargs)
        context.update(users=User.objects.all())
        return context

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(UserChatView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        print "INSIDE UserChatView"
        redis_publisher = RedisPublisher(facility='foobar', users=[request.POST.get('user')])
        # add message to the database, get it back from the db, convert to Redis, and publish
        message = RedisMessage(request.POST.get('message'))
        redis_publisher.publish_message(message)
        return HttpResponse('OK')


class GroupChatView(TemplateView):
    template_name = 'group_chat.html'

    def get_context_data(self, **kwargs):
        context = super(GroupChatView, self).get_context_data(**kwargs)
        context.update(groups=Group.objects.all())
        print "get_context_data"
        print "get_context_data"
        print "get_context_data"
        print "get_context_data"
        for key in context:
            print key
            print context[key]

        return context

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        print "INSIDE GROUP CHAT DISPATCH"
        return super(GroupChatView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):

        print "INSIDE POST"
        print "INSIDE POST"
        print "INSIDE POST"
        print "INSIDE POST"

        redis_publisher = RedisPublisher(facility='foobar', groups=[request.POST.get('group')])

        new_msg_text = request.POST.get('message')
        new_chat_msg = models.ChatMessage(msg_text= new_msg_text)
        print "gonna create this new chat msg GroupChatView:"
        print new_chat_msg
        new_chat_msg.save()

        message = RedisMessage(new_chat_msg.msg_text)
        redis_publisher.publish_message(message)
        return HttpResponse('OK')
