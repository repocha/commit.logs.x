import sys,os
sys.path.append('..')
from git_parser import GitParser
from datetime import datetime

"""
print the stats of the commit logs
"""

def __parsetimestr(date_str):
  naive_date_str, _, offset_str = date_str.rpartition(' ')
  naive_dt = datetime.strptime(naive_date_str, '%a %b %d %H:%M:%S %Y')
  return naive_dt

def __gettimestr(timestr):
  return __parsetimestr(timestr).strftime("%Y-%m-%d")

def __num_contributors(cmts):
  contrib = set([])
  for cmt in cmts:
    contrib.add(cmt['author'])
  return len(contrib)

"""
def gen_cmtlogs(repos_dir):
  for repop in os.listdir(repos_dir):
    repofp = os.path.join(repos_dir, repop)
    cmtlogfp = 'commit.logs_dir/' + repop + '.log'
    if os.path.exists(cmtlogfp) == False:
      os.system('bash git_log.sh ' + repofp + ' ' + cmtlogfp) 
"""

def repo_stats(gitps):
  for r in gitps:
    p = gitps[r]
    print r, len(p.cmts), __num_contributors(p.cmts), __gettimestr(p.latest_cmt()['date'])

if __name__ == "__main__":
  gitps = {}
  cmtlogs_dir = 'commit.logs_dir'
  for cmtlog in os.listdir(cmtlogs_dir):
    cmtlogfp = os.path.join(cmtlogs_dir, cmtlog)
    gitp = GitParser(cmtlog[:-4])
    gitp.parse(cmtlogfp)
    gitps[cmtlog[:-4]] = gitp
  repo_stats(gitps)
