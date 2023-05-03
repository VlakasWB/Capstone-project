from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuItemsViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = Menu.objects.create(
            title="IceCream", price=80, inventory=100)
        self.menu_item2 = Menu.objects.create(
            title="Pasta", price=120, inventory=50)

    def test_get_all_menu_items(self):
        response = self.client.get(reverse('menu-items'))
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
