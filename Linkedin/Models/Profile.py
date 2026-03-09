from .Experience import Experience
from .Education import Education
from .Skill import Skill


class Profile:

    def __init__(self, heading: str, summary: str, experience: list, education: list, skills: list):
        if not isinstance(heading, str):
            raise TypeError("heading must be a string")
        if not isinstance(summary, str):
            raise TypeError("summary must be a string")
        if not isinstance(experience, list) or not all(isinstance(e, Experience) for e in experience):
            raise TypeError("experience must be a list of Experience")
        if not isinstance(education, list) or not all(isinstance(e, Education) for e in education):
            raise TypeError("education must be a list of Education")
        if not isinstance(skills, list) or not all(isinstance(s, Skill) for s in skills):
            raise TypeError("skills must be a list of Skill")

        self.heading = heading
        self.summary = summary
        self.experience = experience
        self.education = education
        self.skills = skills

    # Getters
    def get_heading(self):
        return self.heading

    def get_summary(self):
        return self.summary

    def get_experience(self):
        return self.experience

    def get_education(self):
        return self.education

    def get_skills(self):
        return self.skills

    # Setters
    def set_heading(self, heading: str):
        if not isinstance(heading, str):
            raise TypeError("heading must be a string")
        self.heading = heading

    def set_summary(self, summary: str):
        if not isinstance(summary, str):
            raise TypeError("summary must be a string")
        self.summary = summary

    def set_experience(self, experience: list):
        if not isinstance(experience, list) or not all(isinstance(e, Experience) for e in experience):
            raise TypeError("experience must be a list of Experience")
        self.experience = experience

    def set_education(self, education: list):
        if not isinstance(education, list) or not all(isinstance(e, Education) for e in education):
            raise TypeError("education must be a list of Education")
        self.education = education

    def set_skills(self, skills: list):
        if not isinstance(skills, list) or not all(isinstance(s, Skill) for s in skills):
            raise TypeError("skills must be a list of Skill")
        self.skills = skills

    def __str__(self):
        skills_str = ", ".join(str(s) for s in self.skills)
        exp_str = "\n    ".join(str(e) for e in self.experience)
        edu_str = "\n    ".join(str(e) for e in self.education)
        return (
            f"Profile: {self.heading}\n"
            f"  Summary: {self.summary}\n"
            f"  Skills: [{skills_str}]\n"
            f"  Experience:\n    {exp_str}\n"
            f"  Education:\n    {edu_str}"
        )
