

class Education:

    def __init__(self, school, qualification, from_date, to_date=None):
        self.school = school
        self.qualification = qualification
        self.from_date = from_date
        self.to_date = to_date

    # Getters
    def get_school(self):
        return self.school

    def get_qualification(self):
        return self.qualification

    def get_from_date(self):
        return self.from_date

    def get_to_date(self):
        return self.to_date

    # Setters
    def set_school(self, school):
        self.school = school

    def set_qualification(self, qualification):
        self.qualification = qualification

    def set_from_date(self, from_date):
        self.from_date = from_date

    def set_to_date(self, to_date):
        self.to_date = to_date

    def __str__(self):
        to = self.to_date if self.to_date else "Present"
        return f"{self.qualification} from {self.school} ({self.from_date} - {to})"
