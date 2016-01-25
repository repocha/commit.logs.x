import os
import sys
import string
import random
sys.path.insert(0, '..')
from kwfilter import KWFilter
from hparser import parseHTML
import config

def selectall(dirp, kwfilt, known=None):
  """
  Select all the html files in $dirp that matches the keyword-based filter.
  If the url of the html files is in $known, we ignore it.
  """
  res = []
  for f in os.listdir(dirp):
    ppath = os.path.join(dirp, f)
    page = parseHTML(ppath)
    if page == None: #parsing failure
      continue
    if interested(page, kwfilt):
      url = page['url']
      if known != None and url in known:
        continue
      print 'FOUND URL: ', url
      res.append(url)
  random.shuffle(res)
  return res

def interested(page, kwfilt):
  """
  Success: return the url
  Failure: return None
  """
  if page['stat'] == 'open':
    return False
  for question in page['question']:
    if kwfilt.contains(question):
      return True
  for answer in page['answer']:
    if kwfilt.contains(answer):
      return True
  return False

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

forbidKW = [
          ['forbidden'],
          ['authoriz']
        ]

tag = raw_input('Enter the tag name: ')

SECTION = 'tagged_url_crawler'
conf = config.getconfig()
case_dir = conf.get(SECTION, 'case_dir_template').replace('TAG', tag)

kwfilt = KWFilter(permKW + accessKW + forbidKW, {'htaccess' : 'htakkess'})
with open(tag+'_selected.lst', 'w') as f:
  for url in selectall(case_dir, kwfilt):
    f.write(url + '\n')

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
