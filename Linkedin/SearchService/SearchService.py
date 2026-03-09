from .SearchByUsername import SearchByUserName

class SearchService:

    def __init__(self):
        self.strategy = SearchByUserName()

    def search(self, keyword, users):
        return self.strategy.search(keyword, users)
        