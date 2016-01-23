from lxml.html import fromstring

def parseHTML(pagepath):
  """
  Parse a page (specified by $pagepath)
  Return a page object
  """
  page = {}
  try:
    with open(pagepath) as f: 
      doc = fromstring(f.read())
      page['url']  = getlink(doc)
      page['stat'] = getstat(doc)
      page['question'] = []
      page['answer'] = []
      for question in doc.find_class('question'):
        page['question'].append(question.text_content())
      for answer in doc.find_class('answer'):
        page['answer'].append(answer.text_content())
    return page
  except Exception as e:
    print 'FAILURE: ', pagepath, ' | ', str(e)
    return None


def getstat(doc):
  for accepted in doc.find_class('accepted-answer'):
    return 'closed'
  return 'open'

def getlink(doc):
  for l in doc.iter('link'):
    if l.get('rel') == 'canonical':
      return l.get('href')

#p = parseHTML('requests-made-to-a-website-with-a-different-domain-url-in-log-files-hacking-att')
#p = parseHTML('apache-2-2-mod-rewrite-redirect-some-urls-to-https-and-force-http-for-others.1')
#print p['url']
#print p['stat']
#print len(p['question'])
#print len(p['answer'])
#for x in p['answer']:
#  if 'I am logging the url that you see in your browser bar when you are on my website' in x:
#    print 'yes!'
