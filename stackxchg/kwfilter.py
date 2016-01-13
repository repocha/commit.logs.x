import os
import sys
import simplejson
import string

from lxml import etree
from lxml.html import fromstring
import lxml.html as lh
from StringIO import StringIO

def filterall(dirp, kws, known=None):
  for f in os.listdir(dirp):
    ppath = os.path.join(dirp, f)
    try:
      url = filter(ppath, kws)
      if known != None and url in known:
        continue
      if url != None:
        print url
    except:
      print 'FAILURE: ', ppath
      continue

def filter(pagepath, kwss):
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
    for kws in kwss:
      if containsAll(qt, kws):
        return purl
  for answer in doc.find_class('answer'):
    at = answer.text_content().lower()
    for kws in kwss:
      if containsAll(at, kws):
        return purl
  return None

def containsAll(text, kws):
  for kw in kws:
    if kw not in text:
      return False
  return True

def getlink(doc):
  for l in doc.iter('link'):
    if l.get('rel') == 'canonical':
      return l.get('href')

permKW = [
          ['permission', 'deny'],   
          ['permission', 'denied'], 
          ['perm', 'deny'],   
          ['perm', 'denied'], 
        ]

accessKW = [
          ['access', 'deny'],
          ['access', 'denied']
        ]

#checkAll('/home/xuepeng/everything_about_apache/')
#checkAll('everything_about_apache_stackoverflow/')
#print filter('adding-a-reverse-proxy-nginx-or-varnish', ['hello the reverse reverse'])
#filterall('/media/tianyin/TOSHIBA EXT/tixu_old/xuepeng/iconfigure/everything_about_apache', accessKW)

#known = []
#with open('mysql_perm_deny_urls') as f:
#  for l in f:
#    known.append(l.strip())
#print len(known)
#filterall('/media/tianyin/TOSHIBA EXT/tixu_old/xuepeng/iconfigure/everything_about_mysql', accessKW)
filterall('/media/tianyin/TOSHIBA EXT/tixu_old/xuepeng/iconfigure/everything_about_mysql', permKW)
