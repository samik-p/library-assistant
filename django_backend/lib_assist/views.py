from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .nlp.ai import *

# Create your views here.

# call this when a request is made to "/example"
@api_view(["POST"])
def respond(request):
    print("HELLOOOOOOOOOOO")
    print("USER: " + request.data["user_message"])

    data = request.data
    input_text = data["user_message"]
    
    examples = parse_file_for_examples("./lib_assist/nlp/examples.txt")

    # get response
    response = get_response(input_text, examples)
    print("RESPONSE: " + response)

    # make http response using make_response
    status_code = 200

    # http_response = make_response({"response": response}, status_code)
    return Response({"response": response}, status=status.HTTP_201_CREATED)