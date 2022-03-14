from gilded_rose.code.inventory import Inventory, QUALITY

CURRENT_INVENTORY = [{"name": "item 1", "sell_in": 3, "quality": QUALITY[4]},
                     {"name": "item 2", "sell_in": 5, "quality": QUALITY[3]}
                     ]


def test_return_one_inventory_item_by_name():
    inventory_object = Inventory(4, CURRENT_INVENTORY)
    name = "item 1"
    assert inventory_object.return_one_inventory_item_by_name(name) == CURRENT_INVENTORY[0]


def test_sell_in_value():
    this_inventory = Inventory(4, CURRENT_INVENTORY).inventory
    assert this_inventory[0]["sell_in"] == 3


def test_quality():
    this_inventory = Inventory(4, CURRENT_INVENTORY).inventory
    assert this_inventory[0]["quality"] == QUALITY[4]


def test_system_lowers_sell_in():
    inventory_object = Inventory(4, CURRENT_INVENTORY)
    inventory_object.decrease_sell_in()
    assert inventory_object.inventory[0]["sell_in"] == 2
    assert inventory_object.inventory[1]["sell_in"] == 4


def test_system_lowers_quality_when_sell_date_not_passed():
    inventory_object = Inventory(2, CURRENT_INVENTORY)
    inventory_object.decrease_quality()
    assert inventory_object.inventory[0]["quality"] == QUALITY[3]


def test_system_lowers_quality_when_sell_date_passed():
    inventory_object = Inventory(4, CURRENT_INVENTORY)
    inventory_object.decrease_quality()
    assert inventory_object.inventory[0]["quality"] == QUALITY[2]


def test_sell_date_passed_when_should():
    inventory_object = Inventory(4, CURRENT_INVENTORY)
    assert inventory_object.sell_date_passed()


def test_sell_date_not_passed_when_should_not():
    inventory_object = Inventory(2, CURRENT_INVENTORY)
    assert not inventory_object.sell_date_passed()
