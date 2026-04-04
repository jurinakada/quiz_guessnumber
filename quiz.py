import random

print("Welcome to guessing number quiz!!")

#the fixed system (added function)
def user_input():
    return int(input("Please enter the number from 1 to 100-> "))

def create_number():
    return random.randint(1,100)
    
def check_number(answer,input_num):
    if input_num == answer:
        print("You're correct!!")
        return 1
    elif input_num < answer:
        print("your imput number is smaller than answer")
        return 0
    else:
        print("your imput number is larger than answer")
        return 0

def main():

    answer = create_number()
    while(1):
        input_num = user_input()
        if check_number(answer,input_num) == 1:
            break

    print("Your input number: " + str(input_num))
    print("Correct number: " + str(answer))

    
#execute
main()
    

#the original system
# number = random.randint(1,100)
# input_number = 0
# while(1):
#     input_number = int(input("Please enter the number 1 to 100 "))

#     if (input_number > 100) | (input_number < 1):
#         print("that is out of bound")
#     else:
#         if input_number < number:
#             print("Your number is smaller than the number.")
#         elif input_number > number:
#             print("Your number is larger than the number.")
#         else:
#             print("Your number is correct!!")
#             break


