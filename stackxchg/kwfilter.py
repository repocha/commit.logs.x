
class KWFilter:
  """
  This is a simple keyword-based filter. The core function is "contains".
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
  So, what we can do is, first replace 'htaccess' to ''; then
  search [['access', 'deny'], ['permission', 'deny']].
  """
  def __init__(self, kwsl, repl):
    self.kwor = kwsl
    self.replace = repl

  def contains(self, text):
    for r in repl:
      text = text.replace(r, repl[r])
    for kws in kwor:
      if self.containsAll(text, kws)
        return True
    return False

  def containsAll(self, text, kws):
    for kw in kws:
      if kw not in text:
        return False
    return True
