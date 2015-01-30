import sys
sys.path.append('..')
from cha import SVNCha

httpdcha = SVNCha()
httpdcha.parse('commit.log')
httpdcha.getplist('httpd.p.all')
#httpdcha.print2csv(httpdcha.charepo, 'overall.csv')
res = httpdcha.select(httpdcha.charepo, ['config'] + httpdcha.plist)
httpdcha.print2csv(res, 'httpd.git.cha.csv')