import csv

class BaseParser:
  """The base class for commit log analysis
  """
  
  def __init__(self):
    self.cmts = []

  def parse(self, cmtlog_fp):
    """The general parser that split all the cmt logs
    """
    pass;

  def select(self, kws, pop=100):
    """Given a list of keywords, return the commits that contains all the keywords
    """
    res = []
    kwcount = {}
    for cmt in cmts:
      count = 0
      for kw in kws:
        kwl = kw.lower()
        msg = cmt['message'].lower()
        if msg.find(kwl) != -1:
          count += 1
          if kw not in kwcount:
            kwcount[kw] = 1
          else:
            kwcount[kw] += 1
          if count > 0:
            res.append(cmt)
    print '-----------------------------------------------------------------------------'
    print 'The too popular keywords (count >= 50): '
    print '(perhaps we need to comment them out)'
    for kw in kwcount:
      if kwcount[kw] >= pop:
        print kw, kwcount[kw]
    print '-----------------------------------------------------------------------------'
    print 'Number of commits we select out:'
    print len(res)
    print '-----------------------------------------------------------------------------'
    return res

  def message2csv(self, outputfile):
    with open(outputfile, 'wb') as f:
      writer = csv.writer(f, delimiter='\t')
      for cmt in cmts:
        writer.writerow([cmt['commitno'], cmt['message']])

  def printN(self, N=2):
    print '#commits:', len(self.cmts)
    for i in range(N):
      print 'no.', i, self.cmts[i] 
    print '......'
    print 'no.', len(self.cmts)-1, self.cmts[-1]

