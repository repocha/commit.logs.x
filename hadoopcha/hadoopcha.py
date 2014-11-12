import sys
sys.path.append('..')
from cha import ConfCha

class HadoopCha(ConfCha):
    """
    Cha for Hadoop
    """
    def parse(self, chalog):
        f = open(chalog, 'r')
        jirano = ''
        message = ''
        for line in f:
            line = line.strip()
            if line.startswith('------------------------------------------------------------------------'):
                #Handle the old ones
                if len(jirano) > 0:
                    cha = {}
                    cha['version'] = jirano
                    cha['changes'] = message
                    self.charepo.append(cha)
                #Reset
                jirano = ''
                message = ''
            #elif line.startswith('r') and line.find('|') != -1:
            #    assert (line.endswith('line') or line.endswith('lines'))
            #elif line.startswith('HDFS') or line.startswith('MAPRED') or line.startswith('[HADOOP') or line.startswith('HDS') or line.startswith('YARN'):
            elif line.startswith('[HADOOP-'):
		    #jirano = line[:line.find(' ')].replace('.', '').strip()
                jirano = line[8:line.find(']')]
		messge = line 
            elif len(line) == 0:
                pass
            else:
                message += line
        print len(self.charepo)
        print self.charepo[0]
        print self.charepo[-1]
        #for cha in self.charepo:
        #    print cha['version']

hadoopcha = HadoopCha()
hadoopcha.parse('hadoop-jira')
hadoopcha.getplist('hadoop.p.all')
res = hadoopcha.select(hadoopcha.charepo, ['config'] + hadoopcha.plist)
hadoopcha.print2csv(res, 'hadoop.svn.cha.csv')
