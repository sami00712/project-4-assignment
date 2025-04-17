# def in_range(n, low, high):

#     if n >= low and n <= high:
#         return True
    
#     return False

def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    return False

# Test cases
print(in_range(5, 1, 10))   # True (5 is between 1 and 10)
print(in_range(11, 1, 10))  # False (11 is greater than 10)
print(in_range(1, 1, 10))   # True (1 is the lower bound)
print(in_range(10, 1, 10))  # True (10 is the upper bound)
print(in_range(-3, -5, 0))  # True (-3 is between -5 and 0)
