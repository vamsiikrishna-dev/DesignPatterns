
from typing import Dict
import uuid

from Logger import ConsoleLogger
from .TicketManager import Ticket, TicketManager

from .ParkingFloor import ParkingFloor
from ChargeStrategy import ChargeStrategy, FixedChargeStrategy
from datetime import datetime
import threading

class ParkingSystem():

    instance = None
    _lock = threading.Lock()

    @staticmethod
    def get_instance():
        if ParkingSystem.instance is None:
            with ParkingSystem._lock:
                if ParkingSystem.instance is None:
                    ParkingSystem.instance = ParkingSystem()
        return ParkingSystem.instance
    
    def __init__(self):
        if ParkingSystem.instance is not None:
            raise Exception("ParkingSystem is a singleton")
        self.id = str(uuid.uuid4())
        self.floors: Dict[str, ParkingFloor] = {}
        self.payment_strategy: ChargeStrategy = FixedChargeStrategy()
        self.instance_lock = threading.Lock()
    
    def add_floor(self, floor:ParkingFloor):
        self.floors[floor.floor_id] = floor
        
    
    def set_payment(self, strategy: ChargeStrategy):
        self.payment_strategy = strategy

    def park_vehicle(self, vehicle_type, vehicle_id, time: datetime):
        with self.instance_lock:
            for floor in self.floors.values():
                ticket = floor.book_slot(vehicle_type, vehicle_id, time)
                if ticket:
                    return ticket
        return None
    
    def unpark_vehicle(self, ticket: Ticket):
        for floor in self.floors.values():
            state = floor.release_slot(ticket.parking_slot_id)
            if state:
                TicketManager.get_instance().invalidate_ticket(ticket)
                ConsoleLogger.get_instance().log(f"Successfully released slot {ticket.parking_slot_id}")
                return self.payment_strategy.calculate_charge(ticket)
            
        ConsoleLogger.get_instance().log(f"Invalid ticket got.")
                

    


    

