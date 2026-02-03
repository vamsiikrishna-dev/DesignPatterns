import uuid
from .ParkingSlot import ParkingSlot
from Enums import ParkingSlotType, ParkingSlotState
from typing import Dict
from Logger import ConsoleLogger
from .TicketManager import TicketManager
from datetime import datetime

class ParkingFloor():

    def __init__(self):
        self.floor_id = str(uuid.uuid4())
        self.slots:Dict[str, ParkingSlot] = {}
    
    def add_slot(self,slot:ParkingSlot):
        
        self.slots[slot.slot_id] = slot

    def book_slot(self, vehicle_type:ParkingSlotType, vehicle_id, date: datetime):
        empty_slots = [slot for slot in self.slots.values() if slot.get_type() == vehicle_type and slot.get_state() == ParkingSlotState.EMPTY]
        if empty_slots:
            slot = empty_slots[0]
            slot.set_state(ParkingSlotState.FILLED)
            return TicketManager.get_instance().create_ticket(vehicle_id,slot.get_id(), vehicle_type, date)
            
        else:
            ConsoleLogger.get_instance().log("No slot available for the vehicle type")
            return None
        
    
    def release_slot(self, slot_id):
        if slot_id in self.slots.keys():
            self.slots[slot_id].set_state(ParkingSlotState.EMPTY)
            return True
        else:
            return False

