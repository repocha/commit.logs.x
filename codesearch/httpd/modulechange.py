import os
import subprocess

SW_REPO = '/media/tianyin/TOSHIBA EXT/software/httpd-dist/'
MOD_STD = 'src/modules/standard/'

authmods = ['mod_access.c',
            'mod_actions.c',
            'mod_auth_anon.c',
            'mod_auth.c',
            'mod_auth_db.c',
            'mod_auth_dbm.c',
            'mod_digest.c']

LOG_STMT = ['ap_log_perror',
            'ap_log_error',
            'ap_log_rerror',
            'ap_log_cerror',
            'ap_log_cserror'
           ]

def get13s():
  res = []
  sort = []
  for fn in os.listdir(SW_REPO):
    if 'apache_1.3.' in fn:
      sort.append(int(fn.replace('apache_1.3.', '')))
  sort = sorted(sort)
  for n in sort:
    res.append('apache_1.3.' + str(n))
  return res

def listdiff(l1, l2):
  for e in l2:
    if e not in l1:
      print '+', e
  for e in l1:
    if e not in l2:
      print '-', e

def getmods(dp):
  res = []
  for fn in os.listdir(dp):
    res.append(fn)
  return res

def moddiff():
  lastmods = None
  currentmods = None
  for version in get13s():
    dp = os.path.join(SW_REPO, version, MOD_STD)
    currentmods = getmods(dp)
    if lastmods != None:
      print version
      listdiff(lastmods, currentmods)
    lastmods = currentmods

def getdiffstr(fp1, fp2):
  cmd = ['diff', '-u', fp1, fp2]
  process = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE) 
  out, err = process.communicate()
  return out, err

def codediff():
  lastversion = None
  for version in get13s():
    if lastversion != None: 
      for am in authmods:
        curr_mp = os.path.join(SW_REPO, version, MOD_STD, am)
        if os.path.exists(curr_mp) == False:
          print 'ERROR'
        last_mp = os.path.join(SW_REPO, lastversion, MOD_STD, am)

        print curr_mp

        out, err = getdiffstr(last_mp, curr_mp)
        hit = False
        for logstmt in LOG_STMT:
          if logstmt in out:
            hit = True
            break
        #write into files
        if hit == True:
          with open(os.path.join('httpd-mod-1.3', version), 'w') as outf:
            outf.write(out)
    lastversion = version

#moddiff()
codediff()
