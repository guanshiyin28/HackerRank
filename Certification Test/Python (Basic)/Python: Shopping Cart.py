#!/bin/python3

import math
import os
import random
import re
import sys



class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        """Returns a string representation of the item for informative output."""
        return f"{self.name} (${self.price:.2f})"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def __len__(self):
        """Returns the number of items in the cart."""
        return len(self.items)

    def total(self):
        """Calculates and returns the total price of all items in the cart."""
        total_price = sum(item.price for item in self.items)
        return total_price

    def add(self, item):
        """Adds an item to the shopping cart."""
        self.items.append(item)

    def remove(self, item_name):
        """Removes an item from the cart by name, handling potential errors."""
        try:
            item_to_remove = next(item for item in self.items if item.name == item_name)
            self.items.remove(item_to_remove)
            print(f"Removed {item_name} from the cart.")
        except StopIteration:
            print(f"Item '{item_name}' not found in the cart.")
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(len(cart)) + "\n")
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)
            
    fptr.close()
