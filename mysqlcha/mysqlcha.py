import sys
sys.path.append('..')
from cha import GitCha

mysqlcha = GitCha()
mysqlcha.parse('mysql.git.log')
mysqlcha.getplist('mysql.p.all.2')
res = mysqlcha.select(mysqlcha.charepo, ['config'] + mysqlcha.plist)
mysqlcha.print2csv(res, 'mysql.git.cha.csv.2')
