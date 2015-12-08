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
      print '-------------------------------------------------'
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
      print p
      pset.append(p)
  except Exception as e:
    print '[ERROR] parse error', e
    pass
  return pset    


"""
At least works for 2.4.7 
"""
def getConfigInfo(dir_path):
  apset = []
  fl = os.listdir(dir_path)
  for f in fl:
    if (f.endswith('html') and f + '.en' not in fl) or (f.endswith('html.en')):
      pset = getParamsFromHTML(os.path.join(dir_path, f))  
      for p in pset:
        if p not in apset:
          apset.append(p)
        else: 
          print '[ERROR] p already exists', p
    else:
      pass
  return apset

#getParametersHTML('/media/tianyin/TOSHIBA EXT/software/httpd-dist/httpd-2.4.7/docs/manual/mod/core.html.en')
getConfigInfo('/media/tianyin/TOSHIBA EXT/software/httpd-dist/httpd-2.4.2/docs/manual/mod/')
