
# def check_number(number):

#     if number < 0:
#         print("Number is negative")

#     elif number >0:
#         print("Number is positive")

# check_number(23)
# check_number(-11)
# check_number(100)

# def return_max(number1,number2):
#     if number1 > number2:
#         return number1
#     else:
#         return number2

# print(return_max(23,44))
# print(return_max(34,45))
# print(return_max(54,45))
# print(return_max(70,12))


def return_grading(mark):
    if (mark>90):
        grading="A"
        return grading

    elif (mark>=85) and (mark <90):
        grading="B"
        return grading

    elif (mark>=80) and (mark <85):
        grading="C"
        return grading

    else:
        grading="D"
        return grading


print(return_grading(100))
print(return_grading(80))
print(return_grading(55))
print(return_grading(75))
print(return_grading(33))
