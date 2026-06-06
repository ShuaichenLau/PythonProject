import unittest

from shopping_list import ShoppingList

class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({"iphone4": 20, "iphone5": 30, "iphone6": 40})

    def test_get_item_contain(self):
        # self.shopping_list 是对象
        # 对象的 .shopping_list 属性才是那个真正的字典
        self.assertIn("iphone6", self.shopping_list.shopping_list.keys())

    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 3)

    def test_get_item_total_price(self):
        self.assertEqual(self.shopping_list.get_item_total_price(), 90)

    def test_contains_item(self):
        self.assertTrue(self.shopping_list.contains_item("iphone6"))
