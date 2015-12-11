import sys
sys.path.append('..')
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
        print cha
        return
      hit = False
      for f in cha['chfiles']:
        if f.endswith('default.xml'): # == True and f.endswith('pom.xml') == False:
          hit = True
          break
      if hit == True:
        res.append(cha)
    return res

  def pcha(self, chalst, repopath):
    for cha in chalst:
      commit = cha['version']
      cmd = ['git', '-C', repopath, 'show', commit]
      process = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE) 
      out, err = process.communicate()
      print commit
      print cha['changes']
      print out
      # get the diff using git show commitno
      # append in a file

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
          if not re.match('^[A-Z0-9\-]*$', jirano):
            print 'INVALID JIRA: ', jirano
          #print jirano, ' | ', chg
          if jirano not in jiras:
            jiras.append(jirano)
          chg = chg.replace(pfx, '', 1)
    commitj[cha['version']] = jiras
    if len(jiras) == 0:
      print 'COMMIT W/O JIRA: ', cha['changes']
  return commitj

#for j in getJIRAInCommits():
#  print j

def checkJIRAPages():
  print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
  JIRA_PAGE_DIR = '/media/tianyin/TOSHIBA EXT/tixu_old/longjin/hadoop-jira/pages'
  for jn in getJIRAInCommits():
    jnp = os.path.join(JIRA_PAGE_DIR, jn)
    if os.path.exists(jnp) == False:
      print jn

checkJIRAPages()

"""
hadoopCha = HadoopCha()
hadoopCha.parse('hadoop.log.name-status')
chalst = hadoopCha.selectxml()
#hadoopCha.pcha(chalst, '/home/tianyin/hadoop')
for cha in chalst:
    isConfRelated = False
    if 'conf' in cha['changes']:
      isConfRelated = True
    for f in cha['chfiles']:
      if f.endswith('default.xml'):
        isConfRelated = True
        break
    if isConfRelated == True:
      print cha['version'], cha['changes'], len(cha['chfiles'])
"""
