import re


def normalize(name, value):
  resv = value.lower()
  resv = resv.replace(name.lower(), '').replace('\t', '').replace('\r', ' ').replace('\n', ' ')
  resv = re.sub( '\s+', ' ', resv).strip()
  return resv

class ParamSet:
  """
  {
    'name'    : param name
    'default' : param default value
    'file'    : the doc file 
  }
  """
  def __init__(self):
    self.paramset = {}
    
  def addDict(self, pdict):
    """
    pset is usually a param set from one version
    """
    for p in pdict:
      if p not in self.paramset:
        self.paramset[p] = []
      self.paramset[p].append(pdict[p])

  def addList(self, plist):
    for p in plist:
      if p['name'] not in self.paramset:
        self.paramset[p['name']] = []
      self.paramset[p['name']].append(p)

  def size(self):
    return len(self.paramset)

  def validate(self):
    for pname in self.paramset:
      if ' ' in pname:
        for p in self.paramset[pname]:
          print pname
          print p['file']
          print '-------'
        
  def checkValDiff(self):
    """
    we want to know the difference between the values
    {
      'name' : param name
      {
        'default'  : param value
        ['file'] : doc
      }
    }
    """
    valdiff = {}
    for p in self.paramset:
      valdiff[p] = {}
      for pinfo in self.paramset[p]:
        if 'default' not in pinfo:
          continue
        val = pinfo['default']
        fil = pinfo['file']
        if val not in valdiff[p]:
          valdiff[p][val] = []
        valdiff[p][val].append(fil)
    return valdiff


"""
pdict = {}
p1 = {}
p1['name']  = 'p1' 
p1['value'] = 'v1'
p1['file']  = 'f1'
pdict['p1'] = p1
p2 = {}
p2['name']  = 'p2' 
p2['value'] = 'v2'
p2['file']  = 'f2' 
pdict['p2'] = p2
p3 = {}
p3['name']  = 'p3' 
p3['value'] = 'v3'
p3['file']  = 'f3'
pdict['p3'] = p3
"""
#paramset = ParamSet()
#paramset.add2set(pdict)
#vdiff = paramset.checkValDiff()
#for v in vdiff:
#  print v, vdiff[v]
