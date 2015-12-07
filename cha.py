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
        kwcount = {}
        for cha in repo:
            count = 0
            for kw in keywords:
                kwl = kw.lower()
                if len(kwl) <= 3:
                    ###THIS IS A HACK###
                    #we try to avoid some too common words like use, via
                    ####################
                    continue
                cnt = cha['changes'].lower()
                if cnt.find(kwl) != -1:
                    count += 1
                    if kw not in kwcount:
                        kwcount[kw] = 1
                    else:
                        kwcount[kw] += 1
            if count > 0:
                #print cha['changes'] + '\n'
                res.append(cha)
        print '-----------------------------------------------------------------------------'
        print 'The too popular keywords (count >= 50): '
        print '(perhaps we need to comment them out)'
        for kw in kwcount:
            if kwcount[kw] >= 50:
                print kw, kwcount[kw]
        print '-----------------------------------------------------------------------------'
        print 'Number of patches/cases we select out:'
        print len(res)
        print '-----------------------------------------------------------------------------'
        #for kw in keywords:
        #    if kw not in kwcount:
        #        print kw
        return res


    def getplist(self, plist):
        f = open(plist, 'r')
        for p in f:
            p = p.strip()
            if len(p) > 0 and p.startswith('#') == False:
                self.plist.append(p)
        print '#parameters:', len(self.plist)

    def print2csv(self, repo, outputfile):
        f = open(outputfile, 'wb')
        writer = csv.writer(f, delimiter='\t')
        for cha in repo:
            writer.writerow(['----------------------------'])
            writer.writerow([cha['changes'], cha['version']])
        f.close()

    def printinfo(self):
        print 'Number of patches/cases:', len(self.charepo)
        print '1st:', self.charepo[0] 
        print '2nd:', self.charepo[1]
        print '......'

class GitCha(ConfCha):
    """
    Cha for Git
    """
    def parse(self, chalog):
        f = open(chalog, 'r')
        revno = ''
        message = ''
        chfiles = []
        for line in f:
            if len(line.strip()) == 0:
                continue
            if line.startswith('commit '):
                if len(revno) > 0:
                    cha = {}
                    cha['version'] = revno
                    cha['changes'] = message
                    cha['chfiles'] = chfiles
                    self.charepo.append(cha)
                revno = line.replace('commit', '').strip()
                message = ''
                chfiles = []
            elif line.startswith('Author:'):
                pass
            elif line.startswith('Date:'):
                pass
            elif line.startswith('    '):
                message += line.strip() + ' '
            else:
                chfiles.append(line.strip())
        cha = {}
        cha['version'] = revno
        cha['changes'] = message
        cha['chfiles'] = chfiles
        self.charepo.append(cha)
        self.printinfo()

class SVNCha(ConfCha):
    """
    Cha for SVN
    """
    def parse(self, chalog):
        f = open(chalog, 'r')
        revno = ''
        message = ''
        chfiles = []
        for line in f:
            if len(line.strip()) == 0:
                continue
            if line.startswith('------------------------------------------------------------------------'):
                #Handle the old ones
                if len(revno) > 0:
                    cha = {}
                    cha['version'] = revno
                    cha['changes'] = message
                    cha['chfiles'] = chfiles
                    self.charepo.append(cha)
                #Reset
                revno = ''
                message = ''
                chfiles = []
            elif line.startswith('r'):
                temp_list = line.split()
                revno = temp_list[0]
            elif line.startswith('Changed paths:'):
                pass
            elif line.startswith('   M ') or line.startswith('   A ') or line.startswith('   D ') or line.startswith('   R '):
                chfiles.append(line)
            else:
                message += line.strip() + ' '
        self.printinfo()

class BazaarCha(ConfCha):
    """
    Cha for Bazaar
    """
    def parse(self, chalog):
        f = open(chalog, 'r')
        revno = ''
        message = ''
        for line in f:
            line = line.strip()
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
        self.printinfo()
