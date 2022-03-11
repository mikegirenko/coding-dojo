from gilded_rose.code.inventory import Inventory


def test_sell_in_value():
    this_inventory = Inventory(4).inventory
    assert this_inventory[0]["sell_in"] == 3


def test_quality():
    inventory_object = Inventory(4)
    inventory = inventory_object.inventory
    print(inventory)
    assert inventory[0]["quality"] == inventory_object.quality[4]


def test_system_lowers_sell_in_and_quality():
    inventory_object = Inventory(4)
    inventory_object.decrease_sell_in_and_quality()
    assert inventory_object.inventory[0]["sell_in"] == 2
    assert inventory_object.inventory[0]["quality"] == inventory_object.quality[3]


def test_sell_date_passed_when_should():
    inventory_object = Inventory(4)
    assert inventory_object.sell_date_passed()


def test_sell_date_not_passed_when_should_not():
    inventory_object = Inventory(2)
    assert not inventory_object.sell_date_passed()
