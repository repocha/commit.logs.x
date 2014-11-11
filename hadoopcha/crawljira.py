import urllib2

for index in range(1, 11294):

	number = "HADOOP-" + str(index)
	url="https://issues.apache.org/jira/browse/" + number

	page =urllib2.urlopen(url)
	data=page.read()

	fwriter = open("pages/"+number, 'w')
	fwriter.write(data)
	fwriter.close()
