from base_parser import BaseParser

class SVNParser(BaseParser):
  """for SVN commit logs
  """
  def parse(self, cmtlog):
    with open(cmtlog) as f:
      revno = ''
      message = ''
      chfiles = []
      for line in f:
        if len(line.strip()) == 0:
          continue
        if line.startswith('------------------------------------------------------------------------'):
          #Handle the old ones
          if len(revno) > 0:
            cmt = {}
            cmt['commitno'] = revno
            cmt['message'] = message
            cmt['chfiles'] = chfiles
            self.cmts.append(cmt)
            #Reset
            revno = ''
            message = ''
            chfiles = []
        elif line.startswith('r'):
          temp_list = line.split()
          revno = temp_list[0]
        elif line.startswith('Changed paths:'):
          pass
        elif line.startswith('   M ') or line.startswith('   A ') or line.startswith('   D ') or line.startswith('   R '):
          chfiles.append(line)
        else:
          message += line.strip() + ' '
