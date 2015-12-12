import csv

def sort(issues, prefix):
  res = []
  ids = []
  jmap = {}
  for i in issues:
    jid = i['id']
    jid = jid.replace(prefix, '')
    jid = int(jid)
    jmap[jid] = i
    ids.append(jid)
  sjids = sorted(ids)
  for jid in sjids:
    issue = jmap[jid]
    res.append(issue)
  return res

def print2csv(issues, output):
  """
  We assume an issue to have the following attr:
  {id, url, title, summary}
  """
  with open(output, 'wb') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in issues:
      #csvwriter.writerow([i['id'], i['url'], i['title'].encode('utf-8'), i['summary'].encode('utf-8')])
      csvwriter.writerow([i['id'], i['url'], i['title'].encode('utf-8')])
