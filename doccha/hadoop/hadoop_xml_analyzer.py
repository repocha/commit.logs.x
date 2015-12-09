import os
from lxml import etree
from lxml.html import fromstring
import lxml.html as lh
import csv
import subprocess
import os
import fnmatch

def findDefaultXML(repop):
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

#getVersion('deprec.csv', './hadoop-release-file.csv', '', 2)

#getAllDiff('./hadoop-release-file.csv', 'dfs', 1)
#getAllDiff('./hadoop-release-file.csv', 'mapred', 2)

#    xml = f.read()
#    f.close()
#    doc = etree.fromstring(path)
#    pset = []
#    ntags = doc.xpath('//configuration/property/name')
#    for n in ntags:
#        print n.text

#for i in xrange(1,20):
#    pset = getParametersHTML('/home/tixu/software/hadoop-dist/hadoop-0.' + str(i) + '.0/docs/hadoop-default.html')
#    if 'fs.checkpoint.period' in pset:
#        print i 

#getParametersHTML('/home/tixu/software/hadoop-before-2009/hadoop-0.2.0/docs/hadoop-default.html')
#getParametersHTML('/home/tixu/software/hadoop-before-2009/hadoop-0.3.0/docs/hadoop-default.html')
#getParametersHTML('/home/tixu/software/hadoop-before-2009/hadoop-0.4.0/docs/hadoop-default.html')
#getParametersHTML('/home/tixu/software/hadoop-before-2009/hadoop-0.5.0/docs/hadoop-default.html')
#getParametersHTML('/home/tixu/software/hadoop-before-2009/hadoop-0.6.0/docs/hadoop-default.html')
#getParametersHTML('/home/tixu/software/hadoop-before-2009/hadoop-0.7.0/docs/hadoop-default.html')
#getParametersHTML('/home/tixu/software/hadoop-before-2009/hadoop-0.8.0/docs/hadoop-default.html')
#s1 = getParametersHTML('/home/tixu/software/hadoop-dist/hadoop-1.2.1/docs/hdfs-default.html')

#set1 = getParametersXML('/home/tixu/software/hadoop-dist/hadoop-0.1.0/conf/hadoop-default.xml')
#set2 = getParametersXML('/home/tixu/software/hadoop-dist/hadoop-0.2.0/conf/hadoop-default.xml')
#s2 = getParametersXML('/home/tixu/software/hadoop-dist/hadoop-1.2.1/src/hdfs/hdfs-default.xml')

#s1 = getParametersXML('/home/tixu/software/hadoop-dist/hadoop-2.2.0-src//hadoop-mapreduce-project/hadoop-mapreduce-client/hadoop-mapreduce-client-core/src/main/resources/mapred-default.xml', '')
#s2 = getParametersXML('/home/tixu/software/hadoop-dist/hadoop-2.2.0-src/hadoop-hdfs-project/hadoop-hdfs/src/main/resources/hdfs-default.xml', '')

#for p in s1:
#    print p

#pset = parseXML('/home/tixu/software/hadoop-dist/hadoop-2.2.0-src/hadoop-hdfs-project/hadoop-hdfs/src/main/resources/hdfs-default.xml')
#pset = parseXML('/home/tixu/software/hadoop-dist/hadoop-2.2.0-src//hadoop-mapreduce-project/hadoop-mapreduce-client/hadoop-mapreduce-client-core/src/main/resources/mapred-default.xml')

#pset = parseXML('/home/tixu/software/hadoop-dist/hadoop-2.2.0-src/hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common/src/main/resources/yarn-default.xml')
pset = getParamsFromXML('/media/tianyin/TOSHIBA EXT/software/hadoop-dist/hadoop-2.2.0-src/hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common/src/main/resources/yarn-default.xml')
for p in pset:
  print p

for f in findDefaultXML('/media/tianyin/TOSHIBA EXT/software/hadoop-dist/hadoop-2.2.0-src/'):
  print f

#print len(s1)
#print len(s2)
#psetDiff(s1, s2)
#psetDiff(set2, set3)

#print '--------------------------------------------------------------------------------------'

#getParametersXML('/home/tixu/software/hadoop-before-2009/hadoop-0.3.0/conf/hadoop-default.xml')
#getParametersXML('/home/tixu/software/hadoop-before-2009/hadoop-0.4.0/conf/hadoop-default.xml')
#getParametersXML('/home/tixu/software/hadoop-before-2009/hadoop-0.5.0/conf/hadoop-default.xml')
#getParametersXML('/home/tixu/software/hadoop-before-2009/hadoop-0.6.0/conf/hadoop-default.xml')
#getParametersXML('/home/tixu/software/hadoop-before-2009/hadoop-0.7.0/conf/hadoop-default.xml')
#getParametersXML('/home/tixu/software/hadoop-before-2009/hadoop-0.8.0/conf/hadoop-default.xml')
#getParametersXML('/home/tixu/software/hadoop-before-2009/hadoop-0.9.0/conf/hadoop-default.xml')
#getParametersXML('/home/tixu/software/hadoop-before-2009/hadoop-0.23.10-src/hadoop-hdfs-project/hadoop-hdfs/src/main/resources/hdfs-default.xml')
#getParametersXML('/home/tixu/software/hadoop-trunk/hadoop-hdfs-project/hadoop-hdfs/src/main/resources/hdfs-default.xml')
