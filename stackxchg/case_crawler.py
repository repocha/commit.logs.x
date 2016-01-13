import sys

sys.path.insert(0, '..')
from crawler import crawl
from crawler import URLCrawler

URL_LIST = 'serverfault_tags_postgresql_questions.lst'
CASE_DIR = '/media/tianyin/TOSHIBA EXT/tixu_old/xuepeng/iconfigure/everything_about_postgresql'

urls = []
with open(URL_LIST) as f:
  for l in f:
    urls.append(l.strip())

crawler = URLCrawler(urls, CASE_DIR, None)
#crawler.calibrate()
crawler.crawl()
