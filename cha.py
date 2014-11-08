class ConfCha:
    """
    The base class for change-log analysis
    """
    def __init__(self):
        self.charepo = []
        self.totalcha = 0;
        self.confcha = 0;
    
    def parse(chalog):
        """
        The general parser that split all the changes into the repo
        """
        pass;

    def select(repo, keywords):
        """
        Given a list of keywords, return the changes that contains all the keywords
        """
        return []
