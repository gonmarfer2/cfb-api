from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import main.messages as messages


# Create your views here.
def main(request):
    return render(request,"main.html",{})

@api_view(['POST'])
def receive_github(request):
    if request.method == "POST":
        type = request.headers["X-GitHub-Event"]
        data = request.data

        post_discord("github",type,data)
        return Response({},status=status.HTTP_200_OK)

def post_discord(type,subtype,data):
    try:
        webhook,msg = build_message(type,subtype,data)
        msg_json = {
            "method":"POST",
            "headers":{
                "content-type":"application/json"
            }
        }
        msg_json.update(msg)
        requests.post(webhook, json=msg_json)
    except messages.UnknownMessageError:
        pass

def build_message(type,subtype,data):
    if type == "github":
        return messages.github_messages(subtype,data)
    else:
        return "",dict()