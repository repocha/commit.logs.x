import os

"""
All the versions of httpd software packages are archived here.
"""
URL = 'http://archive.apache.org/dist/httpd/'

def wgets(links):
    """
    Simple utility to crawl the packages
    """
    for l in links:
        os.system("wget " + l) 
        time.sleep(1)

def getLinks(index):
    """
    return all the urls of the httpd packages
    """
    f = open(index, 'ro')
    links = []
    for line in f:
        if line.find('[TXT]') == -1:
            if line.find('.tar.gz') != -1:
                l = line
                l = l[l.find('>')+1:]
                l = l[l.find('>')+1:]
                link = l[:l.find('<')]
                print link
                links.append(URL + link)
    print len(links)
    return links

links = getLinks('httpd_archives_lst.html')
wgets(links)
