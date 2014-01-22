from bs4 import BeautifulSoup
import mechanize
import sys
import os


def get_data(url):
    return open('out.html','r').read()
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'),
('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
    br.addheaders.append(("Accept-Language", "en-us,en"))
    br.set_handle_refresh(False)
    #br.header_items()
    data = br.open( url)  #
    return data.read()
def parse_data(data):
	first = True
	soup = BeautifulSoup(data)
	lg_table = soup.find_all('table',class_="league-wc table mtn bbn")[0].find_all('tr')
	#print lg_table
	for row in lg_table:
		#print 44
		if first:
			first = False
			continue
		td = row.find_all('td')
		print td[1].text
		print td[2].text
		print td[3].text
def insert_db():
	sql = ''' CREATE TABLE Student(
  id INTEGER PRIMARY KEY,
  team TEXT,
  week INTEGER, 
  win INTEGER,
  draw INTEGER,
  loss INTEGER,
  f INTEGER,
  a INTEGER,
  gd INTEGER,
  pts INTEGER,
);'''		
	    	# for col in td:
	    	# 	print col.text       



def main():
	data = get_data('http://livescore.com/soccer/england/premier-league/')
	parse_data(data)
if __name__ == '__main__':
	main()

