QUALITY = ("zero", "very low", "low", "medium", "high")


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
        for item in self.inventory:
            current_sell_in = item["sell_in"]
            item["sell_in"] = current_sell_in - 1

    def update_quality(self):
        for item in self.inventory:
            current_quality = item["quality"]
            current_quality_index = QUALITY.index(current_quality)
            if item["name"] == "Aged Brie":
                item["quality"] = QUALITY[current_quality_index + 1]
                return
            if current_quality != "zero":
                if self.sell_date_passed():
                    item["quality"] = QUALITY[current_quality_index - 2]
                else:
                    item["quality"] = QUALITY[current_quality_index - 1]

    def sell_date_passed(self):
        sell_date_passed = False
        for item in self.inventory:
            if self.current_day > item["sell_in"]:
                sell_date_passed = True
        return sell_date_passed

# TODO: next is The Quality of an item is never more than 50
