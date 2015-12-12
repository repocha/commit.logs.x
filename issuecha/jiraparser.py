import os
from lxml import etree
from lxml.html import fromstring
from lxml.html import tostring
import lxml.html as lh
import csv
from io import StringIO, BytesIO

def parse(jpath):
  """
  Now we only care about 'title' and 'summary'
  """
  jira = {}
  f = open(jpath)
  html = f.read()
  f.close()
  doc = fromstring(html)
  #for title in doc.get_element_by_id('summary-val'):
  for title in doc.xpath("//h1[@id='summary-val']"):
    jira['title'] = title.text_content().strip()
  for summary in doc.find_class('user-content-block'):
    jira['summary'] = summary.text_content().strip()
  if 'title' not in jira:
    print 'ERROR: NO TITLE'
  return jira

CONFIG_KW = [
        'config', 
        'option',
        'propert'
        ]

def filter(jira, keywords = CONFIG_KW):
  """
  return whether the jira contains the predefined keywords
  """
  for kw in keywords:
    if jira['title'].lower().find(kw) != -1:
      return True
    if jira['summary'].lower().find(kw) != -1:
      return True
  #none of the keywords is found
  return False 

print filter(parse('/media/tianyin/TOSHIBA EXT/tixu_old/longjin/hadoop-jira/HADOOP-/HADOOP-2222'))
