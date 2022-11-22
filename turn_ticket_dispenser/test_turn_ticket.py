import unittest
from unittest.mock import patch

from turn_ticket_dispenser.turn_ticket import *


class TicketDispenserTest(unittest.TestCase):

    def test_turn_ticket(self):
        ticket_number_object = TurnTicket(0)
        assert ticket_number_object.turn_number == 0

    def test_turn_number_sequence_returns_default_number(self):
        next_turn_number_object = TurnNumberSequence()
        assert next_turn_number_object.next_turn_number() == 0

    def test_ticket_dispenser_returns_ticket_number(self):
        dispenser = TicketDispenser()
        ticket = dispenser.getTurnTicket()
        assert ticket == 0

    def test_two_dispensers(self):
        dispenser_1 = TicketDispenser()
        dispenser_2 = TicketDispenser()
        ticket_1 = dispenser_1.getTurnTicket()
        ticket_2 = dispenser_2.getTurnTicket()
        assert ticket_1 == 0
        assert ticket_2 == 1
        assert ticket_1 != ticket_2


    @patch("turn_ticket_dispenser.turn_ticket.TurnNumberSequence.next_turn_number")
    def test_next_ticket(self, next_turn_number):
        next_turn_number.return_value = 100
        dispenser = TicketDispenser()
        ticket = dispenser.getTurnTicket()
        assert ticket == 100


if __name__ == "__main__":
    unittest.main()
