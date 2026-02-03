import time
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from System import Ticket
from .ChargeStrategy import ChargeStrategy
from datetime import datetime
from Enums import ParkingSlotType

class DynamicChargeStrategy(ChargeStrategy):

    def __init__(self):
        self.hourly_rate_map = {}
        self.hourly_rate_map[ParkingSlotType.SMALL] = 20
        self.hourly_rate_map[ParkingSlotType.MEDIUM] = 30
        self.hourly_rate_map[ParkingSlotType.LARGE] = 40

    def calculate_charge(self, ticket: 'Ticket'):
        #calculation logic
        cur_time = datetime.now()
        issued_time = ticket.issued_time
        diff_sec = cur_time - issued_time

        diff_hrs = diff_sec.total_seconds()/3600
        hourly_rate = self.hourly_rate_map[ticket.parking_slot_type]
        cost = round(diff_hrs * hourly_rate,2)
        return cost