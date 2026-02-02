import time
import uuid
from datetime import datetime

class Ticket():
    def __init__(self,vehicle_number, parking_slot_id,date = datetime.now()):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle_number = vehicle_number
        self.parking_slot_id = parking_slot_id
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

    def create_ticket(self, vehicle_number, parking_slot_id, date):
        ticket = Ticket(vehicle_number, parking_slot_id, date)
        self.tickets[ticket.ticket_id] = ticket
        return ticket
    

