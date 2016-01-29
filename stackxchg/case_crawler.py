import sys
sys.path.insert(0, '..')
import os
from crawler import crawl
from crawler import URLCrawler
import config

SECTION = 'tagged_url_crawler'
conf = config.getconfig()

url_list = conf.get(SECTION, 'post_list')
case_dir_template = conf.get(SECTION, 'case_dir_template')

#URL_LIST = 'serverfault_tags_postgresql_questions.lst'
#CASE_DIR = '/media/tianyin/TOSHIBA EXT/tixu_old/xuepeng/iconfigure/everything_about_postgresql'

rawtag = raw_input('Enter the tag name: ')

tags = []
if '*' in rawtag:
  key = rawtag.replace('*', '')
  for f in os.listdir('.'):
    if 'serverfault_tags_' in f and '_questions.lst' in f and key in f:
      tags.append(f.replace('serverfault_tags_', '').replace('_questions.lst', ''))
  print tags
else:
  tags.append(rawtag)

for tag in tags:
  case_dir = case_dir_template.replace('TAG', tag) 
  if os.path.exists(case_dir) == False:
    os.makedirs(case_dir)
  print 'Download to', case_dir

  urls = []
  with open(url_list.replace('TAG', tag)) as f:
    for l in f:
      urls.append(l.strip())

  crawler = URLCrawler(urls, case_dir, None)
  crawler.calibrate()
  crawler.crawl()
  print 'FINISH CRAWLING TAG \'' + tag + '\''
