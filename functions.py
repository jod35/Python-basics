# they name pieces of code
# they take arguments

# def print_name():
#     print("Jonathan")


# print_name()


# def print_firstname(firstname):
#     print(firstname)

# print_firstname("Jonathan")


# def total(n1,n2,n3):
#     print(n1+n2+n3)

# total(2,3,4)

# def total(*args):
#     print(sum(args))


# total(12,34,25)



# def give_info(name,age):
#     print(f"Your name {name}")
#     print(f"Your age is {age}")


# give_info("Jonathan",22)


# def area(side):
#     print(f"Area of square with a side of {side} units is {side * side}")

# area(2)
# area(4)
# area(6)

def total(*args):
    return sum(args)


print(f"The sum of many args is {total(45,45,345,45)}")
