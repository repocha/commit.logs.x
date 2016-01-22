import os
import sys
import simplejson
import string

from lxml import etree
from lxml.html import fromstring
import lxml.html as lh
from StringIO import StringIO

sys.path.insert(0, '..')
from kwfilter import KWFilter

def selectall(dirp, kwfilt, known=None):
  """
  Select all the html files in $dirp that matches the keyword-based filter.
  If the url of the html files is in $known, we ignore it.
  """
  for f in os.listdir(dirp):
    ppath = os.path.join(dirp, f)
    try:
      url = filter(ppath, kwfilt)
      if known != None and url in known:
        continue
      if url != None:
        print url
    except Exception as e:
      print 'FAILURE: ', ppath, ' | ', str(e)
      continue

def filter(pagepath, kwfilt):
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
    if kwfilt.contains(question.text_content().lower()):
      return purl
  for answer in doc.find_class('answer'):
    if kwfilt.contains(answer.text_content().lower()):
      return purl
  return None

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

kwfilt = KWFilter(permKW + accessKW, {'htaccess' : ''})
selectall('/media/tianyin/TOSHIBA EXT/tixu_old/xuepeng/iconfigure/everything_about_apache', kwfilt)

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
#filterall('/media/tianyin/TOSHIBA EXT/tixu_old/xuepeng/iconfigure/everything_about_mysql', permKW)
