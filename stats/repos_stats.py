import sys,os
sys.path.append('..')
from git_parser import GitParser
from datetime import datetime

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

def repo_stats(repos_dir):
  for repop in os.listdir(repos_dir):
    repofp = os.path.join(repos_dir, repop)
    cmtlogfp = 'cmtlogs/' + repop + '.log'
    if os.path.exists(cmtlogfp) == False:
      os.system('bash git_log.sh ' + repofp + ' ' + cmtlogfp) 
    gitp = GitParser()
    gitp.parse(cmtlogfp)
    print repop, len(gitp.cmts), __num_contributors(gitp.cmts), __gettimestr(gitp.latest_cmt()['date'])

repo_stats('/home/tianyin/exp_repos')
