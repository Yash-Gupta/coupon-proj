from coupon_generator import CouponGenerator
from coupon import Coupon
from coupon_rule import HalfOffHealthyPurchases, TenOffPromo, FiveForFive
from store import Store
from helpers import Singleton

COUPON_CODE_LENGTH = 10
INITIAL_COUPON_STOCK = {
  HalfOffHealthyPurchases: 50,
  TenOffPromo: 50,
  FiveForFive: 100
}

class StoresManager(metaclass=Singleton):
  def __init__(self) -> None:
    self.generator = CouponGenerator(COUPON_CODE_LENGTH)
    self.stores = set()

  def register_store(self, store: Store) -> None:
    if not store in self.stores:
      self.stores.add(store)
      self.issue_coupons(store)

  def issue_coupons(self, store: Store) -> None:
    # Problem 1.1: YOUR CODE HERE
    assert store in self.stores, f"Cannot issue coupons to {store.name} since {store.name} is not registered!"

    # populate initial coupon stock for each type of coupon
    for rule, coupon_amount in INITIAL_COUPON_STOCK.items():
      coupons_list = []
      for i in range(coupon_amount):
        coupons_list += [self.generator.generate_coupon(rule)]
      store.add_coupons_to_inventory(coupons_list, rule)

