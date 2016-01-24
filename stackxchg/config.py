import ConfigParser, os

DEFAULT_CONFIG_FILE = 'stackxchg_craw.cfg'

config = ConfigParser.SafeConfigParser()
config.read(DEFAULT_CONFIG_FILE)


def dump():
  print '###', DEFAULT_CONFIG_FILE, '##########################################'
  for sec in config.sections():
    print '[' + sec + ']'
    for item in config.items(sec):
      print '%-25s =   %-100s' % (item[0], item[1])
  print '######################################################################'

if __name__ == "__main__":
  dump()
  #print config.get('tagged_url_crawler', 'website')
