# Function to sort words of a string in alphabeticat order

def string_alpha_sort(input_str):
    split=input_str.split(' ')
    sort=sorted(split)
    sorted_str=' '.join(sort)
    return sorted_str

input_str = input("Enter a string: ")
print(f"Original string: {input_str}")
print(f"Alphabetically sorted string: {string_alpha_sort(input_str)}")
