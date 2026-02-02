import time
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from System import Ticket
from .ChargeStrategy import ChargeStrategy
from datetime import datetime

class FixedChargeStrategy(ChargeStrategy):

    def __init__(self,hourly_rate = 20):
        self.hourly_rate = 20

    def calculate_charge(self, ticket: 'Ticket'):
        #calculation logic
        cur_time = datetime.now()
        issued_time = ticket.issued_time
        diff_sec = cur_time - issued_time
        diff_sec = diff_sec.total_seconds()
        diff_hrs = diff_sec/3600
        cost = round(diff_hrs * self.hourly_rate,2)
        return cost