def swap_two_variables(input):
    a = input["a"]
    b = input["b"]
    a = a^b
    b = a^b
    a = a^b
    return a,b
