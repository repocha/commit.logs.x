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
        #fields
        title    = ''
        desc     = ''
        comments = ''
        #flag: tell in which fields
        flag = ''
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            if line.startswith('------------------------------------------------------------------------'):
                #Handle the old ones
                if len(jirano) > 0:
                    print title
                    assert title.endswith('- ASF JIRA')
                    message = title + '\n'
                    message += desc + '\n'
                    cha = {}
                    cha['version'] = jirano
                    cha['changes'] = message
                    self.charepo.append(cha)
                #Reset
                jirano = ''
                message = ''
                title = ''
                desc = ''
                comments = ''
            elif line.startswith('[HADOOP-'):
                jirano = line[line.find('[')+1:line.find(']')]
                title = line
                flag = 'titl' 
            elif line == '[DESC]':
                flag = 'desc'
            elif line == '[COMMENTS]':
                flag = 'comm'
            else:
                if flag == 'desc':
                    desc += ' ' + line
                elif flag == 'comm':
                    comments += ' ' + line
                elif flag == 'titl':
                    title += ' ' + line
                else:
                    assert False
        self.printinfo() 

hadoopcha = HadoopCha()
hadoopcha.parse('hadoop.jira.logger')
hadoopcha.getplist('hadoop.p.all')
res = hadoopcha.select(hadoopcha.charepo, ['config'] + hadoopcha.plist)
hadoopcha.print2csv(res, 'hadoop.jira.cha.csv')
