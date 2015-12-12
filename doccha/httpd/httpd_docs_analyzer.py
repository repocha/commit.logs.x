import os
from lxml import etree
from lxml.html import fromstring
from lxml.html import tostring
import lxml.html as lh
import csv
from io import StringIO, BytesIO

"""
TODO: 2.0.35 -- 2.0.42
"""

def getParamsFromHTML(path):
  """
  This should work for most new HTML manual pages
  Currently from 2.0.42 -- 2.4.7 
  """
  pset = []
  f = open(path)
  html = f.read()
  f.close()
  doc = fromstring(html)
  for dsec in doc.xpath("//div[@class='directive-section']"):
    #print '-------------------------------------------------'
    p = {}
    for h2 in dsec.iter('h2'):
      # print h2.text_content()
      p['name'] = h2.text_content().replace('Directive', '').strip()
      p['file'] = path
    for tr in dsec.iter('tr'):
      for th in tr.iter('th'):
        if th.text_content().strip().startswith('Default:'):
          for td in tr.iter('td'):
            # print td.text_content()
            p['default'] = td.text_content().strip()
        elif th.text_content().strip().startswith('Syntax:'):
          for td in tr.iter('td'):
            # print td.text_content()
            p['syntax'] = td.text_content().strip()
    if 'default' in p:
      p['default'] = p['default'].replace(p['name'], '').strip()
      if 'syntax' in p:
        p['syntax']  = p['syntax'].replace(p['name'], '').strip()
    #print p
    pset.append(p)
  #end for loop
  return pset    

def getParamsFromOldHTML(path):
  """
  This should work for httpd-1 (1.3.0 -- 1.3.42) 
  The old HTML pages are very hard to analyze as they do not have clear structures, 
  but are plain texts combined with <a>
  We define a set of specific rules to extract the config information
  """
  pset = []
  PROPS = {
          'directive-dict.html#Syntax'   : 'Syntax',
          'directive-dict.html#Default'  : 'Default',
          'directive-dict.html#Context'  : 'Context',
          'directive-dict.html#Status'   : 'Status',
          'directive-dict.html#Compatibility' : 'Compatibility',
          'directive-dict.html#Override' : 'Override',
          'directive-dict.html#Module'   : 'Module'
          }
  f = open(path)
  html = f.read()
  f.close()
  doc = fromstring(html)
  #1. ignore pages that do not have any directive-dict tags
  hasParams = False
  for e in doc.iter():
    if e.tag == 'a':
      if 'href' in e.attrib:
        if e.attrib['href'] in PROPS:
          hasParams = True
  if hasParams == False:
    print 'IGNORE: ', path 
    return []
  #2. then we split the page based on <HR>
  dstr = tostring(doc)
  hrSlices = dstr.split('<hr>')
  for hrSlice in hrSlices:
    #if hrSlice.find('<p>') != -1:
    #  hrSlice = hrSlice[ : hrSlice.find('<p>')]
    if hrSlice.find('<html>') == -1:
      hrSlice = '<html> ' + hrSlice
    if hrSlice.find('</html>') == -1:
      hrSlice = hrSlice + ' </html>'
    pname = None
    hrdoc = fromstring(hrSlice)
    for e in hrdoc.iter():
      if e.tag == 'a':
        if 'name' in e.attrib:
          pname = e.attrib['name']
    if pname == None:
      continue
    #print '---------------------------------------------'
    #print hrSlice
    #print pname
    props = []
    for e in hrdoc.iter():
      if e.tag == 'a':
        if 'href' in e.attrib and e.attrib['href'].find('directive-dict.html#') != -1:
          if e.attrib['href'] not in PROPS:
            print 'UNKNOWN TAG: ', e.attrib['href']
          else:
            props.append(PROPS[e.attrib['href']])
    props_idx = {}
    hrdoctext = hrdoc.text_content()
    for prop in props:
      props_idx[prop] = hrdoctext.find(prop)
    props_ridx = {}
    props_idx_lst = []
    for prop in props_idx:
      props_ridx[props_idx[prop]] = prop
      props_idx_lst.append(props_idx[prop])
    props_ridx[0] = 'Directive'
    props_idx_lst = sorted(props_idx_lst)
    #print props_ridx
    #print props_idx_lst
    pmore = {}
    previdx = 0
    for idx in props_idx_lst:
      pmore[props_ridx[previdx]] = hrdoctext[previdx : idx].strip()
      previdx = idx
    #print 'info: ', pmore
    if len(pmore) == 0:
      continue
    p = {}
    p['file'] = path
    p['name'] = pmore['Directive'].replace('Directive', '').replace('The', '').strip()
    if 'Default' in pmore:
      p['default'] = pmore['Default'].replace('Default:', '').strip()
    if 'Syntax' in pmore:
      p['syntax'] = pmore['Syntax'].replace('Syntax', '').strip()
    # print p
    pset.append(p)
  print len(pset)
  return pset

"""
It rocks, currently, it works for 2.2.10, 2.4.2, and 2.4.7
"""
def getConfigInfo(dir_path, v2 = True):
  apset = []
  fl = os.listdir(dir_path)
  for f in fl:
    if (f.endswith('html') and f + '.en' not in fl) or (f.endswith('html.en')):
      pset = getParamsFromHTML(os.path.join(dir_path, f)) if v2 else getParamsFromOldHTML(os.path.join(dir_path, f))  
      for p in pset:
        apset.append(p)
    else:
      pass
  return apset

def getModules(plst):
  """
  Return the modules from the entire plst
  """
  modset = []
  for p in plst:
    modhtml = os.path.basename(p['file'])
    mod = modhtml[:modhtml.find('.html')]
    if mod not in modset:
      modset.append(mod)
  return modset

#getParametersHTML('/media/tianyin/TOSHIBA EXT/software/httpd-dist/httpd-2.4.7/docs/manual/mod/core.html.en')
pset = getConfigInfo('/media/tianyin/TOSHIBA EXT/software/httpd-dist/httpd-2.0.42/docs/manual/mod/')
print len(pset)
#print getModules(pset)
#print len(getConfigInfo('/media/tianyin/TOSHIBA EXT/software/httpd-dist/httpd-2.4.2/docs/manual/mod/'))
#print len(getConfigInfo('/media/tianyin/TOSHIBA EXT/software/httpd-dist/httpd-2.4.7/docs/manual/mod/'))

#getParamsFromOldHTML('/media/tianyin/TOSHIBA EXT/software/httpd-dist/apache_1.3.0/htdocs/manual/mod/core.html')
#getParamsFromOldHTML('/media/tianyin/TOSHIBA EXT/software/httpd-dist/apache_1.3.0/htdocs/manual/mod/mod_setenvif.html')
#getConfigInfo('/media/tianyin/TOSHIBA EXT/software/httpd-dist/apache_1.3.42/htdocs/manual/mod/', False)
#getParamsFromOldHTML('core_hr.html')

