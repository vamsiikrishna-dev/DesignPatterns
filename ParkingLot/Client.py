import time
from Enums import ParkingSlotType
from System import ParkingSystem
from System import ParkingFloor
from System import ParkingSlot
from datetime import datetime

if __name__ == '__main__':
    system = ParkingSystem.get_instance()
    slot = ParkingSlot(ParkingSlotType.MEDIUM)

    floor = ParkingFloor()
    floor.add_slot(slot)

    system.add_floor(floor)

    ticket = system.park_vehicle(ParkingSlotType.MEDIUM, 'AP27PEK9409', datetime(2026,2,2,10))
    print(f"Ticket: {ticket}")
    cost = system.unpark_vehicle(ticket)

    print(cost)
    ticket = system.park_vehicle(ParkingSlotType.MEDIUM, 'TS27PEK9409', datetime(2026,2,2,10))
    print(f"Ticket: {ticket}")


    