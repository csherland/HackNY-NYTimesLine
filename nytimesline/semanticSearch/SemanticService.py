import json
import urllib2
import random
import datetime


class SemanticService:

    __articleUrl__ = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q={Query}&begin_date={Begin}&end_date={End}&api-key={ApiKey}"
    # __searchUrl__ = "http://api.nytimes.com/svc/semantic/v2/concept/search.json?query={Query}&api-key={ApiKey}"
    # __nameUrl__ = "http://api.nytimes.com/svc/semantic/v2/concept/name/{Type}/{Name}?fields=all&offset={Offset}&api-key={ApiKey}"
    __hdr__ = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    # _Type_ = {
    #     "location": "nytd_geo",
    #     "person": "nytd_per",
    #     "organization": "nytd_org",
    #     "descriptor": "nytd_des"
    # }

    # technically need two separate keys
    def __init__(self, key):
        self.__ApiKey__ = key


    def ArticleSearch(self, query, begin, end):
        results = []
        url = self.__articleUrl__.format(Query=query, Begin=begin, End=end, ApiKey=self.__ApiKey__)
        url = url.replace(' ','%20')
        # print url
        try:
            req = urllib2.Request(url, headers=self.__hdr__)
            jsonResponse = urllib2.urlopen(req)
            results = json.load(jsonResponse)["response"]
            return results
        except urllib2.URLError, e:
            print e.message
            return results


    def ArticlesByDate(self, query):
        num4yearSegments = 10
        base = datetime.date.today()
        dateList = [ base - datetime.timedelta(days=1461*x) for x in range(0,num4yearSegments+1) ]
        timeline = []

        for d in xrange(num4yearSegments):
            begin = dateList[d+1].strftime('%Y%m%d')
            end = dateList[d].strftime('%Y%m%d')
            results = self.ArticleSearch(query,begin,end)
            timeline.append({
                'begin': begin,
                'end': end,
                'hits': results["meta"]["hits"]
                })

        chronological = []
        for t in reversed(timeline):
            chronological.append(t)
        return chronological

    # def SemanticArticles(self, type, name, hitLimit):
    # def SemanticArticles(self, name, hitLimit):
    #     page = 0
    #     apiHits = 0
    #     # call SemanticName hitLimit or less number of times
    #     # results = self.SemanticName(type,name,offset)
    #     # articles = results["article_list"]["results"]
    #     # total = results["article_list"]["total"]

    #     # print articles

    #     results = self.ArticleSearch(name,page)
    #     print results
    #     articles = results["docs"]
    #     total = results["meta"]["hits"]

    #     apiHits = apiHits + 1
    #     remaining = total - len(articles)

    #     for k in range(1,min(hitLimit,remaining/10)):
    #         print k

    # def SemanticSearch(self, query):
    #     """
    #     Searches NYT Semantic API for content names
    #     related to the query term
    #     """
    #     results = []
    #     url = self.__searchUrl__.format(Query=query, ApiKey=self.__ApiKey__)
    #     url = url.replace(' ','%20')
    #     try:
    #         req = urllib2.Request(url, headers=self.__hdr__)
    #         jsonResponse = urllib2.urlopen(req)
    #         results = json.load(jsonResponse)["results"]
    #         return results
    #     except urllib2.URLError, e:
    #         print e.message
    #         return results
    # 
    # def SemanticName(self, type, name, offset):
    #     """
    #     Get content from NYT Semantic API for content name
    #     """
    #     results = []
    #     url = self.__nameUrl__.format(Type=type, Name=name, Offset=offset, ApiKey=self.__ApiKey__)
    #     url = url.replace(' ','%20')
    #     print url
    #     try:
    #         req = urllib2.Request(url, headers=self.__hdr__)
    #         jsonResponse = urllib2.urlopen(req)
    #         results = json.load(jsonResponse)["results"][0]
    #         return results
    #     except urllib2.URLError, e:
    #         print e.message
    #         return results
    #
    #
    # def ChooseName(self, searches):
    #     return searches[random.randint(0,len(searches)-1)]