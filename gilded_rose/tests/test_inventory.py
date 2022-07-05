from gilded_rose.code.inventory import Inventory


def test_return_one_inventory_item_by_name():
    current_inventory = [{"name": "Bread", "sell_in": 3, "quality": 4},
                         {"name": "Salami", "sell_in": 5, "quality": 3},
                         {"name": "Aged Brie", "sell_in": 3, "quality": 2}]
    inventory_object = Inventory(4, current_inventory)
    name = "Bread"
    assert inventory_object.return_one_inventory_item_by_name(name) == current_inventory[0]


def test_inventory_item_has_sell_in_value():
    current_inventory = [{"name": "Spam", "sell_in": 3, "quality": 4}]
    inventory_object = Inventory(4, current_inventory).inventory
    assert inventory_object[0]["sell_in"] == current_inventory[0]["sell_in"]


def test_inventory_item_has_quality_value():
    expected_quality = 4
    current_inventory = [{"name": "Bread", "sell_in": 3, "quality": expected_quality}]
    inventory_object = Inventory(4, current_inventory).inventory
    assert inventory_object[0]["quality"] == expected_quality


def test_system_lowers_sell_in_value_for_each_inventory_item():
    current_inventory = [{"name": "Bread", "sell_in": 3, "quality": 4},
                         {"name": "Salami", "sell_in": 2, "quality": 3}]
    inventory_object = Inventory(2, current_inventory)
    inventory_object.decrease_sell_in()
    assert inventory_object.inventory[0]["sell_in"] == 1
    assert inventory_object.inventory[1]["sell_in"] == 0


def test_system_lowers_quality_when_sell_date_not_passed():
    current_inventory = [{"name": "Bread", "sell_in": 2, "quality": 4},
                         {"name": "Salami", "sell_in": 4, "quality": 3},
                         {"name": "Cheese", "sell_in": 2, "quality": 2}]
    inventory_object = Inventory(1, current_inventory) # 2 here is less than sell_in of each item
    inventory_object.update_quality()
    assert inventory_object.inventory[0]["quality"] == 3
    assert inventory_object.inventory[1]["quality"] == 2
    assert inventory_object.inventory[2]["quality"] == 1


def test_system_lowers_quality_twice_faster_when_sell_date_passed():
    current_inventory = [{"name": "Bread", "sell_in": 0, "quality": 4},
                         {"name": "Salami", "sell_in": 0, "quality": 3}]
    inventory_object = Inventory(1, current_inventory) # 4 here is more than sell_in of each item
    inventory_object.update_quality()
    assert inventory_object.inventory[0]["quality"] == 2
    assert inventory_object.inventory[1]["quality"] == 1


def test_sell_date_passed_return_true_when_sell_date_passed():
    current_inventory = [{"name": "Bread", "sell_in": 3, "quality": 4}]
    inventory_object = Inventory(4, current_inventory)
    assert inventory_object.sell_date_passed()


def test_sell_date_passed_does_not_return_true_when_sell_date_not_passed():
    current_inventory = [{"name": "Bread", "sell_in": 5, "quality": 4}]
    inventory_object = Inventory(4, current_inventory)
    assert not inventory_object.sell_date_passed()


def test_aged_brie_increases_in_quality_the_older_it_get():
    current_inventory = [{"name": "Aged Brie", "sell_in": 3, "quality": 2}]
    inventory_object = Inventory(2, current_inventory)
    inventory_object.update_quality()
    assert inventory_object.return_one_inventory_item_by_name("Aged Brie")["quality"] == 3


def test_quality_of_an_item_never_negative():
    current_inventory = [{"name": "Bread", "sell_in": 1, "quality": 1},
                         {"name": "Salami", "sell_in": 1, "quality": 0}]
    inventory_object = Inventory(5, current_inventory)
    inventory_object.update_quality()
    assert inventory_object.inventory[0]["quality"] == 0
    assert inventory_object.inventory[1]["quality"] == 0


def test_quality_of_an_item_is_never_more_than_fifty():
    current_inventory = [{"name": "Aged Brie", "sell_in": 1, "quality": 49}]
    inventory_object = Inventory(2, current_inventory)
    inventory_object.update_quality()
    assert inventory_object.inventory[0]["quality"] == 50
