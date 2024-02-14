import random

# Binary Search Implementation
def binary_search(products,target_sku):
    low, high = 0, len(products) - 1
    # Binary search loop
    while low <= high:        
        mid = (low + high) // 2 # Calculate the middle index  
        current_sku = products[mid]["sku"] # Get the current sku at the middle index
        
        if current_sku == target_sku: return products[mid]
        # Adjust the search range based on the comparison with target sku        
        if current_sku >= target_sku: 
            high = mid - 1 # Move to the left half  
        else: low = mid + 1  # Move to the right half

    return None


# Inventory Initialization
inventory_length = random.randint(10, 99) 
products = []  # define list of products

for i in range(inventory_length):   

    sku = f'SKU{i+1:03}'  # ':03' specifies the width of the field, ensuring the resulting string is at least 3 characters wide.
    product_name = f'Product{i+1}'
    price = round(random.uniform(10.0, 100.0), 2) 
    quantity = random.randint(1, 50)  

    product = {'sku': sku, 'product_name': product_name, 'price': price, 'quantity': quantity}
    products.append(product)


# Test Initialization

# Test Case 1 - Successful Search
product  = random.choice(products)
result_1 = binary_search(products,product["sku"])
assert result_1 == product, f"Test Case 1 failed: Expected , got {result_1}" 

# Test Case 2 - Unsuccessful Search
product  = "SKU100000"
result_2 =  binary_search(products,product)
assert result_2 == None, f"Test Case 2 failed: Expected , got {result_2}" 

# Test Case 3 - Efficiency Measurement
product = products[0]["sku"]
comparisons_list = []

for _ in range(10):
    comparisons = binary_search(products, product)
    comparisons_list.append(comparisons)

average_comparisons = sum([len(comparisons) for comparisons in comparisons_list]) / len(comparisons_list)
print(f"Average number of comparisons for Test Case 3: {average_comparisons}")
    

# Test Case 4 - Edge Cases
# perform Binary Search for a product with the highest SKU value
product  = products[0]["sku"]
result_4_1 = binary_search(products,product)
assert result_4_1["sku"] == product, f"Test Case 4 failed: Expected , got {result_4_1}" 

# perform Binary Search for a product with the lowest SKU value
product  = products[-1]["sku"]
result_4_1 = binary_search(products,product)
assert result_4_1["sku"] == product, f"Test Case 4 failed: Expected , got {result_4_1}" 


print("All test cases passed successfully!")