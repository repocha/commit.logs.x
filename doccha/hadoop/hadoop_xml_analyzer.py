import os
from lxml import etree
from lxml.html import fromstring
import lxml.html as lh
import csv
import subprocess
import os
import fnmatch
import filecmp

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

def findDefaultXML(repop):
  """
  Hadoop's config file is all named XXX-default.xml,
  and we want to automatically find these config files given a repository
  """
  pattern = '*default*.xml'
  flst = []
  ignore = []
  for dname, sdname, flist in os.walk(repop):
    for fname in flist:
      if fnmatch.fnmatch(fname, pattern):
        if fname.find('test') != -1:
          #print 'Ignore: ', fname
          ignore.append(fname)
        elif dname.find('/test') != -1: # it is located in a test dir
          #print 'Ignore: ', dname, fname
          pass
        else:
          flst.append(os.path.join(dname, fname))
  return flst, ignore

#TODO: put the parameters of each version into a set,
#also, we need to handle multiple xmls with the same name
#also, print out all the xml names so that we can remove some of them
def findXMLFiles(repodir):
  xmlsmap = {}
  ignored = []
  for repo in os.listdir(repodir):
    xmlsmap[repo] = []
    repop = os.path.join(repodir, repo)
    if os.path.isdir(repop):
      print repop, '-----------------------------------------'
      xml2anyz, ign = findDefaultXML(repop)
      for ix in ign:
        if ix not in ignored:
          ignored.append(ix)
      #here we want to dedup because sometimes the same files occur multiple times...
      unqxml2anyz = []
      for xa in xml2anyz:
        dup = False
        for uxa in unqxml2anyz:
          if os.path.basename(xa) == os.path.basename(uxa):
            # compare the contents
            if filecmp.cmp(xa, uxa) == False:
              print '[ERROR] The two config file has the same name but different contents:'
              print xa
              print uxa
              print '---------------------------------------------------------------------'
              break
            else:
              dup = True
              break
        if dup == False:
          unqxml2anyz.append(xa)
      print '#dup xmls: ', str(len(xml2anyz) - len(unqxml2anyz)) 
  for ix in ignored:
    print 'IGNORED FILE NAMES: ', ix
            
findXMLFiles('/media/tianyin/TOSHIBA EXT/software/hadoop-dist/')
