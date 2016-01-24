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
Crawl all the question URLs associated with a given tag
"""

SECTION = 'tagged_url_crawler'
conf = config.getconfig()

def crawlTagPages(tag):
  """
  Crawl tag pages
  """
  i = 1
  while True:
    url = conf.get(SECTION, 'tagged_urls_template').replace('TAG', tag).replace('PN', str(i))
    fp  = os.path.join(conf.get(SECTION,'download_dir').replace('TAG', tag), "tag_page_" + str(i))
    print 'CRAWLING: ', url
    crawl(url, fp)
    if containsQuestions(fp):
      i += 1
    else:
      return 

def xtrAllQuestionURLs(dirp, fp):
  """
  Extract all the page links
  """
  with open(fp, 'w') as lf:
    fl = os.listdir(dirp)
    for f in fl:
      fp = os.path.join(dirp, f)
      for l in xtrQuestionURLs(fp):
        lf.write(l + '\n')


def xtrQuestionURLs(tpg):
  """
  Extract the page link into a file
  """
  qlst = []
  with open(tpg) as f:
    doc = fromstring(f.read())
    doc.make_links_absolute(conf.get(SECTION, 'website'))
    for qsum in doc.find_class('question-summary'):
      for qlnk in qsum.find_class('question-hyperlink'):
        for url in qlnk.iterlinks():
          qlst.append(url[2])
  return qlst

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
  downloadDir = conf.get(SECTION, 'download_dir').replace('TAG', tag)
  questionLst = conf.get(SECTION, 'post_list').replace('TAG', tag)

  if os.path.exists(downloadDir) == False:
    os.makedirs(downloadDir) 
  crawlTagPages(tag)
  xtrAllQuestionURLs(downloadDir, questionLst)
  #print xtrQuestionURLs('/tmp/serverfault_tags_vsftpd/tag_page_1')
