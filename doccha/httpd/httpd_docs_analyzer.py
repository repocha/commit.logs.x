import os
from lxml import etree
from lxml.html import fromstring
import lxml.html as lh
import csv

"""
This works for most new HTML manual pages
"""
def getParamsFromHTML(path):
  pset = []
  f = open(path)
  xml = f.read()
  f.close()
  doc = fromstring(xml)
  try:
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
  except Exception as e:
    print '[ERROR] parse error', e
    pass
  return pset    


"""
It rocks, currently, it works for 2.2.10, 2.4.2, and 2.4.7
"""
def getConfigInfo(dir_path):
  apset = []
  fl = os.listdir(dir_path)
  for f in fl:
    if (f.endswith('html') and f + '.en' not in fl) or (f.endswith('html.en')):
      pset = getParamsFromHTML(os.path.join(dir_path, f))  
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
pset = getConfigInfo('/media/tianyin/TOSHIBA EXT/software/httpd-dist/httpd-2.2.10/docs/manual/mod/')
print len(pset)
print getModules(pset)
#print len(getConfigInfo('/media/tianyin/TOSHIBA EXT/software/httpd-dist/httpd-2.4.2/docs/manual/mod/'))
#print len(getConfigInfo('/media/tianyin/TOSHIBA EXT/software/httpd-dist/httpd-2.4.7/docs/manual/mod/'))


