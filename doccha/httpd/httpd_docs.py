import os
from lxml import etree
from lxml.html import fromstring
import lxml.html as lh
import csv
import filecmp

PKG_ROOT = '/media/tianyin/TOSHIBA EXT/software/httpd-dist'

def cmpLst(l1, l2):
  if len(l1) != len(l2):
    return False
  for e in l1:
    if e not in l2:
      return False
  return True

def diffLst(l1, l2):
  a = [] # add
  r = [] # remove
  m = [] # modify
  for e in l1['fp']:
    if e not in l2['fp']:
      r.append(e)
  for e in l2['fp']:
    if e not in l1['fp']:
      a.append(e)
    else:
      f1 = os.path.join(l1['px'], e)
      f2 = os.path.join(l2['px'], e)
      print f1
      print f2
      if filecmp.cmp(f1, f2) == False:
        m.append(e)
  return a, r, m

def lsFiles(docsdir):
  """
  Check if the docs files exist
  """
  res = []
  fl = os.listdir(docsdir)
  for f in fl:
    # We only track the .en version
    if (f.endswith('html') and f + '.en' not in fl) or (f.endswith('html.en')):
      #res.append(os.path.join(docsdir, f))
      res.append(f)
  return {'px' : docsdir, 'fp' : res}


l1 = lsFiles(PKG_ROOT + '/httpd-2.4.6/docs/manual/mod/')
l2 = lsFiles(PKG_ROOT + '/httpd-2.4.3/docs/manual/mod/')
#print cmpLst(l1, l2)
a, r, m = diffLst(l1, l2)
for e in a:
  print 'A   ', e
for e in r:
  print 'R   ', e
for e in m:
  print 'M   ', e

