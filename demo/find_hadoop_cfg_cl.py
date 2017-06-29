import sys
sys.path.append('..')
from git_parser import GitParser

"""In this demo, we want to find all the commit logs 
that contain at least one Hadoop config parameter
"""

def getparams(plfp):
  plist = []
  with open(plfp) as f:
    for p in f:
      p = p.strip()
      if p not in plist:
        plist.append(p)
  return plist

gitp = GitParser('hadoop')
gitp.parse('../data/hadoop.git.log')
pl = getparams('hadoop.param.lst')
for cmt in gitp.kwselect(pl):
  print cmt
