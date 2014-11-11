import csv
import readline

class ConfCha:
    """
    The base class for change-log analysis
    """
    def __init__(self):
        self.charepo = []
        self.plist = []
        self.totalvns = 0;
        self.totalcha = 0;
        self.confcha = 0;

    def parse(self, chalog):
        """
        The general parser that split all the changes into the repo
        """
        pass;

    def select(self, repo, keywords):
        """
        Given a list of keywords, return the changes that contains all the keywords
        """
        res = []
        for cha in repo:
            count = 0
            for kw in keywords:
                if len(kw) <= 3:
                    #try to avoid some too common words like use, via
                    continue
                if cha['changes'].find(kw) != -1:
                    count += 1
            if count > 0:
                print cha['changes'] + '\n'
                res.append(cha)
        print len(res)
        return res


    def getplist(self, plist):
        f = open(plist, 'r')
        for p in f:
            p = p.strip().lower()
            if len(p) > 0 and p.startswith('#') == False:
                self.plist.append(p)
        print '#parameters:', len(self.plist)

    def print2csv(self, repo, outputfile):
        f = open(outputfile, 'wb')
        writer = csv.writer(f, delimiter='\t')
        for cha in repo:
            writer.writerow(['--------------------', '------'])
            writer.writerow([cha['changes'], cha['version']])
        f.close()


class BazaarCha(ConfCha):
    """
    Cha for Bazaar
    """
    def parse(self, chalog):
        f = open(chalog, 'r')
        revno = ''
        message = ''
        for line in f:
            line = line.strip().lower()
            if line.startswith('------------------------------------------------------------'):
                #Handle the old ones
                if len(revno) > 0:
                    cha = {}
                    cha['version'] = revno
                    cha['changes'] = message
                    self.charepo.append(cha)
                #Reset
                revno = ''
                message = ''
            elif line.startswith('revno:'):
                revno = line.replace('revno:', '').strip()
            elif line.startswith('committer:'):
                pass
            elif line.startswith('author:'):
                pass
            elif line.startswith('From:'):
                pass
            elif line.startswith('branch'):
                pass
            elif line.startswith('timestamp:'):
                pass
            elif line.startswith('date:'):
                pass
            elif line.startswith('message:'):
                message = line.replace('message:', '').strip()
            else:
                #if line.find(': ') != -1:
                #    print line
                message += ' ' + line
        print len(self.charepo)
        print self.charepo[0]
        print self.charepo[-1]

#hadoopcha = HadoopCha()
#hadoopcha.parse('./hadoopcha/hadoop.svn.log')

