# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = {
        "A": {
            "price": 50,
            "deal": {
                "amount": 3,
                "saved": 20,
            },
        },
        "B": {
            "price": 30,
            "deal": {
                "amount": 2,
                "saved": 15,
            },
        },
        "C": {
            "price": 20,
        },
        "D": {
            "price": 15,
        },
    }
    shop_cart = skus.split("")
    ordered_items = {}
    ordered_items["illegal_items"] = 0
    for item in shop_cart:
        if item not in items:
            ordered_items["illegal_items"] += 1
        ordered_items[item] = 0 if not ordered_items[item] else ordered_items[item] += 1
