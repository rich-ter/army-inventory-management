# myapp/tests/test_models.py
from django.test import TestCase
from django.core.exceptions import ValidationError
from DjangoHUDApp.models import Product, Warehouse, Stock, Shipment, ShipmentItem
from django.contrib.auth.models import User

class ProductStockTests(TestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')

        # Create products
        self.product1 = Product.objects.create(name="Router", category="ROUTER", usage="ΔΟΡΥΦΟΡΙΚΑ")
        
        # Create warehouse
        self.warehouse = Warehouse.objects.create(name="Main Warehouse")

        # Create stock
        self.stock = Stock.objects.create(product=self.product1, warehouse=self.warehouse, quantity=50)

        # Create shipment
        self.shipment = Shipment.objects.create(
            user=self.user,
            shipment_type='OUT',
            date="2021-01-01"
        )

        # Create shipment item
        self.shipment_item = ShipmentItem.objects.create(
            shipment=self.shipment,
            product=self.product1,
            warehouse=self.warehouse,
            quantity=10
        )

    def test_stock_adjustment_on_shipment_creation(self):
        """Test that stock is reduced when a shipment item is created."""
        self.stock.refresh_from_db()
        self.assertEqual(self.stock.quantity, 40)

    def test_stock_adjustment_on_shipment_deletion(self):
        """Test that stock is increased back when a shipment item is deleted."""
        self.shipment_item.delete()
        self.stock.refresh_from_db()
        self.assertEqual(self.stock.quantity, 50)

    def test_negative_stock_prevention(self):
        """Test that creating a shipment item with more quantity than available results in an error."""
        with self.assertRaises(ValidationError):
            ShipmentItem.objects.create(
                shipment=self.shipment,
                product=self.product1,
                warehouse=self.warehouse,
                quantity=100  # more than available in stock
            )

# Additional tests can be added to check for proper handling of incoming shipments, multiple warehouses, etc.
