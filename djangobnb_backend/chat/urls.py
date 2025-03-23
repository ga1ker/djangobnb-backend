from django.urls import path

from . import api

urlpatterns = [
    path('', api.conversation_list, name='api_conversation_list'),
    path('<uuid:pk>/', api.conversation_detail, name='api_conversation_detail'),
]