class TurnTicket(object): #  this returns number
    def __init__(self, turn_number):
        self.turn_number = turn_number


class TurnNumberSequence(object):  # this increments number
    _turnNumber = -1

    @staticmethod
    def next_turn_number():
        TurnNumberSequence._turnNumber += 1

        return TurnNumberSequence._turnNumber


class TicketDispenser(object):
    def getTurnTicket(self):
        newTurnNumber = TurnNumberSequence.next_turn_number()  # ?
        newTurnTicket = TurnTicket(newTurnNumber)

        return newTurnTicket
