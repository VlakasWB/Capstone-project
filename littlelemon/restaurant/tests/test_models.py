from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_menu_item_string_representation(self):
        menu_item = Menu.objects.create(
            title="IceCream", price=80, inventory=100)
        self.assertEqual(str(menu_item), "IceCream : 80")
