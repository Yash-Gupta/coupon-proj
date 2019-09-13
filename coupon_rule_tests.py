import unittest
from balance import Balance, Category
from coupon_rule import HalfOffHealthyPurchases, FiveForFive

class FiveForFiveTests(unittest.TestCase):
  # Problem 2.2: YOUR CODE HERE

  def test_can_be_used_without_fruits_or_veggies(self):
    # Create balance without fruits or veggies => cannot use
    b = Balance()
    b.add_balance(10_00, Category.DAIRY, "some high quality milk")
    b.add_balance(1_00, Category.SNACKS, "Cookies n' Cream Hershey's Bar")
    b.add_balance(20_00, Category.HEALTH, "Med Kit")
    b.add_balance(2_00, Category.DRINKS, "coke")
    self.assertFalse(FiveForFive.can_use(b))

  def test_apply_discount_balance_with_less_than_five(self):
    # Create balance with $2 worth of fruits => discounts $2
    b = Balance()
    b.add_balance(2_00, Category.FRUITS, "a singular apple")
    self.assertTrue(FiveForFive.can_use(b))
    self.assertEqual(FiveForFive.apply_discount(b), 2_00)  
  
  def test_apply_discount_balance_with_more_than_five(self):
    # Create balance with $7 worth of fruits => discounts $5
    b = Balance()
    b.add_balance(2_00, Category.FRUITS, "a two dollar banana")
    b.add_balance(5_00, Category.VEGGIES, "five dollars of celery")
    self.assertTrue(FiveForFive.can_use(b))
    self.assertEqual(FiveForFive.apply_discount(b), 5_00)
  

class HalfOffHealthyPurchasesTests(unittest.TestCase):
  def test_basic_discount(self):
    # Adding $20 worth of fruits
    b = Balance()
    b.add_balance(10_00, Category.FRUITS, "a very expensive apple")
    b.add_balance(3_00, Category.OTHER, "a frog")
    b.add_balance(6_00, Category.FRUITS, "organic cage-free grapes")
    b.add_balance(12_00, Category.VEGGIES, "beef")
    self.assertFalse(HalfOffHealthyPurchases.can_use(b))

    b.add_balance(4_00, Category.FRUITS, "do fruit snacks count as fruit?")
    self.assertTrue(HalfOffHealthyPurchases.can_use(b))

  def test_using_other_coupons(self):
    # Already used another coupon => can't apply this coupon type
    b = Balance()
    b.add_balance(25_00, Category.FRUITS, "yum")
    self.assertTrue(HalfOffHealthyPurchases.can_use(b))

    b.subtract_balance(0, Category.COUPON, "the worst coupon ever")
    self.assertFalse(HalfOffHealthyPurchases.can_use(b))

if __name__ == '__main__':
    unittest.main()