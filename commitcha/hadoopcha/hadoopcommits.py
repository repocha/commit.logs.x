import sys
sys.path.append('../..')
from cha import GitCha
import subprocess
import os
import re

class HadoopCha(GitCha):
  """
  The input file should be generated using git log --name-status
  """
  def selectxml(self):
    res = []
    for cha in self.charepo:
      if 'chfiles' not in cha:
        #print cha
        return
      hit = False
      for f in cha['chfiles']:
        if f.endswith('default.xml') == True and f.endswith('pom.xml') == False:
          hit = True
          break
      if hit == True:
        res.append(cha)
    return res

  def chaShow(self, commit, repopath):
    cmd = ['git', '-C', repopath, 'show', commit]
    process = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE) 
    out, err = process.communicate()
    return out, err

def getJIRAInCommits():
  commitj = {}
  prefix = ['HDFS', 'MAPREDUCE', 'HADOOP', 'YARN', 'MR']
  delims = [' ', '.', ':', ',', '/', '@', ')', ']', '"', '\'', '(']
  hadoopCha = HadoopCha() 
  hadoopCha.parse('hadoop.log.name-status')
  for cha in hadoopCha.charepo:
    hasJIRA = False
    #print cha['version'], cha['changes'], len(cha['chfiles'])
    for pfx in prefix:
      if cha['changes'].find(pfx):
        hasJIRA = True
        break
    if hasJIRA == False:
      print 'This commit does not has JIRA NO.:', cha['changes']
    jiras = [] 
    for pfx in prefix:
      chg = cha['changes']
      while chg.find(pfx) != -1:
        if pfx in chg:
          jirano = chg[chg.find(pfx) : ]
          for delim in delims:
            if jirano.find(delim) != -1:
              jirano = jirano[ : jirano.find(delim)]
          if not re.match('^[A-Z]*\-[0-9]*$', jirano):
            print 'INVALID JIRA: ', jirano
          #print jirano, ' | ', chg
          elif jirano not in jiras:
            jiras.append(jirano)
          chg = chg.replace(pfx, '', 1)
    commitj[cha['version']] = jiras
    if len(jiras) == 0:
      print 'COMMIT W/O JIRA: ', cha['changes']
  return commitj

#for j in getJIRAInCommits():
#  print j

def checkJIRAPages():
  """
  Check if the commit log is corresponding to a JIRA#
  """
  JIRA_PAGE_DIR = '/media/tianyin/TOSHIBA EXT/tixu_old/longjin/hadoop-jira/pages'
  cmap = getJIRAInCommits()
  print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
  for commit in cmap:
    for jn in cmap[commit]:
      jnp = os.path.join(JIRA_PAGE_DIR, jn)
      if os.path.exists(jnp) == False:
        print 'NOT CRAWLED: ', jn
      elif os.stat(jnp).st_size == 0:
        print 'CORRUPTED: ', jnp


def splitCommit(commitLog):
  """
  Split a commit log into per-file structure
  """
  started  = False
  filecha  = {}
  lastkey  = ''
  lastcntt = ''
  for line in commitLog.splitlines():
    if line.startswith('diff'):
      if ' --git ' not in line:
        raise ValueError('ERROR: starting with \'diff\' but not having \'--git\': ' + line)
      fc = line.replace('diff', '').replace(' --git ', '').strip()
      if started:
        filecha[lastkey] = lastcntt
      else:
        started = True
      lastcntt = ''
      lastkey = fc
    else:
      lastcntt += line + '\n'
  if started:
    filecha[lastkey] = lastcntt
  return filecha


def recordDefXmlCha():
  """
  generate a dump recording the changes of the default xmls
  """
  chas = []
  hadoopCha = HadoopCha()
  hadoopCha.parse('hadoop.log.name-status')
  chalst = hadoopCha.selectxml()
  for cha in chalst:
    rescha = {}
    xmls = []
    for f in cha['chfiles']:
      if f.endswith('-default.xml'):
        xmls.append(f)
    if len(xmls) > 0:
      #print cha['version'], cha['changes'], len(xmls)
      rescha['commit'] = cha['version']
      rescha['summary'] = cha['changes']
      rescha['date'] = cha['date']
      rescha['xmls'] = xmls
      out, err = hadoopCha.chaShow(cha['version'], '/home/tianyin/hadoop')
      filecha = splitCommit(out)
      rescha['changes'] = filecha
      chas.append(rescha)
  return chas

def getChaType(filecha):
  add = False
  rmv = False
  for line in filecha.splitlines():
    if line.startswith('+++') or line.startswith('---'):
      continue
    if line.startswith('+'):
      add = True
    elif line.startswith('-'):
      rmv = True
    else:
      pass
  if add and rmv:
    return 'R'
  elif add and rmv == False:
    return 'A'
  elif add == False and rmv:
    return 'M'


def dumpDefXmlCha(chas, xmlname):
  cnt = 0
  for cha in chas:
    contains = False
    filecha = cha['changes']
    for f in filecha:
      if f.endswith(xmlname) and getChaType(filecha[f]) == 'R':
        contains = True
        break
    if contains:
      cnt += 1
      print '=================================================================='
      print cha['commit']
      print '------------------------------------------------------------------'
      print cha['summary']
      print cha['date']
      print '=================================================================='
      for f in filecha:
        if f.endswith(xmlname) and getChaType(filecha[f]) == 'R':
          print filecha[f]
  print cnt


#checkJIRAPages()
dumpDefXmlCha(recordDefXmlCha(), 'hdfs-default.xml')

#hadoopCha = HadoopCha()
#out, err = hadoopCha.chaShow('bf6aa30a156b3c5cac5469014a5989e0dfdc7256', '/home/tianyin/hadoop')
#print out
#print splitCommit(out) 
