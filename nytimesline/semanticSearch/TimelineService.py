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

	def ProcessQuery(query):
		print "Processing query: " + query
		print "Searching for similar content names..."
		search = __S__.SemanticSearch(query)
		print "Prioritizing content names..."
		print "Getting articles..."