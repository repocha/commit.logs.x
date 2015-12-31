#!/usr/bin/python
import sys
sys.path.append('..')
from cha import ConfCha
from cha import BazaarCha

email_split_string = "-------------- next part --------------"

class OpenStackCha(ConfCha):
    def parse(self, chalog):
        print chalog
        """
        Parse the squid chang log
        """
        data = open(chalog, 'r').read()

        parts = data.split(email_split_string)

        line = None

        for part in parts:
            if "swift" not in part.lower():
                continue
            lines = part.split("\n")
            for line in lines:
                if line.startswith("Subject: "):
                    version = line
                    break

            if line is None:
                print "Ehh? no subjects?"

            changes = part

            cha = {}
            cha['version'] = version
            cha['changes'] = part
            self.charepo.append(cha)   

        print "total_chas", len(self.charepo)
    
#squidcha = SquidCha()
#squidcha.parse('squid-3.4-ChangeLog.txt')
#squidcha.getplist('squid.p.all')
#res = squidcha.select(squidcha.charepo, ['config'] + squidcha.plist)
#squidcha.print2csv(res, 'squid.cha.csv')
#squidcha.select(squidcha.select(squidcha.charepo, ['configur'] + squidcha.plist), ['check', 'detect'])

if __name__ == "__main__":
    openstackcha = OpenStackCha()
    openstackcha.parse("openstack.a")
    openstackcha.getplist("openstack.p.all")
    res = openstackcha.select(openstackcha.charepo, openstackcha.plist)
    openstackcha.print2csv(res, "openstack.csv")

# squidbzrcha = BazaarCha()
#squidbzrcha.parse('bzr.log.txt')
#squidbzrcha.getplist('squid.p.all')
#res = squidbzrcha.select(squidbzrcha.charepo, ['config'] + squidbzrcha.plist)
#squidbzrcha.print2csv(res, 'squid.bzr.cha.csv')

