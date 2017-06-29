import sys
sys.path.append('..')
from bzr_parser import BazaarParser

bzrp = BazaarParser('squid')
bzrp.parse('../data/squid.bzr.log')
bzrp.printN()
