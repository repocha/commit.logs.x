import sys
sys.path.append('..')
from cha import GitCha
import subprocess
import os
import re

#REPO = '/home/tianyin/hadoop-trunk/hadoop'
REPO = '/home/tianyin/httpd-trunk/httpd'
CLOG = 'aaa.commit.log'

logstmts = ['ap_log_perror',
            'ap_log_error',
            'ap_log_rerror',
            'ap_log_cerror',
            'ap_log_cserror'
           ]

def show_commit_code(commit):
  cmd = ['git', '-C', REPO, 'show', commit]
  process = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE) 
  out, err = process.communicate()
  return out, err

gitcha = GitCha()
gitcha.parse(CLOG)
print len(gitcha.charepo)

i = 0
for c in gitcha.charepo:
  commit = c['version']
  out, err = show_commit_code(commit)
  for logstmt in logstmts:
    if logstmt in out:
      #print c['changes']
      i += 1
      op = os.path.join('httpd_commits', str(i))
      with open(op, 'w') as f:
        f.write(out)
      #print commit
      break
print '# selected commits:', i
  #if 'throw new AccessControlException' in out:
  #  print c['changes']
  
