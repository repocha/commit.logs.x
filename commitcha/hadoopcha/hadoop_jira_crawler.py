import sys
sys.path.append('..')
from crawler import Crawler

import urllib2
import os
import sleep
from lxml import etree
from lxml import html

class HadoopJIRACrawler(Crawler):
  def __init__(self, odir, pfx, f, l):
    self.output_dir = os.path.join(odir, pfx)
    self.output_log = 'jira.' + pfx + '.log'
    self.fst = f
    self.lst = l
    self.prefix = pfx
    self.pathprefix = os.path.join(self.output_dir, pfx)
    print 'Download to', self.output_dir

  def crawl(self):
    """
    Crawl the pages
    """
    for index in range(self.fst, self.lst):
      number = str(index)
      url = "https://issues.apache.org/jira/browse/" + self.prefix + number
      dst = self.pathprefix + number

      if os.path.exists(dst) == False or os.stat(dst).st_size == 0:
        print 'CRAWLING:', self.prefix + number
        try:
          page =urllib2.urlopen(url)
          data=page.read()
          fwriter = open(dst, 'w')
          fwriter.write(data)
          fwriter.close()
          time.sleep(1)
        except:
          pass
      else:
        print 'ALREADY CRAWLED:', self.prefix + number

  def check(self):
    for index in range(self.fst, self.lst):
      number = str(index)
      url = "https://issues.apache.org/jira/browse/" + self.prefix + number
      dst = self.pathprefix + number
      if os.path.exists(dst) == False or os.stat(dst).st_size == 0:
        print 'NEED TO CRAWL:', self.prefix + number
        return False
    return True

  def write2log(self):
    output = open(self.output_log, 'a')
    for num in range(self.fst, self.lst):
      case = open(self.pathprefix + str(num), 'r')	
      html = BeautifulSoup(case)
			
      #title part
      output.write("\n\n-------------------------------------------------------------------------\n")
      output.write(html.title.string.encode('utf-8'))
      output.write('\n')
            		
      #description part
      output.write('[DESC]\n')
      descriptions = html.find_all("div", "user-content-block")
      for description in descriptions:
        output.write(description.get_text().encode('utf-8').strip())
      output.write('\n')
            
      #comments part
      output.write('[COMMENTS]\n')
      comments = html.find_all("div", "action-body flooded")	
      for comment in comments:
        output.write(comment.get_text().encode('utf-8'))
			
      if num % 10 ==0:
        print "finish " + str(num)	
	
    output.write("\n\n-------------------------------------------------------------------------\n")
    output.close()		

ROOT_REPO = '/media/tianyin/TOSHIBA EXT/tixu_old/longjin/hadoop-jira/'
PREFIX = 'HADOOP-'
# https://issues.apache.org/jira/browse/HADOOP-12635?jql=project%20%3D%20HADOOP
hadoopjiracrawler = HadoopJIRACrawler(ROOT_REPO, PREFIX, 1, 12636)
#hadoopjiracrawler.check()
hadoopjiracrawler.crawl()
#hadoopjiracrawler.write2log()
