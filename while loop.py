
# count =0

# while count <6:
#     print(count)
#     count +=1



#guessing game
correct_number=112

guess=0

while guess != correct_number:
    guess=int(input("Enter their guess: "))

    if guess == correct_number:
        print("You win !!!!")
        break

    print("Continue")
