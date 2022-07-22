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
    output = 0
    for item in skus:
        if item not in items:
            print("illegal item found")
            output -= 1
        else:
            output += items[item]["price"]
            items[item]["count"] = (
                1 if not "count" in items[item] else items[item]["count"] + 1
            )
        if (
            "deal" in items[item]
            and items[item]["count"] == items[item]["deal"]["amount"]
        ):
            output -= items[item]["deal"]["saved"]

    return output
