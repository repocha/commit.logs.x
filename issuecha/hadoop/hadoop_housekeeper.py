import os
from lxml import etree
from lxml.html import fromstring
from lxml.html import tostring
import lxml.html as lh
from io import StringIO, BytesIO

prefix = 'HADOOP'
dirp = '/media/tianyin/TOSHIBA EXT/tixu_old/longjin/hadoop-jira/' + prefix + '-/'
components = ['HDFS', 'MAPREDUCE', 'YARN']
cnt = 0
for f in os.listdir(dirp):
  title = None
  fp = os.path.join(dirp, f)
  fd = open(fp)
  html = fd.read()
  fd.close()
  doc = fromstring(html)
  for title in doc.iter('title'):
    title = title.text_content().strip()
  if title == None:
    print f
  if title.find('[') == -1 or title.find(']') == -1:
    print f, title
    continue
  jirano = title[ title.find('[') + 1 : title.find(']') ]
  for c in components:
    if jirano.startswith(c):
      print f, '>>>', jirano
    else:
      cnt += 1
print '#TRUE CASES: ', cnt
