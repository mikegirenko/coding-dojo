class Inventory:
    def __init__(self, current_day):
        self.quality = ("na", "very low", "low", "medium", "high")
        self.number_of_days = 30
        self.first_day = 1
        self.current_day = current_day
        self.inventory = [{"name": "item 1", "sell_in": 3, "quality": self.quality[4]}]

    def decrease_sell_in_and_quality(self):
        self.inventory[0]["sell_in"] = 2
        self.inventory[0]["quality"] = self.quality[3]

    def sell_date_passed(self):
        sell_date_passed = False
        this_item = self.inventory[0]
        if self.current_day > this_item["sell_in"]:
            sell_date_passed = True
        return sell_date_passed
