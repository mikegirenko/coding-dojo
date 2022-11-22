class TurnTicket(object):
    def __init__(self, turn_number):
        self.turn_number = turn_number


class TurnNumberSequence(object):
    _turnNumber = -1

    @staticmethod
    def next_turn_number():
        TurnNumberSequence._turnNumber += 1

        return TurnNumberSequence._turnNumber


class TicketDispenser(object):
    def getTurnTicket(self):
        newTurnNumber = TurnNumberSequence.next_turn_number()
        newTurnTicket = TurnTicket(newTurnNumber).turn_number

        return newTurnTicket
