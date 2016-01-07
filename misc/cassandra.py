import yaml

cnt = 0
srcconf = {}
f = open('/home/tianyin/cassandra/src/java/org/apache/cassandra/config/Config.java', 'r')
for l in f:
  l = l.strip()
  if '=' in l and 'public' in l:
    #print l
    cnt += 1
    pl = l.split('=')
    decl = pl[0].strip()
    name = decl[decl.rfind(' ') : ].strip()
    defv = pl[1].strip()
    defv = defv[ : defv.rfind(';')]
    print name, defv
    srcconf[name] = defv
print cnt

print '-------------------------------------------------------------'
flconf = yaml.load(open('/home/tianyin/cassandra/conf/cassandra.yaml').read())
for p in flconf:
  if p not in srcconf:
    print 'VALUE MISSING IN SRC: ', p
  else:
    srcv = srcconf[p]
    flev = flconf[p]
    if srcv.endswith('L'):
      srcv = srcv[: -1]
    if srcv == 'true':
      srcv = 'True'
    if srcv == 'false':
      srcv = 'False'
    if str(srcv) != str(flev):
      print 'INCONSISTENT: ', p, srcv, '<>', flev
      
