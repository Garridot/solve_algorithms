# Test Scenario: Auto-complete Feature

## Background:

You are tasked with implementing an auto-complete feature for a search bar in a web application. The goal is to provide suggestions as users type, utilizing the Binary Search algorithm on a sorted list of possible suggestions.

## Test Objective:

1. **Algorithm Implementation:**
   - Implement Binary Search to efficiently find and suggest auto-complete options.
   - Ensure that the list of suggestions is maintained in a sorted order.

2. **Search Efficiency:**
   - Evaluate the efficiency of your Binary Search implementation by measuring the number of comparisons during an auto-complete suggestion operation.

3. **Edge Cases Handling:**
   - Test the algorithm's performance with edge cases, such as searching for suggestions with the earliest and latest alphabetical characters.

## Test Steps:

1. **Initialization:**
   - Create a sample list of suggestions with at least 10 items, each in alphabetical order.
   - Ensure that the list of suggestions is initially sorted.

2. **Test Case 1 - Successful Auto-complete:**
   - Choose a random partial input (prefix).
   - Perform Binary Search to find and suggest auto-complete options.
   - Verify that the correct suggestions are provided.

3. **Test Case 2 - Unsuccessful Auto-complete:**
   - Choose a random non-existent partial input.
   - Perform Binary Search to find and suggest auto-complete options.
   - Verify that the algorithm correctly indicates that there are no suggestions.

4. **Test Case 3 - Efficiency Measurement:**
   - Choose a partial input and perform Binary Search for auto-complete suggestions.
   - Record the number of comparisons made.
   - Repeat the operation with different partial inputs and analyze the average number of comparisons.

5. **Test Case 4 - Edge Cases:**
   - Perform Binary Search for suggestions with the earliest alphabetical characters.
   - Perform Binary Search for suggestions with the latest alphabetical characters.
   - Ensure the algorithm handles these edge cases correctly.
