# Coupon-Proj

A project to help solve DC Central Kitchen's biggest challenges: <i> coupon tracking.</i> This will contain the backend for a digital store and coupon tracking service.

## Overview

This service will allow customers to purchase items from a store. They may use any coupons during this purchase, and the store can reward customers with coupons at the end of the purchase.

The final product looks like this: ![Final Product](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fce5dd3a5-bf5c-4326-83c5-706cda059a2b%2FUntitled.png?table=block&id=65d1b29a-1267-4023-825f-8b89435ed844&width=2880&cache=v2)


## Structure

The hierarchy of the codebase can be shown below. ![UML Class Hierarchy of Coupon-Proj](https://www.lucidchart.com/publicSegments/view/a45c4ac1-b423-4132-a14a-be00ebccd228/image.png)

It becomes apparent that Store Managers are at the top of the hierarchy since they manage all the different stores they are in charge of. On the side, there is a helper file which contains important constants used throughout the program and a helper function. There is also an example file which is used to test the code. Below are notes on the important classes, and what each does in context of the app as a whole.

**Store Manager:** Registers stores and issue them a stock of coupons.

**Store:** Contains an inventory of available coupons in stock and a database of items. Adds coupons to inventory and rewards customers with coupons (if they're in stock).

**Sale:** Scans items, uses coupons, and rewards customers with coupons from the store at the end of the sale.

**Customer:** Starts a balance. Maintains a list of coupons and uses coupons.

**Balance:** Adds items to the balance when they are scanned. Uses coupons when applicable

**Coupon Generator:** Generates a unique coupon with a rule

**Coupon:** A coupon object that is unique by code and follows a certain rule

**Coupon Rule:** Contains a list of instructions for how certain coupon types work

## Sample Workflow:
1. A Customer object is created, initialized with a name, a default of 0 coupons, and a starting balance.
2. A Store object is created, initialized with a name and database of items.
3. A Store Mananger object is created, and they register this new store (so it is valid).
4. When the Store object is registered, it is issued a standard amount of coupons as their initial stock.
5. A Sale object is created and initiated, passing in the Customer and the Store.
6. A list of barcodes are scanned, and the Sale object scans each barcode.
7. The Sale checks if the barcode is valid through the store's database of items, and then adds the item to the Balance.
8. The Balance keeps track of all additions and deductions throughout the entire sale.
9. After all items are scanned, the Sale iterates through the Customer's Coupons.
10. Each Coupon object has a type (HalfOffHealthyPurchases, TenOffPromo, FiveForFive), all of which behave according to certain rules. For example, whether a Coupon can be used or not, and how much a Coupon would discount from the Balance.
11. When each Coupon is used, the appropriate discount is calculated and is added as a 'negative' item to the Balance (thereby lowering the Balance).
12. Once Coupons are applied, the Sale is finished. The Sale's Balance is then deducted from the Customer's personal Balance.
13. The Sale then calculates what Coupons to reward to the Customer, and issues them from the Store's stock. These Coupons are now added to the Customer's personal stock of Coupons.
14. The entire Sale is printed with some polishing and the workflow is finished!

