
class Student():
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
class Professor():
    def __init__(self, name, stream):
        self.name = name
        self.stream = stream

if __name__ == '__main__':
    print("Student and Teacher classes are completely independent classes")