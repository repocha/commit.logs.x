import os
from lxml import etree
from lxml.html import fromstring
import lxml.html as lh
import csv


def getFiles(dir_path):
    fl = os.listdir(dir_path)
    for f in fl:
        if f.find('index.html') != -1:
            continue
        if f.find('directive.html') != -1 or f.find('directive-dict.html') != -1 or f.find('directives.html') != -1:
            continue
        if f.find('module-dict.html') != -1:
            continue
        if (f.endswith('html') and f+'.en' not in fl) or (f.endswith('html.en')):
            print f   

"""
Only works for 2.0.42 --> 2.4.*
"""
def getAllParameters(dir_path, v, norm):
    apset = []
    fl = os.listdir(dir_path)
    for f in fl:
        if f.find('index.html') != -1:
            continue
        if f.find('directive.html') != -1 or f.find('directive-dict.html') != -1 or f.find('directives.html') != -1:
            continue
        if f.find('module-dict.html') != -1:
            continue

        if (f.endswith('html') and f+'.en' not in fl) or (f.endswith('html.en')):
            #print dir_path + f
            if v == '1':
                pset = getParametersOldHTML(dir_path + f) 
            elif v == '2':
                pset = getParametersHTML(dir_path + f, norm) 
            for p in pset:
                if p not in apset:
                    apset.append(p)
        else:
            pass
    #print len(apset)
    return apset



"""
Works for versions before 2.0.42
"""
def getParametersOldHTML(path):
    if path.find('mod_unique_id.html') != -1: return []
    
    f = open(path)
    xml = f.read()
    f.close()
    doc = fromstring(xml)
    
    pset = []
    i = 0
    for ul in doc.iter('ul'):
        i += 1
        if path.find('mod_negotiation.html') != -1 or \
           path.find('mod_dir.html') != -1 or \
           path.find('mod_log_forensic') != -1 or \
           path.find('mod_status.html') != -1  or \
           path.find('mod_ext_filter') != -1:
            if i == 1: continue
        if path.find('mod_rewrite.html') != -1 and path.find('apache_1') != -1:
            if i == 1: continue 
        if path.find('mod_imap.html') != -1 and path.find('apache_1') != -1:
            imap = path.replace('/home/tixu/software/httpd-dist/apache_1.3.', '')
            imap = imap.replace('/htdocs/manual/mod/mod_imap.html', '')
            vi = int(imap)
            if vi < 14 and i == 1: continue
        if path.find('mod_log_config.html') != -1 and path.find('apache_1') != -1:
            imap = path.replace('/home/tixu/software/httpd-dist/apache_1.3.', '')
            imap = imap[:imap.find('/htdocs/manual/mod/mod_log_config.html')]
            vi = int(imap)
            if vi < 14 and i == 1: continue 
        if path.find('mod_auth_ldap.html') != -1 and path.find('httpd-2') != -1:
            if i == 1: continue 
        if path.find('mod_speling.html') != -1:
            return ['checkspelling']
        for li in ul.iter('li'):
            p = li.text_content().strip().lower()
            p = p.replace('<', '')
            p = p.replace('>', '')
            pset.append(p)
        #break after the ul block
        break
    #print len(pset)
    return pset    
   

"""
This works for most new HTML manual pages
"""
def getParametersHTML(path, norm):
    f = open(path)
    xml = f.read()
    f.close()
    doc = fromstring(xml)
    
    pset = []
    try:
        for li in doc.get_element_by_id('toc'):
            p = li.text_content().strip()
            if norm == True:
                p = p.lower()
            p = p.replace('<', '')
            p = p.replace('>', '')
            pset.append(p)
    except:
        #print '[WARN] Do not find toc:', path
        pass
    #print len(pset)
    return pset    

"""
Get the parameter difference
"""
def psetDiff(old_set, new_set):
    diff_set = []
    for p in new_set:
        if p not in old_set:
            #print '+', p
            diff_set.append('+,' + p)
    for p in old_set:
        if p not in new_set:
            #print '-', p
            diff_set.append('-,' + p)
    return diff_set


"""
Get all the diff parameter in all set
"""
def httpdDiff(release_file):
    w = open('httpd.diff', 'wb')
    f = open(release_file, 'rb')
    reader = csv.reader(f, delimiter=',')
    prev_pset = [] 
    for row in reader:
        #print row[0]
        #print row[1]
        docpath = '/home/tixu/software/httpd-dist/' + row[0] + row[1]
        curr_pset = getAllParameters(docpath, row[2])
        ds = psetDiff(prev_pset, curr_pset)
        for d in ds:
            print d + "," + row[0]
        prev_pset = curr_pset        
    w.close()


"""
Study the core part of httpd
"""
def core_diff(release_file):
    pages = ['core.html', 'mpm_common.html', 'beos.html', 'event.html', 'mpm_netware.html', 'mpmt_os2.html', 'prefork.html', 'mpm_winnt.html', 'worker.html']
    page_path = []
    w = open('httpd_core.diff', 'wb')
    f = open(release_file, 'rb')
    reader = csv.reader(f, delimiter=',')
    prev_pset = [] 
    for row in reader:
        #print row[0]
        #print row[1]
        curr_pset = []
        docpath  = '/home/tixu/software/httpd-dist/' + row[0] + row[1]
        
        for p in pages:
            if os.path.isfile(docpath + p + '.en'):
                page_path.append(docpath + p + '.en')
            elif os.path.isfile(docpath + p):
                page_path.append(docpath + p)
 
        if row[2] == '1':
            for pp in page_path:
                merge_set(curr_pset, getParametersOldHTML(pp, False))
        elif row[2] == '2':
            for pp in page_path:
                merge_set(curr_pset, getParametersHTML(pp, False))
        #curr_pset = getAllParameters(docpath, row[2])
        ds = psetDiff(prev_pset, curr_pset)
        for d in ds:
            print d + "," + row[0]
        prev_pset = curr_pset        
    w.close()

def merge_set(set1, set2):
    for e in set2:
        if e not in set1:
            set1.append(e)
    

def httpdChecker(results):
    f = open(results, 'rb')
    reader = csv.reader(f, delimiter=',')
    pcounter = {}
    for row in reader:
        t = row[0]
        p = row[1]
        v = row[2]
        if p not in pcounter:
            pcounter[p] = []
        pcounter[p].append([t, p, v])

    print len(pcounter)
    dset = []
    for p in pcounter:
        l = len(pcounter[p])
        if l > 2:
            if l%2 == 1:
                pcounter[p] = [pcounter[p][0]]
            if l%2 == 0:
                pcounter[p] = [pcounter[p][0], pcounter[p][1]]
    
    print len(pcounter)
    
    f2 = open(results, 'rb')
    reader2 = csv.reader(f2, delimiter=',')
    for row in reader2:
        t = row[0]
        p = row[1]
        v = row[2]
        valid = False
        for tri in pcounter[p]:
            #print tri[0], tri[1], tri[2]
            #print t, p, v
            if tri[0] == t and tri[1] == p and tri[2] == v:
                valid = True
                break
        if valid == True:
            print t + ',' +  p + ',' +  v


#getFiles('/home/tixu/software/httpd-dist/httpd-2.4.7/docs/manual/mod/')

#httpdDiff('./httpd-release-file.csv')

core_diff('./httpd2-release-file.csv')

#httpdChecker('mapred.diff')
#s = getAllParameters('/home/tixu/software/httpd-dist/httpd-2.4.7/docs/manual/mod/', '2', False)
#for p in s:
#    print p
#print len(s)
#getAllParameters('/home/tixu/software/httpd-dist/httpd-2.0.42/docs/manual/mod/')

#s1 = getParametersHTML(core.html.en')
#s2 = getParametersHTML('/home/tixu/software/httpd-dist/httpd-2.4.7/docs/manual/mod/core.html.en')
#s2 = getParametersOldHTML('/home/tixu/software/httpd-dist/apache_1.3.0/htdocs/manual/mod/core.html')
#print psetDiff(s1, s2)


#ps = getParametersHTML('/home/tixu/software/httpd-dist/httpd-2.4.7/docs/manual/mod/core.html.en')
#for p in ps:
#    print p 

