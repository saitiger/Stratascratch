def is_palindrome(num):
    
    return str(num) == str(num)[::-1]

def next_palindrome(n):
    n += 1
    while n <= 1_000_000:
        if is_palindrome(n):
            return n
        n += 1
    return "No palindrome found within the limit"

