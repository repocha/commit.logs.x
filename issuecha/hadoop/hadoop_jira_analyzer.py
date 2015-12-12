import hadoop_jira_parser
import os 

CONFIG_KW = [
        'config', 
        'option',
        'propert'
        ]

def filter(jira, keywords = CONFIG_KW):
  """
  Return whether the jira contains the predefined keywords
  """
  for kw in keywords:
    if jira['title'].lower().find(kw) != -1:
      return True
    if 'summary' in jira and jira['summary'].lower().find(kw) != -1:
      return True
  #none of the keywords is found
  return False 

def dfilter(dirp, paramspath, output):
  """
  Get config-related JIRAs and print to a CSV
  """
  js = []
  # build keywords
  kws = []
  for kw in CONFIG_KW:
    kws.append(kw)
  pf = open(paramspath, 'r')
  for p in pf:
    kws.append(p.strip().lower())
  print len(kws)
  pf.close() 
  for f in os.listdir(dirp):
    fp = os.path.join(dirp, f)
    jira = hadoop_jira_parser.parse(fp)
    if jira != None and filter(jira, kws) == True:
      print f, jira['title'], jira['summary']
      #if 'summary' in jira:
      #  print jira['summary']
      js.append(jira)
  return js

js = dfilter('/media/tianyin/TOSHIBA EXT/tixu_old/longjin/hadoop-jira/YARN-/', 
             '/home/tianyin/confcha/doccha/hadoop/params.list')
print len(js)
