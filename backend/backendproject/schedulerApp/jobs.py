import requests
from bs4 import BeautifulSoup
import environ
from ModelsDB.models import DidYouKnow


root = environ.Path(__file__)
env = environ.Env()
environ.Env.read_env()


# Create your views here.
def getter():
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
                    li = [lst.text]

                    for l in li:
                        mylst = l.split('\n')
                        # for m in mylst:
                        #     myContext = m

    for div in second_div:
        Monuments = div.find('div', {'id': 'mf-otd'})

    for div in thirth_div:
        Selected_image_today = div.find('div', {'class': 'center'})

    did_you_know = DidYouKnow()
    did_you_know.text = mylst
    did_you_know.save()
