# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns, include
from django.core.urlresolvers import reverse_lazy
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from django.contrib import admin
from .views import BroadcastChatView, UserChatView, GroupChatView, get_historic_chat_messages
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^chat/$', BroadcastChatView.as_view(), name='broadcast_chat'),
    url(r'^userchat/$', UserChatView.as_view(), name='user_chat'),
    url(r'^get_historic_chat_messages/$', get_historic_chat_messages, name='get_historic_chat_messages'),
    url(r'^groupchat/$', GroupChatView.as_view(), name='group_chat'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('broadcast_chat'))),
) + staticfiles_urlpatterns()
