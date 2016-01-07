import sys
sys.path.append('../..')
from cha import GitCha
import subprocess
import os
import re

class OpenStackCha(GitCha):
  def removeMerge(self):
    res = []
    for cha in self.charepo:
      if cha['merge'] != None:
        res.append(cha)
    return res
    
oscha = OpenStackCha()
oscha.parse('keystone.git.log')
chas = oscha.select(oscha.removeMerge(), ['config', 'param', 'option'])
print len(chas)
for cha in chas:
  print cha['changes']
