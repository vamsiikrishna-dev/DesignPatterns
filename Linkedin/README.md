# LinkedIn Low-Level Design 🔗

A comprehensive low-level design implementation of LinkedIn's core features using Python, demonstrating object-oriented design principles and design patterns.

## 📋 Overview

This project implements a simplified version of LinkedIn's backend system with core functionalities including user management, profiles, connections, job postings, notifications, and search capabilities.

## 🏗️ Architecture

### Design Patterns Used

- **Facade Pattern**: `Linkedin` class provides a unified interface to all subsystems
- **Strategy Pattern**: `SearchService` uses different search strategies
- **State Pattern**: `JobPosting` uses `JobState` enum for job status management
- **Observer Pattern**: Notification system for user interactions

### System Components

```
Linkedin/
├── Models/           # Core data models
├── Facadee/         # Facade pattern implementation
├── NotificationService/  # Notification system
├── SearchService/   # Search functionality with strategy pattern
└── Client.py        # Demo application
```

## 🎯 Core Features

### 1. User Management
- User registration and authentication
- Unique user identification with UUID
- Password-based login system

### 2. Profile Management
- Comprehensive user profiles with validation
- Experience, education, and skills tracking
- Type-safe profile creation and updates

### 3. Connection System
- Send and accept connection requests
- Bidirectional connection management
- Connection request tracking

### 4. Job Posting System
- Create and manage job postings
- Job state management (Open/Blocked/Closed)
- Skills-based job matching

### 5. Notification System
- Real-time notification delivery
- Multiple notification types
- User inbox management

### 6. Search Functionality
- Username-based search with strategy pattern
- Extensible search algorithms
- Case-insensitive search

## 🚀 Quick Start

1. **Run the demo**:
```bash
cd /Users/kandevam/Documents/Design\ Patterns/Linkedin
python Client.py
```

2. **Basic usage**:
```python
from Facadee import Linkedin
from Models import User, Profile, Experience, Education, Skill

# Initialize platform
linkedin = Linkedin()

# Register user
user = User("john_doe", "password123")
linkedin.register_user(user)

# Login
logged_user = linkedin.login("john_doe", "password123")

# Create profile
profile = Profile(
    heading="Software Engineer",
    summary="Passionate developer",
    experience=[Experience("Google", "SDE", "2020-01-01")],
    education=[Education("MIT", "B.S. CS", "2016-09-01", "2020-05-01")],
    skills=[Skill("Python"), Skill("Java")]
)
linkedin.create_profile(user, profile)
```

## 📚 API Reference

### Core Classes

#### User
```python
class User:
    def __init__(self, username: str, password: str)
    # Properties: id, username, password, profile, connections, inbox
```

#### Profile
```python
class Profile:
    def __init__(self, heading: str, summary: str, 
                 experience: list[Experience], 
                 education: list[Education], 
                 skills: list[Skill])
```

#### JobPosting
```python
class JobPosting:
    def __init__(self, position: str, experience: str, 
                 location: str, description: str, 
                 skills: list[str], state: JobState)
```

### Main Facade

#### Linkedin
```python
class Linkedin:
    def register_user(self, user: User)
    def login(self, username: str, password: str) -> User
    def send_connection_request(self, from_user: User, to_user: User)
    def accept_connection(self, user: User, target_user: User)
    def post_job(self, job: JobPosting)
    def create_profile(self, user: User, profile: Profile)
    def send_notification(self, sender: User, receiver: User, 
                         content: str, notification_type: NotificationType)
    def search(self, keyword: str) -> list[User]
```

## 🔧 Design Decisions

### 1. Facade Pattern
The `Linkedin` class acts as a facade, providing a simple interface to complex subsystems:
- Centralizes all operations
- Hides implementation complexity
- Provides consistent API

### 2. Type Safety
- Strong typing with type hints
- Runtime validation in Profile class
- Prevents invalid data states

### 3. Separation of Concerns
- Models handle data representation
- Services handle business logic
- Clear boundaries between components

### 4. Extensible Search
- Strategy pattern allows multiple search algorithms
- Easy to add new search criteria
- Pluggable search implementations

### 5. State Management
- Enum-based job states for type safety
- Clear state transitions
- Prevents invalid state changes

## 🎓 Learning Outcomes

### Object-Oriented Design
- **Encapsulation**: Private attributes with getter/setter methods
- **Inheritance**: Abstract Search class with concrete implementations
- **Polymorphism**: Strategy pattern in search functionality
- **Abstraction**: Clean interfaces hiding implementation details

### Design Patterns
- **Facade**: Simplified interface to complex subsystems
- **Strategy**: Pluggable search algorithms
- **State**: Job posting state management
- **Observer**: Notification system architecture

### Best Practices
- **Single Responsibility**: Each class has one clear purpose
- **Open/Closed**: Easy to extend without modifying existing code
- **Dependency Inversion**: High-level modules don't depend on low-level details
- **Interface Segregation**: Clean, focused interfaces

## 🔍 Code Examples

### Creating and Managing Connections
```python
# Send connection request
linkedin.send_connection_request(alice, bob)

# Accept connection
linkedin.accept_connection(bob, alice)

# Both users are now connected
print(f"Alice's connections: {alice.get_connections()}")
print(f"Bob's connections: {bob.get_connections()}")
```

### Job Posting Workflow
```python
# Create job posting
job = JobPosting(
    position="Senior Developer",
    experience="5+ years",
    location="Remote",
    description="Build scalable systems",
    skills=["Python", "AWS"],
    state=JobState.OPEN
)

# Post job
linkedin.post_job(job)

# Update job state
job.set_state(JobState.CLOSED)
```

### Notification System
```python
# Send notification
linkedin.send_notification(
    sender=alice,
    receiver=bob,
    content="Profile view notification",
    notification_type=NotificationType.MESSAGE
)

# Check inbox
for notification in bob.get_inbox():
    print(notification)
```

## 🚀 Extensions

### Potential Enhancements
1. **Advanced Search**: Add search by skills, location, company
2. **Messaging System**: Direct messaging between connections
3. **Feed System**: Activity feed with posts and updates
4. **Recommendation Engine**: Job and connection recommendations
5. **Privacy Settings**: Control profile visibility
6. **Company Pages**: Corporate profiles and employee management

### Adding New Search Strategy
```python
class SearchBySkills(Search):
    def search(self, keyword: str, users: list[User]) -> list[User]:
        results = []
        for user in users:
            if user.get_profile():
                for skill in user.get_profile().get_skills():
                    if keyword.lower() in skill.get_name().lower():
                        results.append(user)
                        break
        return results

# Use new strategy
search_service.strategy = SearchBySkills()
```

## 📊 System Metrics

- **Classes**: 12 core classes
- **Design Patterns**: 4 patterns implemented
- **Features**: 6 major feature areas
- **Type Safety**: Full type hints and validation
- **Test Coverage**: Comprehensive demo scenarios

## 🤝 Contributing

Feel free to:
- Add new search strategies
- Implement additional notification types
- Enhance profile features
- Add new design patterns
- Improve error handling

---

⭐ **Perfect for learning system design, OOP principles, and design patterns in Python!**