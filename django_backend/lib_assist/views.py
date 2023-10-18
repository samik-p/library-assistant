from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.utils import timezone

from .nlp.ai import *
from .models import Conversation, Message
from langdetect import detect
from .serializers import MessageSerializer

# Create your views here.

# call this when a request is made to "/api/chat/<conversation_pk>"
@api_view(["POST"])
def respond(request):
    """This is called when a request is made to "/api/chat/<conversation_pk>"
    
    Args:
        request (json): __description__
        pk (__type__): primary key
        
    Returns:
        Response: __description__
    """
    print("=====================================")
    print("USER: " + request.data["user_message"])

    data = request.data
    input_text = data["user_message"]
    
    # detect language of input text
    language = detect(input_text)
    
    # get conversation, and then last message of that conversation
    conversation = Conversation.objects.get(pk=request.data["pk"])
    last_message_pk = conversation.last_message_id
    # print(last_message_pk)
    last_message = Message.objects.get(pk=last_message_pk)
    # print(last_message)
    # print(last_message.pk)
    
    # create a new message to add to Message table
    new_message_json = {
        "sender": "user",
        "content": input_text,
        "conversation": conversation.pk,
        "responding_to": last_message.pk,
        "time_sent": timezone.now(),
        "language": language,
    }

    # serialize and save the new message
    new_message = MessageSerializer(data=new_message_json)
    if new_message.is_valid():
        new_message.save()

        # TODO: update the "last_message_id" of the conversation to be the new message's id
    else:
        print(f"===views.py: new_mesage.is_valid() is False===")
        print(f"content:\t{input_text}")
        print(f"conversation (pk):\t{conversation.pk}")
        print(f"responding_to (pk):\t{last_message.pk}")
        print(f"time_sent:\t{timezone.now()}")
        print(f"language:\t{language}")
    
    examples = parse_file_for_examples("./lib_assist/nlp/examples.txt")

    # get response
    response = get_response(input_text, examples)
    print("RESPONSE: " + response)

    # make http response using make_response
    status_code = 200

    # http_response = make_response({"response": response}, status_code)
    return Response({"response": response}, status=status.HTTP_201_CREATED)