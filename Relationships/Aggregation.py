# Aggregation: "I organize and manage you, but you can exist elsewhere"
# Semantic essence: Organizational relationship with independent objects

# AGGREGATION: Library → Book (library organizes books)
class Book:
    def __init__(self, title, isbn, author):
        self.title = title
        self.isbn = isbn
        self.author = author
        # Book exists independently of any library

class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []  # Organizes existing books
    
    def acquire_book(self, book):
        """Library organizes books that exist independently"""
        if book not in self.books:
            self.books.append(book)
            print(f"Library acquired: {book.title}")
    
    def remove_book(self, book):
        """Book can be moved to another library"""
        if book in self.books:
            self.books.remove(book)
            print(f"Book removed: {book.title}")
    
    def list_books(self):
        print(f"{self.name} has {len(self.books)} books")

# AGGREGATION: Team → Player (team organizes players)
class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        # Player exists independently of any team

class Team:
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport
        self.players = []  # Organizes existing players
    
    def sign_player(self, player):
        """Team organizes players who exist independently"""
        if player not in self.players:
            self.players.append(player)
            print(f"Team signed: {player.name}")
    
    def release_player(self, player):
        """Player can join another team"""
        if player in self.players:
            self.players.remove(player)
            print(f"Player released: {player.name}")
    
    def list_roster(self):
        print(f"{self.name} has {len(self.players)} players")

# AGGREGATION: Playlist → Song (playlist organizes songs)
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        # Song exists independently of any playlist

class Playlist:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.songs = []  # Organizes existing songs
    
    def add_song(self, song):
        """Playlist organizes songs that exist independently"""
        if song not in self.songs:
            self.songs.append(song)
            print(f"Added to playlist: {song.title}")
    
    def remove_song(self, song):
        """Song can be in multiple playlists"""
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed from playlist: {song.title}")
    
    def play_playlist(self):
        print(f"Playing {self.name} with {len(self.songs)} songs")

# AGGREGATION: Department → Employee (department organizes employees)
class Employee:
    def __init__(self, name, emp_id, role):
        self.name = name
        self.emp_id = emp_id
        self.role = role
        # Employee exists independently of any department

class Department:
    def __init__(self, name, dept_code):
        self.name = name
        self.dept_code = dept_code
        self.employees = []  # Organizes existing employees
    
    def hire_employee(self, employee):
        """Department organizes employees who exist independently"""
        if employee not in self.employees:
            self.employees.append(employee)
            print(f"Department hired: {employee.name}")
    
    def transfer_employee(self, employee):
        """Employee can be transferred to another department"""
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"Employee transferred: {employee.name}")
    
    def list_staff(self):
        print(f"{self.name} has {len(self.employees)} employees")

# AGGREGATION: Portfolio → Stock (portfolio organizes stocks)
class Stock:
    def __init__(self, symbol, company, price):
        self.symbol = symbol
        self.company = company
        self.price = price
        # Stock exists independently in the market

class Portfolio:
    def __init__(self, owner):
        self.owner = owner
        self.stocks = []  # Organizes existing stocks
    
    def buy_stock(self, stock):
        """Portfolio organizes stocks that exist independently"""
        if stock not in self.stocks:
            self.stocks.append(stock)
            print(f"Bought stock: {stock.symbol}")
    
    def sell_stock(self, stock):
        """Stock continues to exist in the market"""
        if stock in self.stocks:
            self.stocks.remove(stock)
            print(f"Sold stock: {stock.symbol}")
    
    def view_portfolio(self):
        print(f"{self.owner}'s portfolio has {len(self.stocks)} stocks")

if __name__ == '__main__':
    # Semantic test: Organization of independent objects
    
    # Library organizing books
    book1 = Book("1984", "978-0451524935", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "978-0061120084", "Harper Lee")
    book3 = Book("Pride and Prejudice", "978-0141439518", "Jane Austen")
    
    library1 = Library("Central Library", "Downtown")
    library2 = Library("Branch Library", "Suburb")
    
    # Libraries organize existing books
    library1.acquire_book(book1)
    library1.acquire_book(book2)
    library2.acquire_book(book1)  # Same book in multiple libraries
    library2.acquire_book(book3)
    
    library1.list_books()
    library2.list_books()
    
    # Team organizing players
    player1 = Player("Lionel Messi", "Forward")
    player2 = Player("Cristiano Ronaldo", "Forward")
    player3 = Player("Virgil van Dijk", "Defender")
    
    team1 = Team("Barcelona", "Football")
    team2 = Team("Real Madrid", "Football")
    
    # Teams organize existing players
    team1.sign_player(player1)
    team1.sign_player(player3)
    team2.sign_player(player2)
    
    # Player can be transferred
    team1.release_player(player1)
    team2.sign_player(player1)  # Player moves to another team
    
    team1.list_roster()
    team2.list_roster()
    
    # Playlist organizing songs
    song1 = Song("Bohemian Rhapsody", "Queen", "5:55")
    song2 = Song("Stairway to Heaven", "Led Zeppelin", "8:02")
    song3 = Song("Hotel California", "Eagles", "6:30")
    
    playlist1 = Playlist("Rock Classics", "Alice")
    playlist2 = Playlist("Greatest Hits", "Bob")
    
    # Playlists organize existing songs
    playlist1.add_song(song1)
    playlist1.add_song(song2)
    playlist2.add_song(song1)  # Same song in multiple playlists
    playlist2.add_song(song3)
    
    playlist1.play_playlist()
    playlist2.play_playlist()
    
    # Department organizing employees
    emp1 = Employee("Alice Johnson", "E001", "Developer")
    emp2 = Employee("Bob Smith", "E002", "Designer")
    emp3 = Employee("Carol Davis", "E003", "Manager")
    
    dept_it = Department("IT", "D001")
    dept_design = Department("Design", "D002")
    
    # Departments organize existing employees
    dept_it.hire_employee(emp1)
    dept_it.hire_employee(emp3)
    dept_design.hire_employee(emp2)
    
    # Employee can be transferred
    dept_it.transfer_employee(emp1)
    dept_design.hire_employee(emp1)  # Employee moves to another department
    
    dept_it.list_staff()
    dept_design.list_staff()
    
    # Semantic test: Delete organizer - organized objects survive
    del library1
    print(f"After library closes, book '{book1.title}' still exists")
    
    del team1
    print(f"After team disbands, player '{player3.name}' still exists")
    
    del playlist1
    print(f"After playlist deleted, song '{song1.title}' still exists")
    
    # Key semantic point: Objects are organized, not owned
    print("\nSemantic verification:")
    print("- Books can move between libraries")
    print("- Players can transfer between teams") 
    print("- Songs can be in multiple playlists")
    print("- Employees can change departments")
    print("- All objects exist independently of their organizers")