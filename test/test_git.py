import sys
sys.path.append('..')
from git_parser import GitParser

gitp = GitParser('hadoop')
#gitp.parse('../data/hadoop.git.log')
gitp.parse('../data/hadoop.log.name-status')
gitp.printN()
