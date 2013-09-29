import os
import json
from SemanticService import SemanticService as S

class TimelineService:

	def __init__(self):
		cd = os.path.dirname(os.path.abspath(__file__))
		nd = os.path.dirname('../nyt.keys')
		fn = os.path.join(cd,nd)
		fn = os.path.join(fn, 'nyt.keys')
		with open(fn) as f:
			self.__ApiKey__ = json.load(f)['key']
		if not self.__ApiKey__:
			raise('Api Key Error')
		else:
			self.__S__ = S(self.__ApiKey__)

	def ProcessQuery(self, query):
		print "Processing query: " + query
		# print "Searching for similar content names..."
		# searches = self.__S__.SemanticSearch(query)
		# print searches
		# print "Prioritizing content names..."
		# concept = self.__S__.ChooseName(searches)
		# print concept
		# print "Getting articles for concept: " + concept[u'concept_name']
		# articles = self.__S__.SemanticArticles(concept[u'concept_type'], concept[u'concept_name'], 10)
		timeline = self.__S__.ArticlesByDate(query)
		print timeline