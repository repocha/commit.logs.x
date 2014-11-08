import sys
sys.path.append('..')
from cha import ConfCha

class SquidCha(ConfCha):
    def parse(self, chalog):
        """
        Parse the squid chang log
        """
        chl = open(chalog, 'r')
        startflag = False
        prevline = ''
        version = ''
        for line in chl:
            line = line.strip().lower()
            if len(line) == 0:
                continue
            if line.startswith('Changes to squid-'):
                #Start of a version
                line = line.replace('Changes to squid-', '')
                version = line[:line.find(' ')]
                self.totalvns += 1 
                print version
            elif line.startswith('-'):
                self.totalcha += 1
                #Handle the previous one
                cha = {}
                cha['version'] = version
                cha['changes'] = prevline
                self.charepo.append(cha)
                prevline = line
            else:
                prevline += line
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
        for cha in repo:
            count = 0
            for kw in keywords:
                if cha['changes'].find(kw) != -1:
                    count += 1
            if count > 0:
                print cha['changes'] + '\n'
                res.append(cha)
        print len(res)
        return res

squidcha = SquidCha()
squidcha.parse('squid-3.4-ChangeLog.txt')
squidcha.getplist('squid.p.all')
squidcha.select(squidcha.charepo, ['config'] + squidcha.plist)
#squidcha.select(squidcha.select(squidcha.charepo, ['configur'] + squidcha.plist), ['check'])
