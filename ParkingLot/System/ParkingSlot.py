from Enums import ParkingSlotType, ParkingSlotState
import uuid

class ParkingSlot():
    def __init__(self,slot_type: ParkingSlotType):
        self.slot_id = str(uuid.uuid4())
        self.parking_slot_type = slot_type
        self.parking_slot_state = ParkingSlotState.EMPTY
    
    def get_id(self):
        return self.slot_id
    
    def set_type(self,slot_type):
        self.parking_slot_type = slot_type
    
    def get_type(self):
        return self.parking_slot_type
    
    def set_state(self,state):
        self.parking_slot_state = state
    
    def get_state(self):
        return self.parking_slot_state
