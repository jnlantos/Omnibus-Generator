from bs4 import BeautifulSoup
import urllib.request

URL = "http://www.philosophy.utoronto.ca/events/"

def request_page (url):
	"""Return a handle to the web page at the url url"""
	try:
		response = urllib.request.urlopen(url)
		#print(response.info())
		return response
	except URLError:
		print("Unable to open " + url + ".")
		pass

def make_soup (doc):
	"""Return a bs4 object representing the doc as a nested data structure"""
	soup = BeautifulSoup(doc, from_encoding='utf-8')
	#print(soup.prettify())
	return soup

def get_events (soup):
	events = soup.find_all(class_="eventful")
	#print(allevents)
	return events

# temprorarily here for learning purposes
# print(soup.prettify())
# print(soup.title)
# print(soup.title.attrs)
# print(soup.title.string)
# always do str(tag) before using the string otherwise you will carry around the reference to the whole bs4 object!
# unistring = str(soup.title.string)
# print(unistring)
# print(type(unistring))
# for i in unistring:
# 	print(i)
# print(soup.find_all('a'))
# print(soup.original_encoding)

if __name__ == "__main__":
	print(request_page(URL))
#	daterange = input("Please enter a date range.")

