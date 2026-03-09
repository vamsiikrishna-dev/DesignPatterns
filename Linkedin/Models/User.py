import uuid

class User:

    def __init__(self, username, password):
        self.id = str(uuid.uuid4())
        self.username = username
        self.password = password
        self.profile = None
        self.connection_requests = []
        self.connections = []
        self.inbox = []
        
    
    def get_username(self):
        return self.username
    
    
    def get_profile(self):
        return self.profile
    
    def set_username(self, username):
        self.username = username
    
    def set_profile(self, profile):
        self.profile = profile

    # Remaining getters
    def get_id(self):
        return self.id

    def get_password(self):
        return self.password

    def get_connection_requests(self):
        return self.connection_requests

    def get_connections(self):
        return self.connections

    def get_inbox(self):
        return self.inbox

    # Remaining setters
    def set_password(self, password):
        self.password = password

    def set_connection_requests(self, connection_requests):
        self.connection_requests = connection_requests

    def set_connections(self, connections):
        self.connections = connections

    def set_inbox(self, inbox):
        self.inbox = inbox

    def __str__(self):
        connections = ", ".join(c.username for c in self.connections) if self.connections else "None"
        return f"User({self.username}, ID: {self.id}, Connections: [{connections}])"

    def __repr__(self):
        return f"User({self.username})"
