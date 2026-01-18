from Utils import HttpRequestBuilder

if __name__ == '__main__':
    builder = HttpRequestBuilder()
    request = builder.with_url("http://localhost:8000/users")\
                    .with_method("GET")\
                    .with_param("id",2)\
                    .build()
    print(request)