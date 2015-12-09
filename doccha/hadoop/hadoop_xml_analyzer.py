import os
from lxml import etree
from lxml.html import fromstring
import lxml.html as lh
import csv
import subprocess
import os
import fnmatch

def findDefaultXML(repop):
  """
  Hadoop's config file is all named XXX-default.xml,
  and we want to automatically find these config files given a repository
  """
  pattern = '*default*.xml'
  flst = []
  for dname, sdname, flist in os.walk(repop):
    for fname in flist:
      if fnmatch.fnmatch(fname, pattern):
        if fname.find('test') != -1:
          print 'Ignore: ', fname
        else:
          flst.append(os.path.join(dname, fname))
  return flst

def getParamsFromXML(defxml):
  """
  Get all the parameters from the config files
  """
  plst = []
  f = open(defxml)
  xml = f.read()
  f.close()
  doc = fromstring(xml)
  for prop in doc.iter('property'):
    p = {}
    p['file'] = defxml
    for name in prop.iter('name'):
      p['name'] = name.text_content()
    for value in prop.iter('value'):
      p['default'] = value.text_content()
    plst.append(p)
  return plst

#TODO: put the parameters of each version into a set,
#also, we need to handle multiple xmls with the same name
#also, print out all the xml names so that we can remove some of them
BASE_REPO_DIR = '/media/tianyin/TOSHIBA EXT/software/hadoop-dist/'
for repo in os.listdir(BASE_REPO_DIR):
  repop = os.path.join(BASE_REPO_DIR, repo)
  if os.path.isdir(repop):
    print repop, '-----------------------------------------'
    for f in findDefaultXML(repop):
        print f


