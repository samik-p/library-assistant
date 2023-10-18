from rest_framework import serializers
from .models import Ticket, Conversation, Message

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'resolved', 'title', 'summary', 'resolved_by')
        # extra_kwargs = {'sections': {'required': False}}

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('id', 'time_started')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sender', 'content', 'conversation', 'responding_to', 'time_sent', 'language')
