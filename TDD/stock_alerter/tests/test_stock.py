import unittest
from datetime import datetime
from ..stock import Stock


class StockTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock("GOOG")

    def tearDown(self):
        pass

    def test_price_of_a_new_stock_class_should_be_none(self):
        self.assertIsNone(self.goog.price)

    def test_stock_update(self):
        """
        An update should set teh price on the stock object
        We will be using the `datetime` module for timestamp
        """
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.assertEqual(10, self.goog.price)

    def test_negative_price_should_throw_ValueError(self):
        # try:
        #     self.goog.update(datetime(2014, 2, 12), price=-1)
        # except ValueError:
        #     return
        # self.fail("ValueError was not raise when price is negative")
        # self.assertRaises(ValueError, self.goog.update, datetime(2014, 2, 12), -1)
        with self.assertRaises(ValueError):
            self.goog.update(datetime(2014, 2, 12), price=-1)

    def test_price_should_give_the_last_value(self):
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.goog.update(datetime(2014, 2, 12), price=8.4)
        self.assertAlmostEqual(8.4, self.goog.price, delta=0.0001)