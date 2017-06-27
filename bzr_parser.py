from base_parser import BaseParser

class BazaarParser(BaseParser):
  """for Bazaar
  """
  def parse(self, cmtlog):
    with open(cmtlog) as f:
      revno = ''
      message = ''
      for line in f:
        line = line.strip()
        if line.startswith('------------------------------------------------------------'):
          #Handle the old ones
          if len(revno) > 0:
            cmt = {}
            cmt['commitno'] = revno
            cmt['message'] = message
            self.cmts.append(cmt)
          #Reset
          revno = ''
          message = ''
        elif line.startswith('revno:'):
          revno = line.replace('revno:', '').strip()
        elif line.startswith('committer:'):
          pass
        elif line.startswith('author:'):
          pass
        elif line.startswith('From:'):
          pass
        elif line.startswith('branch'):
          pass
        elif line.startswith('timestamp:'):
          pass
        elif line.startswith('date:'):
          pass
        elif line.startswith('message:'):
          message = line.replace('message:', '').strip()
        else:
          #if line.find(': ') != -1:
          #    print line
          message += ' ' + line
      self.printN()

