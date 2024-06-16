import requests
from bs4 import BeautifulSoup as bs

newspaper = "https://economictimes.indiatimes.com"

def extract_links_from_html(page_html: str) -> list:
	soup = bs(page_html, 'html.parser')
	li_tags = soup.find_all('li')
	links = []
	for li in li_tags:
		for a_tag in li.find_all('a'):
			if a_tag['href'] != '#':
				links.append(a_tag['href'])
			else:
				return links
	return links



def get_page_from_url(year: int , month: int , time: int , date: int = 1):
	url = "https://economictimes.indiatimes.com/archivelist/year-%d,month-%d,starttime-%d.cms" % (year, month, time)

	response = requests.get(url)
	
	if response.status_code == 200:
		links = extract_links_from_html(response.text)
		print("Total Number of links is %d and year, month, date and time is %d , %d , %d , %d" % (len(links), year , month , date , time))
		for link in links:
			# print(newspaper+link)
			#instead of priniting, we will store the links in a csv file
			# format will be:
			# year, month, date, link
			with open("economictimes.csv", "a") as f:
				f.write("%d,%d,%d,%s\n" % (year, month, date, newspaper+link))
	else:
		print("FAILED to get page from url %s" % url)

def leap(year: int) -> bool:
	return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

year = 2008
month = 1
start_time = 39448 # 1st Jan 2007
end_time = 45456 # 13th June 2024

x = {
	1:31, 
	2:28,
	3:31,
	4:30,
	5:31,
	6:30,
	7:31,
	8:31,
	9:30,
	10:31,
	11:30,
	12:31
}

def get_all_pages(start_time: int , end_time: int , year: int , month: int) -> None:
	date = 1
	for time in range(start_time, end_time):
		get_page_from_url(year , month , time , date)
		date += 1
		if((not leap(year) and date == x[month]+1)):
			date = 1
			month += 1
			if(month == 13):
				month = 1
				year += 1
		elif leap(year) and month == 2 and date == 30:
			date = 1
			month += 1
			if(month == 13):
				month = 1
				year += 1
		elif leap(year) and month != 2 and date == x[month]+1:
			date = 1
			month += 1
			if(month == 13):
				month = 1
				year += 1


# get_page_from_url(year= year, month=month, time= start_time)

get_all_pages(start_time, end_time, year, month)

