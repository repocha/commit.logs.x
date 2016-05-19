import sys
sys.path.append('..')
from cha import GitCha
import subprocess
import os
import re
import csv

def show_commit_code(commit):
  cmd = ['git', '-C', REPO, 'show', commit]
  process = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE) 
  out, err = process.communicate()
  return out, err

def select_commits(sw, commit_log, repo, signatures, outdir):
  gitcha = GitCha()
  gitcha.parse(CLOG)
  print '#commits in logs:', len(gitcha.charepo)
  i = 0
  csvf = open(sw + '_summary.csv', 'wb')
  writer = csv.writer(csvf)
  for c in gitcha.charepo:
    commit = c['version']
    out, err = show_commit_code(commit)
    for s in signatures:
      if s in out:
        i += 1
        writer.writerow([str(i),c['changes'],c['version']])
        #print c['changes']
        op = os.path.join(outdir, str(i))
        with open(op, 'w') as f:
          f.write(out)
        #print commit
        break
  print '# selected commits:', i

  #if 'throw new AccessControlException' in out:
  #  print c['changes']
  
