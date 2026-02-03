import uuid
from datetime import datetime

from Logger import ConsoleLogger

class Ticket():
    def __init__(self,vehicle_number, parking_slot_id, slot_type, date = datetime.now()):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle_number = vehicle_number
        self.parking_slot_id = parking_slot_id
        self.parking_slot_type = slot_type
        self.issued_time = date
    
    def __str__(self):
        return f"id: {self.ticket_id}, vehicle_number: {self.vehicle_number} and issued at :{self.issued_time}"

class TicketManager():
    instance = None

    @staticmethod
    def get_instance():
        if TicketManager.instance is None:
            TicketManager.instance = TicketManager()
        return TicketManager.instance

    def __init__(self):
        self.tickets = {}

    def create_ticket(self, vehicle_number, parking_slot_id, slot_type, date):
        ticket = Ticket(vehicle_number, parking_slot_id, slot_type, date)
        self.tickets[ticket.ticket_id] = ticket
        return ticket
    
    def invalidate_ticket(self,ticket:Ticket):
        id = ticket.ticket_id
        del self.tickets[id]
        ConsoleLogger.get_instance().log(f"Ticket with id {id} invalidated successfully")
        return True
    

