__author__ = 'phadke'

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
        url = self.__nameUrl__.format(Type=type, Name=name)
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

    # def ParseJsonAllBookLists(self, bookLists):
    #     """
    #     Parses JSON list of all book lists into list of BookList
    #     :param bookLists Json list of all book lists from NYT api
    #     :return: [BookList]
    #     """
    #     parsedBookLists = []
    #     for bookList in bookLists:
    #         listKey = bookList["list_name"].replace(' ', '-').lower()
    #         displayName = bookList["display_name"]
    #         parsedBookLists.append(BookList(ListKey=listKey,DisplayName=displayName))
    #     return parsedBookLists
    #
    # def BulkSaveBookLists(self, bookLists):
    #     for bookList in bookLists:
    #         try:
    #             BookList.objects.get_or_create(ListKey=bookList.ListKey,
    #                                            DisplayName=bookList.DisplayName)
    #         except Exception as e:
    #             print(e)
    #             raise e
    #
    # def GetAllBookLists(self):
    #     """
    #     Gets all BookLists from DB
    #     :return: [BookList]
    #     """
    #     return BookList.objects.all()
    #
    # def LoadBookListCache(self, allBookLists):
    #     for bookList in allBookLists:
    #         self.BookListCache[bookList.ListKey] = bookList.DisplayName
    #
    # def RefreshCache(self):
    #     jsonResults = self.GetJsonAllBookLists()
    #     parsedResults = self.ParseJsonAllBookLists(jsonResults)
    #     if parsedResults:
    #         self.BulkSaveBookLists(parsedResults)
    #     if parsedResults and not self.BookListCache:
    #         allBookLists = self.GetAllBookLists()
    #         self.LoadBookListCache(allBookLists)