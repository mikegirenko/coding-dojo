from gilded_rose.code.inventory import Inventory, QUALITY

CURRENT_INVENTORY = [{"name": "item 1", "sell_in": 3, "quality": QUALITY[4]}]


def test_inventory():
    assert Inventory(1, CURRENT_INVENTORY).inventory
