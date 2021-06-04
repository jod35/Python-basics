'''
Create a program that takes in a number of friends and then lets you enter 
their names and ages. Let the program print the information about the
friends
'''


def keep_information(number_of_friends):

    friends=[]

    for friend in range(0,number_of_friends):
        name=input("Enter a name: ")
        age=int(input("Enter an age: "))

        friend={}

        friend['name']=name
        friend['age']=age

        friends.append(friend)

    for f in friends:
        print(f"{f['name'],f['age']}")


keep_information(3)
