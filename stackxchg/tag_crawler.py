import os
import sys
import string
import time

from lxml import etree
from lxml.html import fromstring
import lxml.html as lh
from StringIO import StringIO

sys.path.insert(0, '..')
from crawler import crawl

"""
Crawl all the question URLs associated with a given tag
"""

"""
change these for every tag
"""
WEBSITE = 'http://serverfault.com'
URL_TEMPLATE = WEBSITE + "/questions/tagged/TAG?page=PN"
DOWNLOAD_DIR = '/tmp/serverfault_tags_TAG' 

#Crawl the entry pages of users
def crawlTagPages(tag):
  """
  Crawl tag pages
  """
  i = 1
  while True:
    url = URL_TEMPLATE.replace('TAG', tag).replace('PN', str(i))
    fp  = os.path.join(DOWNLOAD_DIR.replace('TAG', tag), "tag_page_" + str(i))
    print 'CRAWLING', url
    crawl(url, fp)
    if containsQuestions(fp):
      i += 1
    else:
      return 

def containsQuestions(page):
  """
  Whether the page contains questions
  """
  with open(page) as f:
    doc = fromstring(f.read())
    for qlnk in doc.find_class('question-summary'):
      return True
  return False

if __name__ == "__main__":
  tag = raw_input('Enter the tag name: ')
  print 'Crawling tag pages of "' + tag + '"'
  if os.path.exists(DOWNLOAD_DIR.replace('TAG', tag)) == False:
    os.makedirs(DOWNLOAD_DIR.replace('TAG', tag)) 
  crawlTagPages(tag)
