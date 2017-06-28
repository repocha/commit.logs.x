import sys
sys.path.append('..')
from git_parser import GitParser

def getparams(plfp):
  plist = []
  with open(plfp) as f:
    for p in f:
      p = p.strip()
      if p not in plist:
        plist.append(p)
  return plist

gitp = GitParser()
gitp.parse('../data/hadoop.git.log')
pl = getparams('hadoop.param.lst')
for cmt in gitp.select(pl):
  print cmt
