from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import main.messages as messages
from django.conf import settings


# Create your views here.
def main(request):
    return render(request,"main.html",{})

@api_view(['POST'])
def receive_github(request):
    if request.method == "POST":
        type = request.headers["X-GitHub-Event"]
        data = request.data["payload"][0]

        post_discord_github(type,data)
        return Response({},status=status.HTTP_200_OK)

def post_discord_github(type,data):
    try:
        webhook,msg = build_message(type,data)
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

def build_message(type,data):
    return messages.github_messages(type,data)

@api_view(['POST'])
def receive_codacy(request):
    if request.method == "POST":
        print("="*90)
        print(request.data)

        post_discord_codacy(request.data)
        return Response({},status=status.HTTP_200_OK)

def post_discord_codacy(data):
    webhook = settings.WEBHOOK_CODACY
    msg = messages.build_codacy_msg(data)
    requests.post(webhook, json=msg)
