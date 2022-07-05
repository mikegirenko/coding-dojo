class Inventory:
    def __init__(self, current_day, current_inventory):
        self.number_of_days = 30
        self.first_day = 1
        self.current_day = current_day
        self.inventory = current_inventory

    def return_one_inventory_item_by_name(self, name):
        inventory = self.inventory
        for item in inventory:
            if item["name"] == name:
                return item

    def decrease_sell_in(self):
        # for each day starting on first day and ending on current day
        day_counter = 1
        while day_counter <= self.current_day:
            for item in self.inventory:
                current_sell_in = item["sell_in"]
                item["sell_in"] = current_sell_in - 1
            day_counter += 1

    def update_quality(self):
        # for each day starting on first day and ending on current day
        day_counter = 1
        while day_counter <= self.current_day:
            for item in self.inventory:
                current_quality = item["quality"]
                if current_quality == 50:
                    return
                if item["name"] == "Aged Brie":
                    item["quality"] = current_quality + 1
                    return
                if current_quality != 0:
                    if self.sell_date_passed():
                        if current_quality == 0 or current_quality == 1:
                            item["quality"] = 0
                        else:
                            item["quality"] = current_quality - 2
                    if not self.sell_date_passed():
                        if current_quality == 0 or current_quality == 1:
                            item["quality"] = 0
                        else:
                            item["quality"] = current_quality - 1
            day_counter += 1

    def sell_date_passed(self):
        sell_date_passed = False
        for item in self.inventory:
            if self.current_day > item["sell_in"]:
                sell_date_passed = True
        return sell_date_passed
