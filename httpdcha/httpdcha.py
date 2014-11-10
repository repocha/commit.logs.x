import sys
sys.path.append('..')
from cha import ConfCha

class HTTPDCha(ConfCha):
    def parse(self, chalog):
        """
        Parse the httpd chang log
        """
        chl = open(chalog, 'r')
        prevline = ''
        version = ''
        for line in chl:
            line = line.strip().lower()
            if len(line) == 0:
                continue
            if line.find('-*- coding: utf-8 -*-') != -1:
                continue
            if line.startswith('changes with apache'):
                #Start of a version
                line = line.replace('changes with apache', '')
                version = line.strip()
                self.totalvns += 1 
                print version
            elif line.startswith('*)'):
                self.totalcha += 1
                #Handle the previous one
                cha = {}
                cha['version'] = version
                cha['changes'] = prevline
                self.charepo.append(cha)
                prevline = line
            else:
                prevline += ' ' + line
        #the last one
        cha = {}
        cha['version'] = version
        cha['changes'] = prevline
        self.charepo.append(cha)   
        print len(self.charepo)
        print self.totalvns
        print self.totalcha
        #print self.charepo

    def select(self, repo, keywords):
        res = []
        kwcount = {}
        for cha in repo:
            count = 0
            for kw in keywords:
                if len(kw) <= 4:
                    #try to avoid some too common words like use, via
                    continue
                if cha['changes'].find(kw) != -1:
                    count += 1
                    if kw not in kwcount:
                        kwcount[kw] = 0
                    else:
                        kwcount[kw] += 1
                    #cha['changes'] = cha['changes'].replace(kw, '*' + kw + '*')
            if count > 0:
                print cha['changes'], cha['version'], '\n'
                res.append(cha)
        print len(res)
#        for kw in kwcount:
#            if kwcount[kw] > 100:
#                print kw, kwcount[kw]
        return res

httpdcha = HTTPDCha()
httpdcha.parse('CHANGES_ALL')
httpdcha.getplist('httpd.p.all')
#httpdcha.select(httpdcha.charepo, ['config'])
res = httpdcha.select(httpdcha.charepo, ['config'] + httpdcha.plist)
httpdcha.print2csv(res, 'httpd.cha.csv.2')
#httpdcha.select(httpdcha.select(httpdcha.charepo, ['config']), ['check', 'detect'])

