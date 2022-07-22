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
            "count": 0,
        },
        "B": {
            "price": 30,
            "deal": {
                "amount": 2,
                "saved": 15,
            },
            "count": 0,
        },
        "C": {"price": 20, "count": 0},
        "D": {"price": 15, "count": 0},
    }
    output = 0
    for item in skus:
        if item not in items or item.islower():
            print("illegal item found")
            return -1
        else:
            output += items[item]["price"]
            items[item]["count"] += 1
            if (
                "deal" in items[item]
                and items[item]["count"] == items[item]["deal"]["amount"]
            ):
                items[item]["count"] = 0
                output -= items[item]["deal"]["saved"]

    return output




