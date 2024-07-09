def reverse_string(string):
    # return string[::-1] # Pythonic Code
    reversed_str = ""
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str
