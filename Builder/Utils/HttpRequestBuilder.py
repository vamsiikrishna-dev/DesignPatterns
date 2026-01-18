from .HttpRequest import HttpRequest

class HttpRequestBuilder():

    def __init__(self):
        self.request = HttpRequest()

    def with_url(self,url):
        self.request.url = url
        return self
    
    def with_header(self, key, value):
        self.request.headers[key] = value
        return self
    
    def with_param(self, key, value):
        self.request.params[key] = value
        return self

    def with_body(self, content):
        self.request.body = content
        return self

    def with_method(self,method):
        self.request.method = method
        return self

    def with_timeout(self,timeout):
        self.request.timeout = timeout
        return self
    
    def build(self):
        return self.request

    def clean(self):
        self.request = HttpRequest()


    