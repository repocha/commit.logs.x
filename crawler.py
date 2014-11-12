
class Crawler:
    """
    The base class for crawler
    """
    def __init__(self, odir, olog):
        self.output_dir = odir
        self.output_log = olog

    def crawl(self):
        """
        Crawling stuff and output to the dir
        """
        pass

    def write2log(self):
        pass
