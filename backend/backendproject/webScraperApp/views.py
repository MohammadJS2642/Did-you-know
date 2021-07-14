import json
from django import http
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from bs4 import BeautifulSoup
import environ

root = environ.Path(__file__)
env = environ.Env()
environ.Env.read_env()


# Create your views here.
def getter(request):
    url = env('url')
    req = requests.get(url).content
    soup = BeautifulSoup(req, 'html.parser')

    first_div = soup.find_all('div', attrs={'class': 'mw-parser-output'})
    second_div = soup.find_all('div', attrs={'id': 'mp-left'})
    thirth_div = soup.find_all('div', attrs={'id': 'mf-fp'})

    for div in first_div:
        Selected_article = div.find('div', {'id': 'mf-fa'})
        did_you_know = div.find_all('div', {'id': 'mf-con'})

        for inDiv in did_you_know:
            t = inDiv.find_all('div', {'style': 'padding: 0 0.5em;'})
            for nextDiv in t:
                ul = nextDiv.find_all('ul')
                for lst in ul:
                    li = lst.text

    for div in second_div:
        Monuments = div.find('div', {'id': 'mf-otd'})

    for div in thirth_div:
        Selected_image_today = div.find('div', {'class': 'center'})

    context = {
        'Selected_article': Selected_article,
        'did_you_know': did_you_know,
        'Monuments': Monuments,
        'Selected_image_today': Selected_image_today,
    }

    arr = [li]

    # return HttpResponse(req)
    return HttpResponse(arr)
    # return JsonResponse(arr)
