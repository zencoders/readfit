from HTMLParser import HTMLParser

import urllib
import re

class Fetcher(HTMLParser):
	__url_list=[]

	def set_handling_function(self,func):
		self.__handling_function=func

	def get_url_list(self):
		return self.__url_list

	def handle_starttag(self,tag,attr):
		attr_dict=dict(attr)
		link=self.__handling_function(tag,attr_dict)
		if link != "":
			self.__url_list.append(link)

class Crawler:
	__fetcher=Fetcher()
	def __init__(self,url,fetch_func,max__depth=0,exclude=[],filters=[]):
		self.__url=url
		self.__exclude=exclude
		self.__filters=filters
		self.__url_to_visit=[url]
		self.__url_visited=[]
		self.__fetcher.set_handling_function(fetch_func)

	#This method has been added for a better 
	#readability and future improvements
	def __is_url_visited(self,url):
		return url in self.__url_visited

	def __is_filtered(self,url):
		#TODO implement filtering rules here
		return False
	#Check if the url is visitable, urls
	#are not visitable if already visited or must be filtered
	def __is_url_visitable(self,url):
		return (not self.__is_url_visited(url)) and (not self.__is_filtered(url))

	#Retrieve a given page by url
	def __get_html_file(self,url):
		try:
			connection=urllib.urlopen(url)
			response_page=connection.read()
		except:
			response_page=""
		return response_page

	def crawl(self):
		#TODO implement deep mining logic with depth
		while self.__url_to_visit!=[]:
			url=self.__url_to_visit.pop(0)
			if self.__is_url_visitable(url):
				page=self.__get_html_file(url)
				if page!="":
					self.__fetcher.feed(page)
					self.__fetcher.close()
					self.__fetcher.reset()
				self.__url_visited.append(url)


#The following code has been added for testing purposes

#The following function is an example of function to supply to Crawler class
#this function caracterize the fetching policy of the Crawler class
def reddit_fetch_function(tag,attr):
	if tag=="a":
		if 'href' in attr:
			if 'class' in attr:
				if re.search('title',attr['class']):
					print "link with class=\"title\":",attr['href']
					return attr['href']
	return ""

def main():
	reddit_crawler=Crawler("http://www.reddit.com/r/programming",reddit_fetch_function)
	reddit_crawler.crawl()

if __name__ == "__main__":
	main()
