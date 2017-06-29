class KWFilter:
  """This is a simple keyword-based filter. The core function is "contains".
  Given a text string, the function returns true or false, indicating whether or
  not the text string is of interest.
  
  A filter encloses three types of information:
  (1) keywords must be included
  (2) keywords that only one of them needs to be included
  (3) keywords transformation

  Let me give an example. Among all the html files on ServerFault, 
  we want to select out all the html files related to 'access denied' or
  'permission denied'.
  Also, we want to filter 'htaccess' keywords.
  So, what we can do is, first replace 'htaccess' to ''; then search
  [ 
    ['access', 'deny'], 
    ['permission', 'deny']
  ].
  """
  def __init__(self, kwsl, repl=None):
    self.kwor = kwsl
    self.repl = repl

  def contains(self, text, tolower=True):
    if self.repl != None:
      for r in self.repl:
        text = text.replace(r, self.repl[r])
    for kws in self.kwor:
      if self.__contains_all(text, kws, tolower):
        return True
    return False

  def __contains_all(self, text, kws, tolower):
    for kw in kws:
      if tolower == True:
        kw = kw.lower()
        text = text.lower()
      if kw not in text:
        return False
    return True

def parser_filter_by_msg(parser, kwfilt):
  newcmts = []
  for cmt in parser.cmts:
    if kwfilt.contains(cmt['message']):
      newcmts.append(cmt)
  parser.cmts = newcmts
  return parser

def parser_filter_by_chfiles(parser, kwfilt, name_only=False):
  newcmts = []
  for cmt in parser.cmts:
    newchfl = []
    for chfile in cmt['chfiles']:
      nchfile = chfile
      if name_only:
        nchfile = nchfile[nchfile.rfind('/')+1:]
      if kwfilt.contains(nchfile):
        newchfl.append(chfile)
    if len(newchfl) > 0:
      cmt['chfiles'] = newchfl
      newcmts.append(cmt)
  parser.cmts = newcmts
  return parser
