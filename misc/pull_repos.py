import sys,os

def __loadfile(fp): 
  with open(fp) as f:
    return f.read().splitlines()

def __genname(repo_url):
  """git://github.com/domain/repo_name.git"""
  return repo_url.replace('.git','').replace('git://github.com/', '').replace('/', '.')  

def pull_github_repos(repos_fp, destdir):
  if os.path.isdir(destdir) == False:
    print '[info] create', destdir
    os.mkdir(destdir)
  for gitrepo in __loadfile(repos_fp):
    dest = os.path.join(destdir, __genname(gitrepo))
    if not os.path.exists(dest):
      os.system("git clone " + gitrepo + " " + dest)
    else:
      print '[error] repeated repo:', gitrepo


pull_github_repos('repos_no_check_301.lst', '/home/tianyin/exp_repos/')
