"""dict_methods is a set of functions to manage a users shopping cart items."""
from collections.abc import Iterable


def add_item(current_cart: dict[str, int], items_to_add: Iterable[str]) -> dict[str, int]:
    """Add items to shopping cart"""
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes: Iterable[str]) -> dict[str, int]:
    """Create user cart from an iterable notes entry"""
    return dict.fromkeys(notes, 1)


def update_recipes(ideas: dict[str, dict[str, int]], recipe_updates: Iterable[tuple[str, dict[str, int]]]) -> dict[str, dict[str, int]]:
    """Update the recipe ideas dictionary"""
    return ideas | dict(recipe_updates)
    


def sort_entries(cart: dict[str, int]) -> dict[str, int]:
    """Sort a users shopping cart in alphabetically order"""
    return dict(sorted(cart.items()))


def send_to_store(cart: dict[str, int], isle_mapping: dict[str, tuple[str, bool]]) -> dict[str, tuple[int, str, bool]]:
    """Combine users order to isle and refrigeration information"""
    fulfillment_cart = {}
    for item, quantity in cart.items():
        fulfillment_cart[item] = [quantity, *isle_mapping[item]]
    return dict(sorted(fulfillment_cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart: dict[str, tuple[int, str, bool]], store_inventory: dict[str, tuple[int, str, bool]]) -> dict[str, tuple[int | str, str, bool]]:
    """Update store inventory levels with user order"""
    for item, (quantity, _, _) in fulfillment_cart.items():
        store_inventory[item][0] = store_inventory[item][0] - quantity or 'Out of Stock'
    return store_inventory
