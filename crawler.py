import urllib2
import time
import os

def crawl(url, dstpath, intv=1):
  """
  Utility function
  """
  with open(dstpath, 'w') as of:
    of.write(urllib2.urlopen(url).read())
    time.sleep(intv)

class Crawler:
  """
  The base class for crawler
  """
  def __init__(self, odir, olog):
    self.output_dir = odir
    self.output_log = olog

  def crawl(self):
    """
    Crawling stuff and output to the dir
    """
    pass

  def write2log(self):
    pass

class URLCrawler(Crawler):
  """
  Given a bunch of URLs, and crawl them all
  """
  def __init__(self, urls, odir, olog):
    self.output_dir = odir
    self.output_log = olog
    self.urls = urls

  def calibrate(self):
    crawled = []
    tocrawl = []
    for f in os.listdir(self.output_dir):
      if os.path.getsize(os.path.join(self.output_dir, f)) > 0:
        crawled.append(f) 
    for url in self.urls:
      if self.url2fname(url) not in crawled:
        tocrawl.append(url)
    print '--------------------------------------------------------------------'
    print ' CALIBRATION'
    print '--------------------------------------------------------------------'
    #print 'URL#1:        ', crawled[0]
    #print 'URL#2:        ', crawled[1]
    #print 'URL#3:        ', crawled[2]
    #print 'URL#4:        ', crawled[3]
    #print '--------------------------------------------------------------------'
    print '#CRAWLED URLS:', len(crawled)
    print '#TOCRAWL URLS:', len(tocrawl)
    print '--------------------------------------------------------------------'
    return tocrawl

  def crawl(self):
    tocrawl = self.calibrate()
    for url in tocrawl:
      try:
        crawl(url, os.path.join(self.output_dir, self.url2fname(url)))
        print 'CRAWLED: ', url
      except:
        print "FAILURE:", url

  def url2fname(self, url):
    return url[url.rfind('/') + 1:]

