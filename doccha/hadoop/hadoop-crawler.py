import os

URL = 'http://archive.apache.org/dist/hadoop/core/'

def wgets(links):
    for l in links:
        os.system("wget " + l) 
#        time.sleep(1)

def getLinks(index):
    f = open(index, 'ro')
    links = []
    for line in f:
        if line.find('hadoop-') != -1:
            l = line
            l = l[l.find('>')+1:]
            l = l[l.find('>')+1:]
            link = l[:l.find('<')]
            if line.find('[DIR]') != -1:
                if link.endswith('/'):
                    fname = link[:-1] + '.tar.gz'
                    link = link + fname
                else:
                    print '[ERROR]', link
                print URL + link
                links.append(URL + link)
            elif line.find('[TXT]') != -1:
                pass
            else:
                print URL + link
                links.append(URL + link)
    return links

links = getLinks('/home/tixu/software/scripts/index.html')
wgets(links)
