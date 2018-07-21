1.	import requests
2.	from bs4 import BeautifulSoup
3.	url = "http://www.cricbuzz.com/cricket-match/live-scores"
4.	res = requests.get(url)
5.	soup = BeautifulSoup(res.content,"lxml")
6.	print("\t\t\t\tWELCOME TO LIVE CRICKET SCORE")
7.	print("\n\n\n\n")
8.	#print(soup.find_all("a",{"class":"cb-lv-scrs-well-live"})[0].text)
9.	for item in soup.find_all("a",{"class":"cb-lv-scrs-well-live"}):
10.		print("\t\t\t"+item.text)	
11.	print("\n\n\n")
