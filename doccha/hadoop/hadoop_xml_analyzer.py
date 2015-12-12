import os
from lxml import etree
from lxml.html import fromstring
import lxml.html as lh
import csv
import subprocess
import os
import fnmatch
import filecmp

#TODO: there are a list of renamed parameters 

def getParamsFromXML(defxml, repo):
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
    p['repo'] = repo
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
          print 'FIND XML: ', os.path.join(dname, fname)
          flst.append(os.path.join(dname, fname))
  return flst, ignore

def findXMLFiles(repodir):
  """
  Find the xml config files from all the versions
  """
  xmlsmap = {}
  ignored = []
  allxmls = []
  for repo in os.listdir(repodir):
    repop = os.path.join(repodir, repo)
    #xmlsmap[repop] = []
    if os.path.isdir(repop):
      #print repop, '-----------------------------------------'
      xml2anyz, ign = findDefaultXML(repop)
      for ix in ign:
        if ix not in ignored:
          ignored.append(ix)
      #here we want to dedup because sometimes the same files occur multiple times...
      unqxml2anyz = []
      for xa in xml2anyz:
        if os.path.basename(xa) not in allxmls:
          allxmls.append(os.path.basename(xa))
        dup = False
        for uxa in unqxml2anyz:
          if os.path.basename(xa) == os.path.basename(uxa):
            # compare the contents
            if filecmp.cmp(xa, uxa) == False:
              print '---------------------------------------------------------------------'
              print '| [ERROR] The two config file has the same name but different contents:'
              print '|', xa
              print '|', uxa
              print '---------------------------------------------------------------------'
              break
            else:
              dup = True
              break
        if dup == False:
          unqxml2anyz.append(xa)
      xmlsmap[repop] = unqxml2anyz
      print '#dup xmls: ', str(len(xml2anyz) - len(unqxml2anyz))
  for ix in ignored:
    print 'IGNORED FILE NAMES: ', ix
  for xml in allxmls:
    print 'XMLS: ', xml
  return xmlsmap            

def buildParamsMap():
  """
  ParamsMap should be in the following format
  {version : {name : pstruct}}
  """
  paramsMap = {}
  xmlsmap = findXMLFiles('/media/tianyin/TOSHIBA EXT/software/hadoop-dist/')
  for d in xmlsmap:
    print '>>> ', d, len(xmlsmap[d])
    pmap = {}
    for xml in xmlsmap[d]:
      for p in getParamsFromXML(xml, d):
        if p['name'] in pmap:
          if p['default'] != pmap[p['name']]['default']:
            print '---------------------------------------------------------------------------------------'
            print '| [ERROR] the default of ', p['name'], 'is different.'
            print '|', p['default'], '<>', pmap[p['name']]['default'] 
            if p['file'] == pmap[p['name']]['file']:
              print '| DIFF IN SAME FILE: '
              print '|', p['file']
            else:
              print '| DIFF IN DIFF FILES: '
              print '|', p['file']
              print '|', pmap[p['name']]['file']
            print '---------------------------------------------------------------------------------------'
          else:
            pass
        else:
          pmap[p['name']] = p
    #print d, len(pmap)
    paramsMap[d] = pmap
  return paramsMap

def getVersionOrder():
  pass

def checkDefaultDiff():
  paramsMap = buildParamsMap() 
  #1. get all the parameters
  plst = []
  for v in paramsMap:
    for p in paramsMap[v]:
      if p not in plst:
        plst.append(p)
  print '#Total params: ', len(plst)
  pDef = {}
  for p in plst:
    pDef[p] = {}
    for v in paramsMap:
      if p in paramsMap[v]:
        if 'default' not in paramsMap[v][p]:
          paramsMap[v][p]['default'] = ''
        if paramsMap[v][p]['default'] not in pDef[p]:
          pDef[p][paramsMap[v][p]['default']] = [os.path.basename(paramsMap[v][p]['repo']) + '|' + os.path.basename(paramsMap[v][p]['file'])]
        else:
          pDef[p][paramsMap[v][p]['default']].append(os.path.basename(paramsMap[v][p]['repo']) + '|' + os.path.basename(paramsMap[v][p]['file']))
  for p in pDef:
    if len(pDef[p]) > 1: #i.e., it is changed...
      print p, pDef[p].keys()
  for p in pDef:
    if len(pDef[p]) > 1:
      print '>>> ', p
      for v in pDef[p]:
        print v, pDef[p][v]

#checkConsistencyInSameVersion()
checkDefaultDiff()

