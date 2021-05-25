from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from django.template.response import TemplateResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import requests
import json

# Create your views here.

class AnimeQuotesApi(APIView):

    def get(self, request):
        response = requests.get("https://animechan.vercel.app/api/random")
        if response.status_code != 200:
            return Response({
                "code": "problem_during_petition",
                "detailed": "problema durante petición",
                "data": f"{response.status_code} - {response.text}"
            },status=status.HTTP_502_BAD_GATEWAY)
        quote = response.json()["quote"]
        owner = response.json()["character"]
        return Response({"quote": quote, "character": owner},status=status.HTTP_200_OK)

class AnimeImagesAPi(APIView):

    def get(self, request):
        response = requests.get("https://api.waifu.pics/sfw/waifu")
        if response.status_code != 200:
            return Response({
                "code": "problem_during_petition",
                "detailed": "problema durante petición",
                "data": f"{response.status_code} - {response.text}"
            },status=status.HTTP_502_BAD_GATEWAY)
        url = response.json()["url"]
        pepe = requests.get(url)
        return HttpResponse(pepe.content, content_type="image/png")

def main(request):
    response_quote = requests.get("https://animechan.vercel.app/api/random")
    if response_quote.status_code != 200:
        html = f"<html><body>quote {response_quote.status_code} - {response_quote.text}</body></html>"
        return HttpResponse(html)
    quote = response_quote.json()["quote"]
    owner = response_quote.json()["character"]

    response_waifu = requests.get("https://api.waifu.pics/sfw/waifu")
    if response_waifu.status_code != 200:
        html = f"<html><body>quote español{response_waifu.status_code} - {response_waifu.text}</body></html>"
        return HttpResponse(html)

    url = response_waifu.json()["url"]

    html = settings.BASE_DIR + "/templates/index.html"
    content = {
        "data_1": quote,
        "data_2": f"-{owner}",
        "url": url,
        "title": "Frases de anime que el personaje nunca dijo"
    }
    return TemplateResponse(request, html, context=content)

def nsfw(request, fun):
    if fun == 69:
        response_waifu = requests.get("https://api.waifu.pics/nsfw/waifu")
    else:
        response_waifu = requests.get("https://api.waifu.pics/sfw/cringe")
    if response_waifu.status_code != 200:
        html = f"<html><body>quote español{response_waifu.status_code} - {response_waifu.text}</body></html>"
        return HttpResponse(html)

    url = response_waifu.json()["url"]

    html = settings.BASE_DIR + "/templates/index.html"
    content = {
        "data_1": ("Never gonna give you up, never gonna let you down, "
            "Never gonna run around and desert you, "
            "Never gonna make you cry, "
            "Never gonna say goodbye, "
            "Never gonna tell a lie and hurt you"),
        "data_2": "-Rick Astley",
        "url": url,
        "title": "Solo te metiste por la imagen, a mi no me mientas"
    }
    return TemplateResponse(request, html, context=content)