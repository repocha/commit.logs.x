import csv

class BaseParser:
  """The base class for commit log analysis
  """
  
  def __init__(self, name):
    self.repo_name = name
    self.cmts = []

  def parse(self, cmtlog_fp):
    """The general parser that split all the cmt logs
    """
    pass;

  def message2csv(self, outputfile):
    with open(outputfile, 'wb') as f:
      writer = csv.writer(f, delimiter='\t')
      for cmt in cmts:
        writer.writerow([cmt['commitno'], cmt['message']])

  def latest_cmt(self):
    return self.cmts[0]

  def printN(self, N=2):
    print '-----------------------------'
    print '#commits:', len(self.cmts)
    print '-----------------------------'
    for i in range(N):
      #print i, '| revno.', self.cmts[i]['commitno'], '| msg:', self.cmts[i]['message'] 
      print i, self.cmts[i] 
    print '......'
    #print len(self.cmts)-1, '| revno', self.cmts[-1]['commitno'], '| msg:', self.cmts[-1]['message']
    print len(self.cmts)-1, self.cmts[-1]
    print '-----------------------------'

  def kwselect(self, kws, pop=0.1):
    """Given a list of keywords, return the commits that contains all the keywords
       For more complicated filter, use kwfilter
    """
    res = []
    kwmap = {}
    for cmt in self.cmts:
      contains = False
      for kw in kws:
        kwl = kw.lower()
        msg = cmt['message'].lower()
        if kwl in msg:
          contains = True
          if kw not in kwmap:
            kwmap[kw] = 1
          else:
            kwmap[kw] += 1
      if contains == True:
        res.append(cmt)
    print '-----------------------------------------------------------------------------'
    print 'The too popular keywords (count >= 50): '
    print '(perhaps we need to comment them out)'
    for kw in kwmap:
      if kwmap[kw] >= pop * len(self.cmts):
        print kw, kwmap[kw]
    print '-----------------------------------------------------------------------------'
    print 'Number of commits we select out:'
    print len(res)
    print '-----------------------------------------------------------------------------'
    return res
