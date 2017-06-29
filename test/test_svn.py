import sys
sys.path.append('..')
from svn_parser import SVNParser

svnp = SVNParser('httpd')
svnp.parse('../data/httpd.svn.log')
svnp.printN()
