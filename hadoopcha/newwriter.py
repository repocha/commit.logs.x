import os
import urllib2

from lxml import etree
from lxml import html
from bs4 import BeautifulSoup

output = open('hadoop-jira', 'a')

for num in range(1, 11298):

        #url = "https://issues.apache.org/jira/browse/HADOOP-" + str(num)
        #req = urllib2.Request(url)
        #resp = urllib2.urlopen(req)
        #content = resp.read()
	
	case = open("pages/HADOOP-" + str(num), 'r')	

	#html = BeautifulSoup(content)
	html = BeautifulSoup(case)
	
	output.write("\n\n-------------------------------------------------------------------------\n")
	output.write(html.title.string.encode('utf-8'))
	output.write('\n')

	descriptions = html.find_all("div", "user-content-block")
	for description in descriptions:
		output.write(description.get_text().encode('utf-8').strip())
	#output.write(descriptions[0].get_text())
	output.write('\n')
	
	#comments = html.find_all("div", "issue-data-block activity-comment twixi-block  expanded")
	#comments = html.find_all("div", "action-details flooded")
	comments = html.find_all("div", "action-body flooded")	
	for comment in comments:
		output.write(comment.get_text().encode('utf-8'))
	#print html.find_all("div", "issue-data-block activity-comment twixi-block  expanded")[1].get_text()
	
	if num % 10 ==0:
		print "finish " + str(num)	
	

output.close()
