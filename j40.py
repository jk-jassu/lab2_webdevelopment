# Declare and initialize the list
Numbers = [2,4,6,12,34,52,78,54,98]

def print_list(lst):
    for num in lst:
        print(num)

def print_greater_than_12(lst):
    for num in lst:
        if num > 12:
            print(num)


print_list(Numbers)

print_greater_than_12(Numbers)