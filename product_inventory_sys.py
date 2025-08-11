# Product Inventory System
# You have a list of products with quantity and price:
# python
# CopyEdit
# inventory = [
# {"item": "Pen", "price": 5, "qty": 20},
# {"item": "Notebook", "price": 20, "qty": 10},
# {"item": "Pencil", "price": 3, "qty": 50}
# ]
# (a) Calculate and print the total value of each item (price × quantity).
# (b) Find the item with the highest total value.
# (c) Allow the user to update the quantity of any item.
inventory = [
{"item": "Pen", "price": 5, "qty": 20},
{"item": "Notebook", "price": 20, "qty": 10},
{"item": "Pencil", "price": 3, "qty": 50}
]
def totalvalue():
    for x in inventory:
        print(f"total value is {x['item']} is {x['price']*x['qty']}")

totalvalue()