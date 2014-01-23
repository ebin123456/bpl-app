from bs4 import BeautifulSoup
import mechanize
import sys
import os
import sqlite3



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
	out=[]
	soup = BeautifulSoup(data)
	lg_table = soup.find_all('table',class_="league-wc table mtn bbn")[0].find_all('tr')
	#print lg_table
	for row in lg_table:
		#print 44
		if first:
			first = False
			continue
		td = row.find_all('td')
		td.pop(0)
		td.pop(0)
		tmp_row = []
		#tmp_row.append('')
		for col in td:
			tmp_row.append(col.text)
		out.append(tuple(tmp_row))
		
	return  out
		


def insert_to_db(data_to_db):
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.executemany('INSERT INTO epl_table VALUES (?,?,?,?,?,?,?,?,?)', data_to_db)
	conn.commit()
	conn.close()

def main():
	data = get_data('http://livescore.com/soccer/england/premier-league/')
	data_to_db = parse_data(data)
	insert_to_db(data_to_db)
if __name__ == '__main__':
	main()

