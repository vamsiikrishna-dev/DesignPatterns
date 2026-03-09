from .Search import Search
from Models import User


class SearchByUserName(Search):

    def search(self, keyword: str, users: list[User]):
        # search logic here
        keyword = keyword.lower()
        return [user for user in users if keyword in user.get_username().lower()]
        

