import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  """ ------------ unit test for getDataPoint() method ------------ """
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Assertion is added below for the testing process ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Assertion is added below for the testing process ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


  """ ------------ unit test for getRatio() method ------------ """
  def test_getRatio_calculateRatio(self):
    # price_A = [117.38, 118.95]
    # price_B = [116.325, 117.445]
    # result = [1.0090694175800559, 1.0128145089190685]
    testUnits = [
      {'priceA': 117.38, 'priceB': 116.325, 'ratio': 1.0090694175800559},
      {'priceA': 118.95, 'priceB': 117.445, 'ratio': 1.0128145089190685}
    ]
    for unit in testUnits:
      self.assertEqual(getRatio(unit['priceA'],unit['priceB']), unit['ratio'])


  def test_getRatio_calculateRatioPriceAandBareZero(self):
    testUnits = [
      {'priceA': 117.38, 'priceB': 0, 'ratio': None},
      {'priceA': 0, 'priceB': 117.38, 'ratio': 0}
    ]
    for unit in testUnits:
      self.assertEqual(getRatio(unit['priceA'],unit['priceB']), unit['ratio'])


if __name__ == '__main__':
    unittest.main()
