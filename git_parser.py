from base_parser import BaseParser

class GitParser(BaseParser):
  """for Git commit logs
  """
  def parse(self, cmtlog):
    with open(cmtlog, 'r') as f:
      revno = None
      message = ''
      author = ''
      date = None
      merge = None
      chfiles = []
      for line in f:
        if len(line.strip()) == 0:
          continue
        if line.startswith('commit '):
          if revno != None:
            cmt = {}
            cmt['commitno'] = revno
            cmt['message'] = message
            cmt['chfiles'] = chfiles
            cmt['merge'] = merge
            cmt['date'] = date
            cmt['author'] = author
            self.cmts.append(cmt)
          revno = line.replace('commit', '').strip()
          message = ''
          date = None
          merge = None
          chfiles = []
        elif line.startswith('Author:'):
          author = line.replace('Author:', '').strip()
        elif line.startswith('Merge:'):
          merge = line.replace('Merge:', '').strip()
        elif line.startswith('Date:'):
          date = line.replace('Date:', '').strip()
        elif line.startswith('    '):
          message += line.strip() + ' '
        else:
          chfiles.append(line.strip())

      #the last commit
      cmt = {}
      cmt['commitno'] = revno
      cmt['message'] = message
      cmt['chfiles'] = chfiles
      cmt['author'] = author
      cmt['date'] = date
      cmt['merge'] = merge
      self.cmts.append(cmt)

    self.printN()

