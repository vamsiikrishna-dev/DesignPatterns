
from typing import Dict
import uuid

from Logger import ConsoleLogger
from .TicketManager import Ticket

from .ParkingFloor import ParkingFloor
from ChargeStrategy import ChargeStrategy, FixedChargeStrategy
from datetime import datetime


class ParkingSystem():

    instance = None

    @staticmethod
    def get_instance():
        if ParkingSystem.instance is None:
            ParkingSystem.instance = ParkingSystem()
        return ParkingSystem.instance
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.floors: Dict[str, ParkingFloor] = {}
        self.payment_strategy: ChargeStrategy = FixedChargeStrategy()
    
    def add_floor(self, floor:ParkingFloor):
        self.floors[floor.floor_id] = floor
        
    
    def set_payment(self, strategy: ChargeStrategy):
        self.payment_strategy = strategy

    def park_vehicle(self, vehicle_type, vehicle_id, time: datetime):
        for floor in self.floors.values():
            ticket = floor.book_slot(vehicle_type, vehicle_id, time)
            if ticket:
                return ticket
        return None
    
    def unpark_vehicle(self, ticket: Ticket):
        for floor in self.floors.values():
            state = floor.release_slot(ticket.parking_slot_id)
            if state:
                ConsoleLogger.get_instance().log(f"Successfully released slot {ticket.parking_slot_id}")
                return self.payment_strategy.calculate_charge(ticket)
            
        ConsoleLogger.get_instance().log(f"Invalid ticket got.")
                

    


    

