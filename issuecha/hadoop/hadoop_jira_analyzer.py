import sys
sys.path.append('..')
import jiraparser
import os 

CONFIG_KW = [
        'config', 
        'option',
        'propert'
        ]

def filter(jira, keywords = CONFIG_KW):
  """
  return whether the jira contains the predefined keywords
  """
  for kw in keywords:
    if jira['title'].lower().find(kw) != -1:
      return True
    if 'summary' in jira and jira['summary'].lower().find(kw) != -1:
      return True
  #none of the keywords is found
  return False 

def dfilter(dirp):
  js = []
  for f in os.listdir(dirp):
    fp = os.path.join(dirp, f)
    jira = jiraparser.parse(fp)
    if jira != None and filter(jira) == True:
      print jira['title']
      #if 'summary' in jira:
      #  print jira['summary']
      js.append(jira)
  return js


js = dfilter('/media/tianyin/TOSHIBA EXT/tixu_old/longjin/hadoop-jira/FLUME-/')
print len(js)
