my_tuple = (5, 10, 15, 20, 25)

# Function to find sum of elements
def tuple_sum(t):
    return sum(t)

# Function to find minimum element
def tuple_min(t):
    return min(t)

# Function to search an element
def search_element(t, key):
    if key in t:
        return "Element found"
    else:
        return "Element not found"

# Calling functions
print("Tuple:", my_tuple)
print("Sum of tuple:", tuple_sum(my_tuple))
print("Minimum value:", tuple_min(my_tuple))
print(search_element(my_tuple, 15))