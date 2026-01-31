# Association: "We are equal partners who collaborate"
# Semantic essence: Mutual collaboration between independent equals

# ASSOCIATION: Doctor ↔ Patient (mutual professional relationship)
class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.patients = []  # Collaborates with patients
    
    def add_patient(self, patient):
        if patient not in self.patients:
            self.patients.append(patient)
            patient.add_doctor(self)  # Mutual relationship
    
    def treat_patient(self, patient):
        if patient in self.patients:
            print(f"Dr. {self.name} treating {patient.name}")

class Patient:
    def __init__(self, name, condition):
        self.name = name
        self.condition = condition
        self.doctors = []  # Collaborates with doctors
    
    def add_doctor(self, doctor):
        if doctor not in self.doctors:
            self.doctors.append(doctor)
    
    def consult_doctor(self, doctor):
        if doctor in self.doctors:
            print(f"{self.name} consulting with Dr. {doctor.name}")

# ASSOCIATION: Author ↔ Book (collaborative creative relationship)
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []  # Collaborates in creating books
    
    def write_book(self, book):
        if book not in self.books:
            self.books.append(book)
            book.add_author(self)  # Mutual relationship

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.authors = []  # Collaborates with authors
    
    def add_author(self, author):
        if author not in self.authors:
            self.authors.append(author)

# ASSOCIATION: Student ↔ Course (academic collaboration)
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []  # Collaborates in learning
    
    def enroll_in(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)  # Mutual relationship
    
    def attend_class(self, course):
        if course in self.courses:
            print(f"{self.name} attending {course.name}")

class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.students = []  # Collaborates in teaching
    
    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
    
    def conduct_class(self):
        print(f"Conducting {self.name} for {len(self.students)} students")

# ASSOCIATION: Husband ↔ Wife (equal partnership)
class Husband:
    def __init__(self, name):
        self.name = name
        self.wife = None  # Equal partner
    
    def marry(self, wife):
        self.wife = wife
        wife.husband = self  # Mutual relationship
    
    def collaborate_with_wife(self, task):
        if self.wife:
            print(f"{self.name} and {self.wife.name} working together on {task}")

class Wife:
    def __init__(self, name):
        self.name = name
        self.husband = None  # Equal partner
    
    def collaborate_with_husband(self, task):
        if self.husband:
            print(f"{self.name} and {self.husband.name} working together on {task}")

if __name__ == '__main__':
    # Semantic test: Equal partners who collaborate
    
    # Doctor-Patient collaboration
    dr_smith = Doctor("Smith", "Cardiology")
    dr_jones = Doctor("Jones", "Neurology")
    patient_alice = Patient("Alice", "Heart condition")
    
    # Mutual professional relationship
    dr_smith.add_patient(patient_alice)
    dr_jones.add_patient(patient_alice)  # Patient can have multiple doctors
    
    print(f"Alice has {len(patient_alice.doctors)} doctors")
    print(f"Dr. Smith has {len(dr_smith.patients)} patients")
    
    # Collaboration in action
    patient_alice.consult_doctor(dr_smith)
    dr_smith.treat_patient(patient_alice)
    
    # Author-Book collaboration
    author1 = Author("J.K. Rowling")
    author2 = Author("Neil Gaiman")
    book1 = Book("Harry Potter", "978-0439708180")
    book2 = Book("Good Omens", "978-0060853983")
    
    # Mutual creative relationship
    author1.write_book(book1)
    author2.write_book(book2)
    author1.write_book(book2)  # Co-authored book
    
    print(f"Good Omens has {len(book2.authors)} authors")
    print(f"J.K. Rowling wrote {len(author1.books)} books")
    
    # Student-Course collaboration
    student1 = Student("Bob", "S001")
    student2 = Student("Carol", "S002")
    course1 = Course("Python Programming", "CS101")
    course2 = Course("Data Structures", "CS102")
    
    # Mutual academic relationship
    student1.enroll_in(course1)
    student1.enroll_in(course2)
    student2.enroll_in(course1)
    
    print(f"Bob is enrolled in {len(student1.courses)} courses")
    print(f"CS101 has {len(course1.students)} students")
    
    # Collaboration in action
    student1.attend_class(course1)
    course1.conduct_class()
    
    # Marriage partnership
    husband = Husband("John")
    wife = Wife("Jane")
    husband.marry(wife)
    
    # Equal partnership collaboration
    husband.collaborate_with_wife("planning vacation")
    wife.collaborate_with_husband("managing finances")
    
    # Semantic test: Delete one partner - the other survives independently
    del student1
    print(f"After student leaves, CS101 still has {len(course1.students)} students")
    
    del dr_smith
    print(f"After doctor retires, Alice still has {len(patient_alice.doctors)} doctors")