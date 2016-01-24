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
import config

"""
Crawl all the tags in this site
"""

SECTION = 'tag_crawler'
conf = config.getconfig()

download_dir = conf.get(SECTION, 'download_dir')
if os.path.exists(download_dir) == False:
  os.makedirs(download_dir)

def crawlTagPages():
  """
  Crawl pages that list all the tag information
  """
  i = 1
  while True:
    url = conf.get(SECTION, 'tags_template').replace('PN', str(i))
    fp  = os.path.join(download_dir, "tag_page_" + str(i))
    print 'CRAWLING: ', url
    crawl(url, fp)
    if containsTag(fp):
      i += 1
    else:
      return

def containsTag(page):
  """
  Whether the page contains questions
  """
  with open(page) as f:
    doc = fromstring(f.read())
    for tag in doc.find_class('tag-cell'):
      return True
  return False

def aggrTagsStats():
  tagstats = {}
  for f in os.listdir(download_dir):
    fp = os.path.join(download_dir, f)
    with open(fp) as f:
      doc = fromstring(f.read())
      for tagcell in doc.find_class('tag-cell'):
        tag = ''
        cnt = 0
        for pt in tagcell.find_class('post-tag'):
          tag = pt.text_content()
        for im in tagcell.find_class('item-multiplier'):
          for cnt in im.find_class('item-multiplier-count'):
            cnt = cnt.text_content()
        tagstats[tag] = long(cnt)
  return tagstats

def dumpTags(tosort=True):
  with open(conf.get(SECTION, 'tag_list'), 'w') as f:
    stats = aggrTagsStats()
    if tosort:
      stats = reversed(sorted(stats.items(), key=lambda x: x[1]))
    for t in stats:
      f.write(t[0] + ',' + str(t[1]) + '\n')

if __name__ == "__main__":
  #crawlTagPages()
  #tag = raw_input('Enter the tag name: ')
  dumpTags()
