
class HttpRequest():
    def __init__(self,url=""):
        self.url = url
        self.method = None
        self.params = {}
        self.headers = {}
        self.timeout = 5
        self.body = None
    
    def __str__(self):
        return f"URL:{self.url} Method:{self.method} Headers:{self.headers} Param:{self.params} Body:{self.body} Timeout:{self.timeout}"

