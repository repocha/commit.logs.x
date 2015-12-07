import sys
sys.path.append('..')
from cha import GitCha
import subprocess

class HadoopCha(GitCha):
    """
    The input file should be generated using git log --name-status
    """
    def selectxml(self):
        res = []
        for cha in self.charepo:
            if 'chfiles' not in cha:
                print cha
                return
            hit = False
            for f in cha['chfiles']:
                if f.endswith('default.xml'): # == True and f.endswith('pom.xml') == False:
                    hit = True
                    break
            if hit == True:
                res.append(cha)
        return res

    def pcha(self, chalst, repopath):
        for cha in chalst:
            commit = cha['version']
            cmd = ['git', '-C', repopath, 'show', commit]
            process = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE) 
            out, err = process.communicate()
            print commit
            print cha['changes']
            print out
            # get the diff using git show commitno
            # append in a file

hadoopCha = HadoopCha()
hadoopCha.parse('hadoop.log.name-status')
chalst = hadoopCha.selectxml()
#hadoopCha.pcha(chalst, '/home/tianyin/hadoop')
for cha in chalst:
    print cha['version'], cha['changes']
