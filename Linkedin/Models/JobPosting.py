import uuid
from .JobPostState import JobState

class JobPosting:

    def __init__(self,position, experience, location, description, skills, state: 'JobState'):
        self.id = str(uuid.uuid4())
        self.position = position
        self.experience = experience
        self.location = location
        self.description = description
        self.skills = skills
        self.state = state


    # Getters
    def get_id(self):
        return self.id

    def get_position(self):
        return self.position

    def get_experience(self):
        return self.experience

    def get_location(self):
        return self.location

    def get_description(self):
        return self.description

    def get_skills(self):
        return self.skills

    # Setters
    def set_position(self, position):
        self.position = position

    def set_experience(self, experience):
        self.experience = experience

    def set_location(self, location):
        self.location = location

    def set_description(self, description):
        self.description = description

    def set_skills(self, skills):
        self.skills = skills

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def __str__(self):
        skills = ", ".join(self.skills) if self.skills else "None"
        return (
            f"JobPosting({self.position}, Experience: {self.experience}, "
            f"Location: {self.location}, State: {self.state.name}, Skills: [{skills}])"
        )
