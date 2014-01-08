import threading
import urllib2
from bs4 import BeautifulSoup
import datetime

class MyThread(threading.Thread):

	def __init__(self, url):
		threading.Thread.__init__(self)
		self.url = url

	def run(self):
		request = urllib2.Request(self.url, headers={'User-Agent' : 'Magic Browser'})
		soup = BeautifulSoup( urllib2.urlopen( request ).read() )


my_urls = ['http://www.google.com', 'http://www.yahoo.com', 'http://www.reddit.com', 'http://www.fifa.com', 'http://watchanimeon.com']

time1 = datetime.datetime.now()

for url in my_urls:
	my_thread = MyThread(url)
	my_thread.start()
	print('Done')

time2 = datetime.datetime.now()

total1 = (time2 - time1).microseconds
print('Total time elapsed for threaded function is %s microseconds') % (total1)



time3 = datetime.datetime.now()

for url in my_urls:
	request = urllib2.Request(url, headers={'User-Agent' : 'Magic Browser'})
	soup = BeautifulSoup( urllib2.urlopen( request ).read() )

time4 = datetime.datetime.now()

total2 = (time4 - time3).microseconds
print('Total time elapsed for threaded function is %s microseconds') % (total2)

difference = total2 / total1

print(difference)
