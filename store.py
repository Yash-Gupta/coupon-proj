from coupon import Coupon
from coupon_rule import CouponRule
from customer import Customer
from helpers import NAMESPACE_ID
from store_database import StoreDatabase
from typing import List, Type
import uuid

class Store:
  """
  A Store has a set inventory of coupons and a database of items. It can reward customers from its stock
  and add items from its inventory to a Sale's Balance.
  """
  def __init__(self, name: str, database: StoreDatabase) -> None:
    self.uuid = uuid.uuid5(NAMESPACE_ID, name)
    self.name = name
    self.database = database
    self.coupon_inventory = {}

  def add_coupons_to_inventory(self, coupons: List[Coupon], rule: Type[CouponRule]) -> None:
    self.coupon_inventory[rule] = self.coupon_inventory.get(rule, []) + coupons

  def available_coupon_types(self) -> List[Type[CouponRule]]:
    return list(filter(lambda rule: len(self.coupon_inventory[rule]) > 0, self.coupon_inventory.keys()))

  def reward_coupons(self, customer: Customer, rule: Type[CouponRule], num: int) -> List[Coupon]:

    assert num >= 0, f"Cannot award {num} coupons since {num} < 0!"

    # Initialize empty list of coupons
    coupons_list = []
    coupon_rule_length = len(self.coupon_inventory[rule])

    # If store's coupons for that type are less than what customer needs, return a list of all coupons for that type
    if num >= coupon_rule_length:
      coupons_list = self.coupon_inventory[rule]
      del self.coupon_inventory[rule]

    # If not, return the first num coupons from the store, and remove it from the store
    else:
      coupons_list = self.coupon_inventory[rule][0:num]
      self.coupon_inventory[rule] = self.coupon_inventory[rule][num:coupon_rule_length]

    customer.add_coupons(coupons=coupons_list)
    return coupons_list

  def __hash__(self) -> int:
    return hash(self.uuid)

  def __eq__(self, other: 'Store') -> bool:
    return self.uuid == other.uuid
