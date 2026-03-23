student = {
    "name": "Shailesh",
    "age": 16,
    "marks": 85
}

# Function to display dictionary
def display_dict(d):
    print("Dictionary:", d)

# Function to add a new key-value pair
def add_item(d, key, value):
    d[key] = value
    print("Item added successfully")

# Function to search a key
def search_key(d, key):
    if key in d:
        print("Value =", d[key])
    else:
        print("Key not found")

# Calling functions
display_dict(student)

add_item(student, "grade", "A")
display_dict(student)

search_key(student, "marks")