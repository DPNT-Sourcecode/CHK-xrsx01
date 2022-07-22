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
    args = skus.split("")

