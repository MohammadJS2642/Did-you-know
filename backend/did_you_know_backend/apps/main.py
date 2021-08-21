from bs4 import BeautifulSoup as bs
import bs4
import requests
from requests.models import parse_header_links


class WebScraper:
    '''
        this class contains all functions 
        about web sraping 
    '''

    # __init__ is constructor
    # def __init__(self,url) -> None:
    #     self.url=url
    #     url = 'https://fa.wikipedia.org/wiki/%D8%B5%D9%81%D8%AD%D9%87%D9%94_%D8%A7%D8%B5%D9%84%DB%8C'

    url = 'https://fa.wikipedia.org/wiki/%D8%B5%D9%81%D8%AD%D9%87%D9%94_%D8%A7%D8%B5%D9%84%DB%8C'

    def createJSON(self):
        '''
            this function build a json data 
            from the received URL
        '''
        # create json data
        req = requests.get(self.url).content

        return req

    def workOnData(self):
        '''
        works on received json data
        from creatinJSON function
        '''

        # get web page data
        data = bs(self.createJSON())


r = WebScraper()
r.workOnData()
