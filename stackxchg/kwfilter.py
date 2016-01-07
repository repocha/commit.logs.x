import os
import sys
import simplejson
import string

from lxml import etree
from lxml.html import fromstring
import lxml.html as lh
from StringIO import StringIO

def filterall(dirp, kws):
  for f in os.listdir(dirp):
    ppath = os.path.join(dirp, f)
    url = filter(ppath, kws)
    if url != None:
      print url

def filter(pagepath, kws):
  """
  Success: return the url
  Failure: return None
  """
  conff = []
  f = open(pagepath)
  xml = f.read()
  f.close()
  doc = fromstring(xml)
  purl = getlink(doc)
  for question in doc.find_class('question'):
    qt = question.text_content().lower()
    for kw in kws:
      if kw in qt:
        return purl
  for answer in doc.find_class('answer'):
    at = answer.text_content().lower()
    for kw in kws:
      if kw in at:
        return purl
  return None

def getlink(doc):
  for l in doc.iter('link'):
    if l.get('rel') == 'canonical':
      return l.get('href')

#checkAll('/home/xuepeng/everything_about_apache/')
#checkAll('everything_about_apache_stackoverflow/')
#print filter('adding-a-reverse-proxy-nginx-or-varnish', ['hello the reverse reverse'])
filterall('/media/tianyin/TOSHIBA EXT/tixu_old/xuepeng/iconfigure/everything_about_apache', ['permission den'])
