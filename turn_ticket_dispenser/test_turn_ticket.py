import unittest

from turn_ticket_dispenser.turn_ticket import *


class TicketDispenserTest(unittest.TestCase):

    def test_turn_ticket(self):
        ticket_number_object = TurnTicket(0)
        assert ticket_number_object.turn_number == 0

    def test_turn_number_sequence_returns_default_number(self):
        next_turn_number_object = TurnNumberSequence()
        assert next_turn_number_object.next_turn_number() == 0

    def test_do_something(self):
        dispenser = TicketDispenser()
        ticket = dispenser.getTurnTicket()
        assert not ticket


if __name__ == "__main__":
	unittest.main()
