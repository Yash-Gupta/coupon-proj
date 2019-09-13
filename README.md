# Coupon-Proj

A project to help solve DC Central Kitchen's biggest challenges: <i> coupon tracking.</i> This will contain the backend for a digital store and coupon tracking service.

## Overview

This service will allow customers to purchase items from a store. They may use any coupons during this purchase, and the store can reward customers with coupons at the end of the purchase.

The final product looks like this: ![Final Product](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fce5dd3a5-bf5c-4326-83c5-706cda059a2b%2FUntitled.png?table=block&id=65d1b29a-1267-4023-825f-8b89435ed844&width=2880&cache=v2)


## Structure

The hierarchy of the codebase can be shown below. ![UML Class Hierarchy of Coupon-Proj](https://www.lucidchart.com/publicSegments/view/a45c4ac1-b423-4132-a14a-be00ebccd228/image.png)

It becomes apparent that Store Managers are at the top of the hierarchy since they manage all the different stores they are in charge of. On the side, there is a helper file which contains important constants used throughout the program and a helper function. There is also an example file which is used to test the code. Below are my notes on the important classes, and what each does in context of the app as a whole.

**Store Manager:** Registers stores and issue them a stock of coupons.

**Store:** Contains an inventory of available coupons in stock and a database of items. Adds coupons to inventory and rewards customers with coupons (if they're in stock).

**Sale:** Scans items, uses coupons, and rewards customers with coupons from the store at the end of the sale.

**Customer:** Starts a balance. Maintains a list of coupons and uses coupons.

**Balance:** Adds items to the balance when they are scanned. Uses coupons when applicable

**Coupon Generator:** Generates a unique coupon with a rule

**Coupon:** A coupon object that is unique by code and follows a certain rule

**Coupon Rule:** Contains a list of instructions for how certain coupon types work
