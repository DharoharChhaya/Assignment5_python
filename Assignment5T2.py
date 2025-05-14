def demonstrate_list_slicing():
    # Step 1: Create a list of numbers from 1 to 10
    original_list = list(range(1, 11))
    print(f"Original list: {original_list}")
    
    # Step 2: Extract the first five elements from the list
    extracted_elements = original_list[:5]
    print(f"Extracted first five elements: {extracted_elements}")
    
    # Step 3: Reverse the extracted elements
    reversed_extracted = extracted_elements[::-1]
    print(f"Reversed extracted elements: {reversed_extracted}")

# Run the function
demonstrate_list_slicing()
