# Composition: "You exist because I created you - you are part of me"
# Semantic essence: Creator-creation relationship with existential dependency

# COMPOSITION: Human → Organs (human creates and owns organs)
class Heart:
    def __init__(self, blood_type):
        self.blood_type = blood_type
        self.beats_per_minute = 72
        self.human = None  # Belongs to exactly one human
    
    def beat(self):
        if self.human:
            print(f"{self.human.name}'s heart is beating at {self.beats_per_minute} BPM")

class Brain:
    def __init__(self, iq_level):
        self.iq_level = iq_level
        self.thoughts = []
        self.human = None  # Belongs to exactly one human
    
    def think(self, thought):
        if self.human:
            self.thoughts.append(thought)
            print(f"{self.human.name} is thinking: {thought}")

class Human:
    def __init__(self, name, blood_type, iq_level):
        self.name = name
        # Human creates its organs - they cannot exist without human
        self.heart = Heart(blood_type)
        self.brain = Brain(iq_level)
        
        # Set ownership - organs belong exclusively to this human
        self.heart.human = self
        self.brain.human = self
    
    def live(self):
        self.heart.beat()
        self.brain.think("I am alive")
    
    def __del__(self):
        print(f"{self.name} has died - organs stop functioning")

# COMPOSITION: Car → Engine/Transmission (car creates and owns its parts)
class Engine:
    def __init__(self, engine_type, horsepower):
        self.type = engine_type
        self.horsepower = horsepower
        self.car = None  # Belongs to exactly one car
    
    def start(self):
        if self.car:
            return f"{self.car.make} {self.car.model}'s {self.type} engine started"

class Transmission:
    def __init__(self, transmission_type):
        self.type = transmission_type
        self.gear = 1
        self.car = None  # Belongs to exactly one car
    
    def shift_gear(self, gear):
        if self.car:
            self.gear = gear
            print(f"{self.car.make} shifted to gear {gear}")

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        # Car creates its parts - they cannot exist without car
        self.engine = Engine("V6", 300)
        self.transmission = Transmission("Automatic")
        
        # Set ownership - parts belong exclusively to this car
        self.engine.car = self
        self.transmission.car = self
    
    def drive(self):
        print(self.engine.start())
        self.transmission.shift_gear(2)
    
    def __del__(self):
        print(f"{self.make} {self.model} scrapped - parts destroyed")

# COMPOSITION: House → Rooms (house creates and owns rooms)
class Room:
    def __init__(self, room_type, size):
        self.type = room_type
        self.size = size
        self.house = None  # Belongs to exactly one house
        self.furniture = []
    
    def add_furniture(self, item):
        if self.house:
            self.furniture.append(item)
            print(f"Added {item} to {self.type} in house at {self.house.address}")

class House:
    def __init__(self, address):
        self.address = address
        # House creates its rooms - they cannot exist without house
        self.rooms = [
            Room("Living Room", "20x15"),
            Room("Kitchen", "12x10"),
            Room("Master Bedroom", "15x12"),
            Room("Bathroom", "8x6")
        ]
        
        # Set ownership - rooms belong exclusively to this house
        for room in self.rooms:
            room.house = self
    
    def add_room(self, room_type, size):
        """House creates new rooms - they are part of this house"""
        new_room = Room(room_type, size)
        new_room.house = self
        self.rooms.append(new_room)
        return new_room
    
    def get_total_area(self):
        total = 0
        for room in self.rooms:
            # Parse size like "20x15" to calculate area
            dimensions = room.size.split('x')
            total += int(dimensions[0]) * int(dimensions[1])
        return total
    
    def __del__(self):
        print(f"House at {self.address} demolished - all rooms destroyed")

# COMPOSITION: Document → Pages (document creates and owns pages)
class Page:
    def __init__(self, page_number):
        self.page_number = page_number
        self.content = ""
        self.document = None  # Belongs to exactly one document
    
    def add_content(self, text):
        if self.document:
            self.content += text
            print(f"Added content to page {self.page_number} of '{self.document.title}'")

class Document:
    def __init__(self, title):
        self.title = title
        # Document creates its pages - they cannot exist without document
        self.pages = [
            Page(1),
            Page(2),
            Page(3)
        ]
        
        # Set ownership - pages belong exclusively to this document
        for page in self.pages:
            page.document = self
    
    def add_page(self):
        """Document creates new pages - they are part of this document"""
        new_page_number = len(self.pages) + 1
        new_page = Page(new_page_number)
        new_page.document = self
        self.pages.append(new_page)
        return new_page
    
    def get_total_content(self):
        total_content = ""
        for page in self.pages:
            total_content += page.content + " "
        return total_content.strip()
    
    def __del__(self):
        print(f"Document '{self.title}' deleted - all pages destroyed")

# COMPOSITION: Company → Departments (company creates and owns departments)
class CompanyDepartment:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.company = None  # Belongs to exactly one company
        self.projects = []
    
    def start_project(self, project_name):
        if self.company:
            self.projects.append(project_name)
            print(f"{self.name} dept at {self.company.name} started project: {project_name}")

class Company:
    def __init__(self, name):
        self.name = name
        # Company creates its departments - they cannot exist without company
        self.departments = [
            CompanyDepartment("Engineering", 1000000),
            CompanyDepartment("Marketing", 500000),
            CompanyDepartment("Sales", 750000)
        ]
        
        # Set ownership - departments belong exclusively to this company
        for dept in self.departments:
            dept.company = self
    
    def create_department(self, name, budget):
        """Company creates new departments - they are part of this company"""
        new_dept = CompanyDepartment(name, budget)
        new_dept.company = self
        self.departments.append(new_dept)
        return new_dept
    
    def get_total_budget(self):
        return sum(dept.budget for dept in self.departments)
    
    def __del__(self):
        print(f"Company {self.name} dissolved - all departments closed")

if __name__ == '__main__':
    # Semantic test: Creator-creation relationship with existential dependency
    
    # Human creating organs
    person = Human("Alice", "O+", 120)
    person.live()
    print(f"Alice's heart beats for Alice only")
    
    # Car creating parts
    car = Car("Toyota", "Camry")
    car.drive()
    print(f"Engine belongs exclusively to this {car.make}")
    
    # House creating rooms
    house = House("123 Main Street")
    living_room = house.rooms[0]
    living_room.add_furniture("Sofa")
    living_room.add_furniture("TV")
    
    # Add new room - created by house
    study = house.add_room("Study", "10x8")
    study.add_furniture("Desk")
    
    print(f"House total area: {house.get_total_area()} sq ft")
    print(f"Living room belongs to house at {living_room.house.address}")
    
    # Document creating pages
    doc = Document("My Novel")
    page1 = doc.pages[0]
    page1.add_content("Chapter 1: The beginning of an epic story.")
    
    # Add new page - created by document
    new_page = doc.add_page()
    new_page.add_content("Chapter 2: The plot thickens.")
    
    print(f"Document has {len(doc.pages)} pages")
    print(f"Total content: {doc.get_total_content()}")
    
    # Company creating departments
    company = Company("TechCorp")
    engineering = company.departments[0]
    engineering.start_project("AI Platform")
    
    # Create new department - created by company
    hr_dept = company.create_department("Human Resources", 300000)
    hr_dept.start_project("Employee Wellness Program")
    
    print(f"Company total budget: ${company.get_total_budget():,}")
    
    # Semantic test: Delete creator - all creations are destroyed
    print("\n--- Demonstrating existential dependency ---")
    
    del person  # Alice dies - heart and brain stop functioning
    del car     # Car scrapped - engine and transmission destroyed
    del house   # House demolished - all rooms destroyed
    del doc     # Document deleted - all pages destroyed
    del company # Company dissolved - all departments closed
    
    # Key semantic point: Parts cannot exist without their whole
    print("\nSemantic verification:")
    print("- Organs cannot exist without their human")
    print("- Car parts cannot exist without their car")
    print("- Rooms cannot exist without their house")
    print("- Pages cannot exist without their document")
    print("- Company departments cannot exist without their company")
    print("- All parts are created by and belong exclusively to their whole")