
import random
import time
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set the logging level to DEBUG for detailed output

def create_inventory(inventory_length):
    products = []  # define list of products

    for i in range(inventory_length):       
        sku = f'SKU{i+1:03}'  # ':03' specifies the width of the field, ensuring the resulting string is at least 3 characters wide.
        product_name = f'Product{i+1}'
        price = round(random.uniform(10.0, 100.0), 2) 
        quantity = random.randint(1, 50)  

        product = {'sku': sku, 'product_name': product_name, 'price': price, 'quantity': quantity}
        products.append(product)

    return products

def binary_search(products, target_sku): 
    """
    Perform binary search to find a product in the list of products based on SKU.

    Parameters:
    - products (list): The list of products to search through.
    - target_sku (str): The SKU of the product to find.

    Returns:
    - dict or None: The product dictionary if found, or None if not found.
    """

    # Initialize search boundaries
    low = 0
    high = len(products) - 1

    # Binary search loop
    while low <= high:
        # Calculate the middle index
        middle_index = (low + high) // 2

        # Get the SKU of the product at the middle index
        test_element = products[middle_index]['sku']

        # Print debug information
        logging.info(f"Index to search: {test_element}")

        # Check if the target SKU is equal to the SKU at the middle index
        if test_element == target_sku:
            # Return the product if found
            return products[middle_index]
        elif test_element < target_sku:
            # Adjust the search range for the right half
            low = middle_index + 1
            logging.info(f'{test_element} is less than {target_sku}. Continue searching but ignore items smaller than {test_element}')
        else:
            # Adjust the search range for the left half
            high = middle_index - 1
            logging.info(f'{test_element} is greater than {target_sku}. Continue searching but ignore items larger than {test_element}')

    # Return None if the target SKU is not found
    return None

def search_product(products, product):
    # Record start time
    start_time = time.time()
    # Call binary_search
    found_product = binary_search(products, product)
    # Record end time
    end_time = time.time()
    
    if found_product:
        print(f"\nProduct found: {found_product}")
    else:
        print("\nProduct not found.")

    # Calculate elapsed time
    elapsed_time = end_time - start_time
    logging.debug(f"Elapsed time for binary search: {elapsed_time} seconds")

def main():
    # Create inventory
    inventory_length = random.randint(10, 99)
    products = create_inventory(inventory_length)

    # # Test Case 1 - Successful Search
    # random_product = random.choice(products)

    # print('\nTest Case 1 - Successful Search\n')
    # search_product(products, random_product["sku"])

    # Test Case 2 - Unsuccessful Search
    print('\nTest Case 2 - Unsuccessful Search\n')
    search_product(products, "SKU000")

    # # Test Case 4 - Edge Cases
    # print('\nTest Case 4 - Edge Cases (Search for the product with the highest SKU value)\n')
    # search_product(products, products[0]["sku"])

    # print('\nTest Case 4 - Edge Cases (Search for the product with the lowest SKU value)\n')
    # search_product(products, products[-1]["sku"])

if __name__ == "__main__":
    main()

