# Binary Search Implementation

def binary_search(suggestions, partial_input):
    # Initialize search range
    low, high = 0, len(suggestions) - 1
    
    # Initialize a list to store valid suggestions
    result = []

    # Binary search loop
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        
        # Get the current suggestion at the middle index
        current_suggestion = suggestions[mid]

        # Check if the current suggestion starts with the partial input
        if current_suggestion.startswith(partial_input):
            # If yes, add it to the result list as a valid suggestion
            result.append(current_suggestion)

        # Adjust the search range based on the comparison with partial input
        if current_suggestion >= partial_input:
            # Move to the left half
            high = mid - 1
        else:
            # Move to the right half
            low = mid + 1

    # Return the list of valid suggestions
    return result

# Test Initialization
sample_suggestions = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "orange", "peach", "pear"]
sample_suggestions.sort()

# Test Case 1 - Successful Auto-complete
partial_input_1 = "ban"
result_1 = binary_search(sample_suggestions, partial_input_1)
assert result_1 == ["banana"], f"Test Case 1 failed: Expected ['banana'], got {result_1}"

# Test Case 2 - Unsuccessful Auto-complete
partial_input_2 = "dragonfruit"
result_2 = binary_search(sample_suggestions, partial_input_2)
assert result_2 == [], f"Test Case 2 failed: Expected [], got {result_2}"

# Test Case 3 - Efficiency Measurement
partial_input_3 = "app"
comparisons_list = []

for _ in range(10):
    comparisons = binary_search(sample_suggestions, partial_input_3)
    comparisons_list.append(comparisons)

average_comparisons = sum([len(comparisons) for comparisons in comparisons_list]) / len(comparisons_list)
print(f"Average number of comparisons for Test Case 3: {average_comparisons}")


# Test Case 4 - Edge Cases
partial_input_4_1 = "a"
result_4_1 = binary_search(sample_suggestions, partial_input_4_1)
assert result_4_1 == ["apple"], f"Test Case 4.1 failed: Expected ['apple'], got {result_4_1}"

partial_input_4_2 = "z"
result_4_2 = binary_search(sample_suggestions, partial_input_4_2)
assert result_4_2 == [], f"Test Case 4.2 failed: Expected [], got {result_4_2}"

print("All test cases passed successfully!")
