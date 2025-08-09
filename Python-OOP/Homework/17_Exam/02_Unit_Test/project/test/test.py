import unittest
from project.legendary_item import LegendaryItem

class TestLegendaryItem(unittest.TestCase):
    def setUp(self):
        self.item = LegendaryItem("Sword-of-Power", 75, 80, 100)

    def test_constructor_with_valid_data(self):
        self.assertEqual(self.item.identifier, "Sword-of-Power")
        self.assertEqual(self.item.power, 75)
        self.assertEqual(self.item.durability, 80)
        self.assertEqual(self.item.price, 100)

    def test_identifier_setter_with_valid_data(self):
        self.item.identifier = "New-Blade-99"
        self.assertEqual(self.item.identifier, "New-Blade-99")

    def test_identifier_setter_with_invalid_characters(self):
        with self.assertRaises(ValueError) as cm:
            self.item.identifier = "Invalid!ID"
        self.assertEqual(str(cm.exception), "Identifier can only contain letters, digits, or hyphens!")

    def test_identifier_setter_with_short_length(self):
        with self.assertRaises(ValueError) as cm:
            self.item.identifier = "abc"
        self.assertEqual(str(cm.exception), "Identifier must be at least 4 characters long!")

    def test_power_setter_with_valid_data(self):
        self.item.power = 150
        self.assertEqual(self.item.power, 150)

    def test_power_setter_with_negative_value(self):
        with self.assertRaises(ValueError) as cm:
            self.item.power = -10
        self.assertEqual(str(cm.exception), "Power must be a non-negative integer!")

    def test_durability_setter_with_valid_data(self):
        self.item.durability = 50
        self.assertEqual(self.item.durability, 50)

    def test_durability_setter_with_value_too_low(self):
        with self.assertRaises(ValueError) as cm:
            self.item.durability = 0
        self.assertEqual(str(cm.exception), "Durability must be between 1 and 100 inclusive!")

    def test_durability_setter_with_value_too_high(self):
        with self.assertRaises(ValueError) as cm:
            self.item.durability = 101
        self.assertEqual(str(cm.exception), "Durability must be between 1 and 100 inclusive!")

    def test_price_setter_with_valid_data(self):
        self.item.price = 200
        self.assertEqual(self.item.price, 200)

    def test_price_setter_with_zero(self):
        with self.assertRaises(ValueError) as cm:
            self.item.price = 0
        self.assertEqual(str(cm.exception), "Price must be a multiple of 10 and not 0!")

    def test_price_setter_with_invalid_multiple(self):
        with self.assertRaises(ValueError) as cm:
            self.item.price = 15
        self.assertEqual(str(cm.exception), "Price must be a multiple of 10 and not 0!")

    def test_is_precious_property_when_precious(self):
        self.assertTrue(self.item.is_precious)

    def test_is_precious_property_when_not_precious(self):
        self.item.power = 49
        self.assertFalse(self.item.is_precious)

    def test_enhance_method_updates_attributes(self):
        initial_power = self.item.power
        initial_price = self.item.price
        initial_durability = self.item.durability

        self.item.enhance()

        self.assertEqual(self.item.power, initial_power * 2)
        self.assertEqual(self.item.price, initial_price + 10)
        self.assertEqual(self.item.durability, initial_durability + 10)

    def test_enhance_method_durability_cap(self):
        self.item.durability = 95
        self.item.enhance()
        self.assertEqual(self.item.durability, 100)

    def test_evaluate_method_with_eligible_item(self):
        result = self.item.evaluate(min_durability=70)
        self.assertEqual(result, "Sword-of-Power is eligible.")

    def test_evaluate_method_with_ineligible_item_low_durability(self):
        result = self.item.evaluate(min_durability=90)
        self.assertEqual(result, "Item not eligible.")

    def test_evaluate_method_with_ineligible_item_not_precious(self):
        self.item.power = 40  # Not precious
        result = self.item.evaluate(min_durability=70)
        self.assertEqual(result, "Item not eligible.")

    def test_evaluate_method_with_ineligible_item_both_conditions_fail(self):
        self.item.power = 40  # Not precious
        result = self.item.evaluate(min_durability=90)
        self.assertEqual(result, "Item not eligible.")


if __name__ == '__main__':
    unittest.main()