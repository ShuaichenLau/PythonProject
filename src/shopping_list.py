class ShoppingList:
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    def get_item_count(self):
        return len(self.shopping_list)

    def contains_item(self, item_name):
        return item_name in self.shopping_list

    def get_item_total_price(self):
        total_price = 0
        for item in self.shopping_list.values():
            total_price += item
        return total_price
