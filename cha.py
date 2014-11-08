class ConfCha:
    """
    The base class for change-log analysis
    """
    def __init__(self):
        self.charepo = []
        self.plist = []
        self.totalvns = 0;
        self.totalcha = 0;
        self.confcha = 0;

    def parse(self, chalog):
        """
        The general parser that split all the changes into the repo
        """
        pass;

    def select(self, repo, keywords):
        """
        Given a list of keywords, return the changes that contains all the keywords
        """
        return []

    def getplist(self, plist):
        f = open(plist, 'r')
        for p in f:
            p = p.strip()
            if len(p) > 0:
                self.plist.append(p)
        print '#parameters:', len(p)

