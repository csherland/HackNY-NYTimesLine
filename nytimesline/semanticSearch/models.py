from django.db import models
import json
import urllib2


class SemanticService:
    __searchUrl__ = "http://api.nytimes.com/svc/semantic/v2/concept/search.json?query={Query}&api-key={Api-key}"
    __nameUrl__ = "http://api.nytimes.com/svc/semantic/v2/concept/name/{Type}/{Name}?fields=all&api-key={Api-key}"
    _Type_ = {
        "location": "nytd_geo",
        "person": "nytd_per",
        "organization": "nytd_org",
        "descriptor": "nytd_des"
    }

    def __init__(self, key):
        self.__key__ = key

    def SemanticSearch(self, query):
        """
        Fetches all booklists from NYT api
        :return: JSON results
        """
        results = []
        url = self.__searchUrl__.format(Query=query, ApiKey=self.__key__)
        try:
            hdr = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            }
            req = urllib2.Request(url, headers=hdr)
            jsonResponse = urllib2.urlopen(req)
            results = json.load(jsonResponse)["results"]
            return results
        except urllib2.URLError, e:
            print e.message
            return results

    def SemanticName(self, type, name):
        """
        Fetches all booklists from NYT api
        :return: JSON results
        """
        results = []
        url = self.__nameUrl__.format(Type=type, Name=name, ApiKey=self.__key__)
        try:
            hdr = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            }
            req = urllib2.Request(url, headers=hdr)
            jsonResponse = urllib2.urlopen(req)
            results = json.load(jsonResponse)["results"]
            return results
        except urllib2.URLError, e:
            print e.message
            return results
