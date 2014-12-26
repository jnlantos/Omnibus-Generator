from bs4 import BeautifulSoup
import urllib.request
import datetime
import re
import generate

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

def get_event_info (href_list):
	"""Return formatted html for each event"""
	events_string = ""
	color = "#fffcc"

	for href in href_list:
		soup = make_soup(request_page(href))
		
		# DO LATER. FOR NOW PLACEHOLDERS.
		# --------------------------------------------------
		title = soup.h1.get_text()
		#print(title)
		date = (soup.find(class_="site-posts").p.br).decode("utf-8")
		print(date)
		time = soup.find(class_="site-posts").p.i.get_text()
		#print(time)
		content = "Talk title"
		room = "Room123"
		year = "2015"

		month1 = "month1"
		date1 = "date1"
		year1 = "year1"
		month2 = "month2"
		date2 = "date2"
		year2 = "year2"
		# --------------------------------------------------

		# Alternate the background color of each event
		if color == "#ffffcc":
			color = "#ffcc33"
		else:
			color = "#ffffcc"

		events_string += """<tr>
	      <td valign="top" bgcolor=""" + color + """"><a moz-do-not-send="true" href=""" + href + ">" + title  + "</a>(" + room + " - " + date + " - " + year + ";" + time + ")<br><br>" + content +"""<br>
	      </td>
	      </tr>"""

	return events_string, month1, date1, year1, month2, date2, year2

	

if __name__ == "__main__":

	URL = "http://www.philosophy.utoronto.ca/events/"
	TODAY = datetime.datetime.today()
	NUM_MONTH = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
	HREF_LIST = []
	SOUP = make_soup(request_page(URL))
	

	events_string = ""
	month1 = ""
	date1=""
	year1=""
	month2=""
	date2=""
	year2=""
	me = "myemail@gmail.com"
	recipient = "somebodyelse@hotmail.com"
	
	# Will ask for start date and number of weeks as user input...DO LATER.

	for date in date_range(TODAY, 2):
		# Go to the next month in the calendar if needed
		if ((date.month > NUM_MONTH[get_month(SOUP)[0]]) or (date.month < NUM_MONTH[get_month(SOUP)[0]])):
			next = SOUP.find(class_="em-calnav full-link em-calnav-next")["href"]
			SOUP = make_soup(request_page(URL + next))

		for e in get_events(SOUP, date):
			if ((date.year == int(get_month(SOUP)[1])) and (date.month == NUM_MONTH[get_month(SOUP)[0]]) and (date.day == int(e.a.get_text()))):
				HREF_LIST.append(e.a["href"])
		
	#print(HREF_LIST)

	events_string, month1, date1, year1, month2, date2, year2 = get_event_info(HREF_LIST)
	print(events_string)
	print(month1)
	print(month2)
	print(date1)
	print(date2)
	print(year1)
	print(year2)

	generate.format(month1, date1, year1, month2, date2, year2, events_string, me, recipient)
	
#---------------------------------------
# TEMPORARILY HERE FOR LEARNING PURPOSES
#---------------------------------------

# print(soup.prettify())
# print(soup.title)
# print(soup.title.attrs)
# print(soup.title.string)
# always do str(tag) before using the string otherwise you will carry around the reference to the whole bs4 object! SHOULD GO AND CHECK THIS LATER!
# unistring = str(soup.title.string)
# print(unistring)
# print(type(unistring))
# for i in unistring:
# 	print(i)
# print(soup.find_all('a'))
# print(soup.original_encoding)
	
# url = request_page(URL)
# SOUP = make_soup(url)
# month = get_month(SOUP)
# print(date_range(TODAY, 2))
# print (TODAY)
			
# for event in events:
	# print(date.year == int(get_month(soup)[1]))
	# print(date.month == NUM_MONTH[get_month(soup)[0]])
	# print(date.day == int(event.a.get_text()))
	# print (date)
	# print (event.a.get_text())

# daterange = input("Please enter a date range.")