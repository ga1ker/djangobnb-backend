from django.http import JsonResponse

from rest_framework.decorators import api_view

from .models import Conversation
from .serializers import ConversationDetailSerializer, ConversationListSerializer, ConversationMessageSerializer

@api_view(['GET'])
def conversation_list(request):
    serializer = ConversationListSerializer(Conversation.objects.all(), many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def conversation_detail(request, pk):
    conversation = request.user.conversations.get(pk=pk)

    conversation_serializer = ConversationDetailSerializer(conversation, many=False)
    message_serializer = ConversationMessageSerializer(conversation.messages.all(), many=True)

    return JsonResponse({
        'conversation': conversation_serializer.data,
        'messages': message_serializer.data
    }, safe=False)