import sys
sys.path.append('..')
from cha import GitCha

pgcha = GitCha()
pgcha.parse('pg.git.log')
pgcha.getplist('pg.p.all')
res = pgcha.select(pgcha.charepo, ['config'] + pgcha.plist)
pgcha.print2csv(res, 'pg.git.cha.csv')
