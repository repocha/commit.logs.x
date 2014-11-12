import sys
sys.path.append('..')
from crawler import Crawler

import urllib2
import os

from lxml import etree
from lxml import html
from bs4 import BeautifulSoup


class HadoopJIRACrawler(Crawler):

    def crawl(self):
        for index in range(1, 11298):
	        number = "HADOOP-" + str(index)
	        url="https://issues.apache.org/jira/browse/" + number

	        page =urllib2.urlopen(url)
	        data=page.read()

	        fwriter = open(self.output_dir+'/'+number, 'w')
	        fwriter.write(data)
	        fwriter.close()


    def write2log(self):
	    output = open(self.output_log, 'a')
	    for num in range(1, 11298):
		    case = open(self.output_dir + "/HADOOP-" + str(num), 'r')	
		    html = BeautifulSoup(case)
			
		    #title part
		    output.write("\n\n-------------------------------------------------------------------------\n")
		    output.write(html.title.string.encode('utf-8'))
		    output.write('\n')
		
		    #description part
		    descriptions = html.find_all("div", "user-content-block")
		    for description in descriptions:
			    output.write(description.get_text().encode('utf-8').strip())
		    output.write('\n')
	
		    #comments part
		    comments = html.find_all("div", "action-body flooded")	
		    for comment in comments:
			    output.write(comment.get_text().encode('utf-8'))
			
		    if num % 10 ==0:
			    print "finish " + str(num)	
	
	    output.close()		


hadoopjiracrawler = HadoopJIRACrawler("/home/long/Research/Conquid/pages", "hadoop.jira.log")
#hadoopjiracrawler.crawl()
hadoopjiracrawler.write2log()
