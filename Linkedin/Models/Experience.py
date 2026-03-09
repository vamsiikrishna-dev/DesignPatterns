

class Experience:
    def __init__(self, company, role, from_date, to_date=None):
        self.company = company
        self.role = role
        self.from_date = from_date
        self.to_date = to_date

    # Getters
    def get_company(self):
        return self.company

    def get_role(self):
        return self.role

    def get_from_date(self):
        return self.from_date

    def get_to_date(self):
        return self.to_date

    # Setters
    def set_company(self, company):
        self.company = company

    def set_role(self, role):
        self.role = role

    def set_from_date(self, from_date):
        self.from_date = from_date

    def set_to_date(self, to_date):
        self.to_date = to_date

    def __str__(self):
        to = self.to_date if self.to_date else "Present"
        return f"{self.role} at {self.company} ({self.from_date} - {to})"
