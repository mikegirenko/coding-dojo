QUALITY = ("na", "very low", "low", "medium", "high")


class Inventory:
    def __init__(self, current_day, current_inventory):
        self.number_of_days = 30
        self.first_day = 1
        self.current_day = current_day
        self.inventory = current_inventory

    def decrease_sell_in_and_quality(self):
        current_sell_in = self.inventory[0]["sell_in"]
        self.inventory[0]["sell_in"] = current_sell_in - 1
        current_quality_index = QUALITY.index("high")
        self.inventory[0]["quality"] = QUALITY[current_quality_index - 1]

    def sell_date_passed(self):
        sell_date_passed = False
        this_item = self.inventory[0]
        if self.current_day > this_item["sell_in"]:
            sell_date_passed = True
        return sell_date_passed

    def return_one_inventory_item_by_name(self, name):
        inventory = self.inventory
        for item in inventory:
            if item["name"] == name:
                return item

# TODO once the sell by date has passed, Quality degrades twice as fast
