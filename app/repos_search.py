import sys,os
sys.path.append('..')
from git_parser import GitParser
from kwfilter import KWFilter
from kwfilter import parser_filter_by_chfiles
from kwfilter import parser_filter_by_msg

"""
def gen_cmtlogs(repos_dir):
  for repop in os.listdir(repos_dir):
    repofp = os.path.join(repos_dir, repop)
    cmtlogfp = 'commit.log_dir/' + repop + '.log'
    if os.path.exists(cmtlogfp) == False:
      os.system('bash git_log.sh ' + repofp + ' ' + cmtlogfp) 
"""

def chfile_hunter(gitps, kwfilt):
  """select commits based on the files that the commits touch
  """
  res = []
  cnt = 0
  for r in gitps:
    p = gitps[r]
    np = parser_filter_by_chfiles(p, kwfilt, True)
    if len(np.cmts) > 0:
      res.append(np)
    for cmt in np.cmts:
      print np.repo_name + ',https://github.com/' + np.repo_name.replace('.', '/') + '/commit/' + cmt['commitno'] + ',\"' + cmt['message'] + '\",' + ';'.join(cmt['chfiles'])
      cnt += 1
  print 'count: ', cnt
  return res 

def msg_hunter(gitps, kwfilt):
  """select commits based on the message of the commits
  """
  res = []
  cnt = 0
  for r in gitps:
    p = gitps[r]
    np = parser_filter_by_msg(p, kwfilt)
    if len(np.cmts) > 0:
      res.append(np)
    for cmt in np.cmts:
      print np.repo_name + ',https://github.com/' + np.repo_name.replace('.', '/') + '/commit/' + cmt['commitno'] + ',\"' + cmt['message']
      cnt += 1
  print 'count: ', cnt
  return res 

if __name__ == "__main__":
  gitps = {}
  cmtlogs_dir = 'commit.logs_dir'
  for cmtlog in os.listdir(cmtlogs_dir):
    cmtlogfp = os.path.join(cmtlogs_dir, cmtlog)
    gitp = GitParser(cmtlog[:-4])
    gitp.parse(cmtlogfp)
    gitps[cmtlog[:-4]] = gitp

  """
  #search the change files
  cs = [
         ['check', '.xml'],   
         ['style', '.xml'], 
       ]
  #cs = [['checkstyle', '.xml']]
  kwfilt = KWFilter(cs)
  print len(chfile_hunter(gitps, kwfilt))
  """

  #search the commit logs
  cs = [['check', 'style']]
  with open('kw.checks.lst') as f:
    for l in f:
      l = l.strip()
      if l.startswith('#') == False:
        cs.append(l.split(' '))
  kwfilt = KWFilter(cs)
  msg_hunter(gitps, kwfilt)
  kwfilt.print_kw_matches()
