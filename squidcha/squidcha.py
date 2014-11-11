import sys
sys.path.append('..')
from cha import ConfCha
from cha import BazaarCha

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
            line = line.strip()
            if len(line) == 0:
                continue
            if line.startswith('changes to squid-'):
                #Start of a version
                line = line.replace('changes to squid-', '')
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
    
#squidcha = SquidCha()
#squidcha.parse('squid-3.4-ChangeLog.txt')
#squidcha.getplist('squid.p.all')
#res = squidcha.select(squidcha.charepo, ['config'] + squidcha.plist)
#squidcha.print2csv(res, 'squid.cha.csv')
#squidcha.select(squidcha.select(squidcha.charepo, ['configur'] + squidcha.plist), ['check', 'detect'])

squidbzrcha = BazaarCha()
squidbzrcha.parse('bzr.log.txt')
squidbzrcha.getplist('squid.p.all')
res = squidbzrcha.select(squidbzrcha.charepo, ['config'] + squidbzrcha.plist)
squidbzrcha.print2csv(res, 'squid.bzr.cha.csv')

