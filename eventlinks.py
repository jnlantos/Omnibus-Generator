from bs4 import BeautifulSoup
import urllib.request
import datetime
import re

def request_page (url):
	"""Return a handle to the web page at url"""
	try:
		response = urllib.request.urlopen(url)
		#print(response.info())
		return response
	except URLError:
		print("Unable to open " + url + ".")
		pass

def make_soup (doc):
	"""Return a bs4 object representing doc as a nested data structure"""
	soup = BeautifulSoup(doc, from_encoding='utf-8')
	#print(soup.prettify())
	return soup

def date_range(date, weeks):
	"""Return a list of the dates in the next weeks weeks starting from date"""
	d = (weeks * 7)
	date_list = [date + datetime.timedelta(days=x) for x in range(0, d + 1)]
	return date_list

def get_month (soup):
	"""Return the page's month and year in the format of [month, year]"""
	month = soup.find(class_="month_name").get_text()
	return month.split()

def get_events (soup, date):
	"""Return the page's events on a particular date"""
	events = soup.find_all(class_=re.compile("eventful|eventful-today"))
	return events
	

if __name__ == "__main__":

	URL = "http://www.philosophy.utoronto.ca/events/"
	TODAY = datetime.datetime.today()
	NUM_MONTH = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
	HREF_LIST = []
	SOUP = make_soup(request_page(URL))

	for date in date_range(TODAY, 2):
		#go to the next month if needed
		if ((date.month > NUM_MONTH[get_month(SOUP)[0]]) or (date.month < NUM_MONTH[get_month(SOUP)[0]])):
			next = SOUP.find(class_="em-calnav full-link em-calnav-next")["href"]
			SOUP = make_soup(request_page(URL + next))

		for e in get_events(SOUP, date):
			if ((date.year == int(get_month(SOUP)[1])) and (date.month == NUM_MONTH[get_month(SOUP)[0]]) and (date.day == int(e.a.get_text()))):
				HREF_LIST.append(e.a["href"])
		

	
	print(HREF_LIST)
	

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

	
	#url = request_page(URL)
	#SOUP = make_soup(url)
	#month = get_month(SOUP)
	#print(date_range(TODAY, 2))
	#print (TODAY)
			

# for event in events:
	# 	# print(date.year == int(get_month(soup)[1]))
	# 	# print(date.month == NUM_MONTH[get_month(soup)[0]])
	# 	# print(date.day == int(event.a.get_text()))
	# 	#print (date)
	# 	#print (event.a.get_text())


#	daterange = input("Please enter a date range.")