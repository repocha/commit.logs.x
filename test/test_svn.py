import sys
sys.path.append('..')
from svn_parser import SVNParser

svnp = SVNParser()
svnp.parse('../data/httpd.svn.log')

