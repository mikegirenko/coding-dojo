from gilded_rose.code.inventory import Inventory


def test_update_inventory():
    current_inventory = [{"name": "Conjured", "sell_in": 2, "quality": 4}]
    inventory_object = Inventory(1, current_inventory)
    inventory_object.update_inventory()
    assert inventory_object.inventory[0]["sell_in"] == 1
    assert inventory_object.inventory[0]["quality"] == 2

