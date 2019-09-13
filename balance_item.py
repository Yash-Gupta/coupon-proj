from helpers import format_money, DISPLAY_WIDTH
import balance

class BalanceItem:
  """
  Represents a single change (positive or negative) to a balance
  """
  def __init__(self, amount: int, category: 'Category', description: str) -> None:
    self.amount = amount
    self.category = category
    self.description = description

  def __str__(self) -> str:
    return f"{(self.description + ' ').ljust(DISPLAY_WIDTH - 10, '.')} {format_money(self.amount, sign=True)}"
