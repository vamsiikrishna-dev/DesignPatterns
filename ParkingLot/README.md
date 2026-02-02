# Parking Lot System Design Pattern 🚗

A comprehensive implementation of a parking lot management system demonstrating multiple design patterns working together in a real-world scenario.

## 🎯 Design Patterns Used

### 1. **Singleton Pattern**
- `ParkingSystem` - Ensures only one parking system instance exists
- `TicketManager` - Centralized ticket management
- `ConsoleLogger` - Single logging instance

### 2. **Strategy Pattern**
- `ChargeStrategy` - Different pricing strategies (Fixed, Dynamic)
- Allows runtime switching between pricing models

### 3. **Factory Pattern**
- Creates parking slots of different types
- Manages object creation complexity

## 🏗️ System Architecture

```
ParkingSystem (Singleton)
├── ParkingFloor[]
│   └── ParkingSlot[]
├── TicketManager (Singleton)
└── ChargeStrategy (Strategy)
```

## 🚀 Key Features

- **Multi-floor parking** with different slot types
- **Dynamic pricing** based on vehicle type and duration
- **Ticket-based** parking management
- **Real-time slot availability** tracking
- **Extensible design** for new vehicle types

## 💡 Real-World Problem Solved

Managing a parking lot involves:
- Tracking available slots across multiple floors
- Different pricing for different vehicle types
- Generating and validating parking tickets
- Calculating charges based on duration

## 🔧 Implementation Highlights

### Slot State Management
```python
def book_slot(self, vehicle_type: ParkingSlotType, vehicle_id):
    empty_slots = [slot for slot in self.slots.values() 
                   if slot.get_type() == vehicle_type 
                   and slot.get_state() == ParkingSlotState.EMPTY]
    if empty_slots:
        slot = empty_slots[0]
        slot.set_state(ParkingSlotState.BOOKED)
        return TicketManager.get_instance().create_ticket(vehicle_id, slot.get_id())
```

### Strategy Pattern for Pricing
```python
class DynamicChargeStrategy(ChargeStrategy):
    def calculate_charge(self, vehicle_type, duration):
        base_rate = self.get_base_rate(vehicle_type)
        return base_rate * duration * self.get_multiplier()
```

## 🎮 Usage Example

```python
# Initialize system
system = ParkingSystem.get_instance()
floor = ParkingFloor()
floor.add_slot(ParkingSlot(ParkingSlotType.MEDIUM))
system.add_floor(floor)

# Park vehicle
ticket = system.park_vehicle(ParkingSlotType.MEDIUM, 'AP27PEK9409')
print(f"Ticket: {ticket}")

# Unpark and calculate cost
cost = system.unpark_vehicle(ticket)
print(f"Parking cost: ${cost}")
```

## 🎓 Learning Outcomes

- **Singleton Pattern**: Ensures single instance of critical components
- **Strategy Pattern**: Flexible pricing without code modification
- **State Management**: Proper encapsulation of object states
- **System Design**: Breaking complex problems into manageable components

## 🔄 Extensibility

Easy to extend for:
- New vehicle types (Electric, Handicapped)
- Additional pricing strategies (Peak hours, Member discounts)
- Multiple payment methods
- Reservation systems

## 🏆 Best Practices Demonstrated

- **Single Responsibility**: Each class has one clear purpose
- **Open/Closed Principle**: Open for extension, closed for modification
- **Dependency Injection**: Strategies injected at runtime
- **Error Handling**: Graceful handling of edge cases

---

This implementation showcases how design patterns solve real-world problems while maintaining clean, extensible code architecture.