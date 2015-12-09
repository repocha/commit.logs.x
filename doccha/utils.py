import os
from lxml import etree
from lxml.html import fromstring
import lxml.html as lh
import csv

"""
Get the parameter difference
"""
def pdiff(opset, npset):
  """
  Print the diff between old pset and new pset
  """
  diff_set = []
  for p in new_set:
    if p not in old_set:
      #print '+', p
      diff_set.append('+,' + p)
  for p in old_set:
    if p not in new_set:
      #print '-', p
      diff_set.append('-,' + p)
  return diff_set

