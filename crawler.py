import urllib2
import time

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

def crawl(url, dstpath, intv=1):
  """
  Utility function
  """
  with open(dstpath, 'w') as of:
    of.write(urllib2.urlopen(url).read())
    time.sleep(intv)

