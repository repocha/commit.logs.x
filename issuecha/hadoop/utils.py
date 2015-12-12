import csv

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
