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
	#print(events)
	return events

def get_event_info (href_list):
	"""Return formatted html for each event"""
	events_string = ""
	color = "#fffcc"

	for href in range(len(href_list)):
		soup = make_soup(request_page(href_list[href]))
		
		title = geteventinfo_title(soup)
		date = geteventinfo_date(soup)
		time = geteventinfo_time(soup)
		content = "Talk title"
		room = geteventinfo_room(soup)
		color = geteventinfo_color(color)

		if href == 0:
			month1 = str(date.strftime("%B"))
			date1 = str(date.strftime("%d"))
			year1 = str(date.strftime("%Y"))

		if href == len(href_list) - 1:
			month2 = str(date.strftime("%B"))
			date2 = str(date.strftime("%d"))
			year2 = str(date.strftime("%Y"))

		events_string += """<tr>
	      <td valign="top" bgcolor=""" + color + """"><a moz-do-not-send="true" href=""" + href_list[href] + ">" + title + "</a> (" + room + " - " + str(date.strftime("%A, %B %d - %Y"))  + "; " + time + ")\n<br><br>" + content +"""<br>
	      </td>
	      </tr>"""

	#"If you want to turn Unicode characters back into HTML entities on output, rather than turning them into UTF-8 characters, you need to use an output formatter."
	
	#events_string = str(events_string.encode('utf-8'))

	# 1. Decode early 2. Unicode everywhere 3. Encode late.

	return events_string, month1, date1, year1, month2, date2, year2

def geteventinfo_color(color):
	# Alternate the background color of each event
	if color == "#ffffcc":
		color = "#ffcc33"
	else:
		color = "#ffffcc"
	return color

def geteventinfo_date(soup):
	date = (soup.find(class_="site-posts").p.br.next)
	date = date.split()[2].split("/")
	date_day = int(date[0])
	date_month = int(date[1])
	date_year = int(date[2])
	date = datetime.datetime(date_year, date_month, date_day)
	return date

def geteventinfo_time(soup):
	time = soup.find(class_="site-posts").p.i.get_text()
	#print(time)
	return time

def geteventinfo_room(soup):
	try:
		room = soup.find(class_="site-posts").p.next_sibling.next_sibling.a.get_text()
	except (Exception):
		room = "TBA"
		print("Could not find room. Make sure to replace it.")
		pass
	#print(room)
	return room

def geteventinfo_title(soup):
	title = soup.h1.get_text()
	#print(title)
	return title
	

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
	recipient = "somebodyelse.utoronto.ca"
	
	# Will ask for start date and number of weeks as user input...DO LATER.

	for date in date_range(TODAY, 2):
		# Go to the next month in the calendar if needed
		if ((date.month > NUM_MONTH[get_month(SOUP)[0]]) or (date.month < NUM_MONTH[get_month(SOUP)[0]])):
			next = SOUP.find(class_="em-calnav full-link em-calnav-next")["href"]
			SOUP = make_soup(request_page(URL + next))

		for e in get_events(SOUP, date):
			#print(e)
			if ((date.year == int(get_month(SOUP)[1])) and (date.month == NUM_MONTH[get_month(SOUP)[0]]) and (date.day == int(e.a.get_text()))):
				#print(e.ul.li)
				#if e.ul.li.next_sibling.next_sibling:
					#print(e.ul.li.next_sibling)
				HREF_LIST.append(e.ul.li.a["href"])
				# If there are two or more events on one day
				if e.ul.li.next_sibling.next_sibling:
					HREF_LIST.append(e.ul.li.next_sibling.a["href"])
		
	#print(HREF_LIST)
	

	events_string, month1, date1, year1, month2, date2, year2 = get_event_info(HREF_LIST)

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

# test when internet is down--get weird exceptions?