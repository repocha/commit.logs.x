
DATASET  = 'apache-2.2-deny_closed_urls'
STUDIED1 = 'studied.lst'
STUDIED2 = 'studied.2.lst'
IRRELEVT = 'irrelevant.lst'

def read2lst(fpath):
  res = []
  with open(fpath) as f:
    for l in f:
      res.append(l.strip())
  return res

study1 = read2lst(STUDIED1)
study2 = read2lst(STUDIED2)
irrelt = read2lst(IRRELEVT)

std1cnt = 0
std2cnt = 0
irrecnt  = 0

dataset = []
with open(DATASET) as f:
  for l in f:
    e = {}
    url = l.strip()
    e['url'] = url
    if url in study1:
      e['flg'] = 'study1'
      std1cnt += 1
    elif url in study2:
      e['flg'] = 'study2'
      std2cnt += 1
    elif url in irrelt:
      e['flg'] = 'irrelt'
      irrecnt += 1
    else:
      e['flg'] = 'new'
    dataset.append(e)

print len(dataset)
print 'IRRV CNT: ', irrecnt
print 'STD1 CNT: ', std1cnt
print 'STD2 CNT: ', std2cnt

cnt = 0
for row in dataset:
  cnt += 1  
  print row['url'] + ',' + row['flg'] + ',' + str(cnt)
