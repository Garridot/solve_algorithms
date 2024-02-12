# Test Scenario: Inventory Management System

## Background:

You are tasked with developing an inventory management system for an e-commerce platform. The system needs to efficiently find the quantity available for a particular product identified by its unique SKU (Stock Keeping Unit). To achieve this, you decide to implement the Binary Search algorithm to search through the sorted list of products.

## Test Objective:

1. **Algorithm Implementation:**
- Implement the Binary Search algorithm to search for a product's quantity based on SKU.
- Ensure that the inventory is maintained in a sorted order according to SKU.

2. **Search Efficiency:**
- Evaluate the efficiency of your Binary Search implementation by measuring the number of comparisons made during a search operation.

3. **Edge Cases Handling:**
- Test the algorithm's performance with edge cases, such as searching for a product with the highest and lowest SKU values.

## Test Steps:

1. **Initialization:**
- Create a sample inventory with at least 10 products, each identified by a unique SKU.
- Ensure that the inventory is initially sorted based on SKU.

2. **Test Case 1 - Successful Search:**
- Choose a random product from the inventory.
- Perform a Binary Search to find the quantity of the selected product.
- Verify that the correct quantity is retrieved.

3. **Test Case 2 - Unsuccessful Search:**
- Choose a random SKU that does not exist in the inventory.
- Perform a Binary Search to find the quantity of the non-existent product.
- Verify that the algorithm correctly indicates that the product is not found.

4. **Test Case 3 - Efficiency Measurement:**
- Choose a product and perform a Binary Search.
- Record the number of comparisons made during the search.
- Repeat the operation with different products and analyze the average number of comparisons.

5. **Test Case 4 - Edge Cases:**
- Perform Binary Search for a product with the highest SKU value.
- Perform Binary Search for a product with the lowest SKU value.
- Ensure the algorithm handles these edge cases correctly.

