import sys
sys.path.append('..')
from crawler import Crawler

import urllib2

class HadoopJIRACrawler(Crawler):

    def crawl(self):
        for index in range(1, 11294):
	        number = "HADOOP-" + str(index)
	        url="https://issues.apache.org/jira/browse/" + number

	        page =urllib2.urlopen(url)
	        data=page.read()

	        fwriter = open(self.output_dir+'/'+number, 'w')
	        fwriter.write(data)
	        fwriter.close()

    def write2log()
