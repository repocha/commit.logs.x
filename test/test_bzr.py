import sys
sys.path.append('..')
from bzr_parser import BazaarParser

bzrp = BazaarParser()
bzrp.parse('../data/squid.bzr.log')
