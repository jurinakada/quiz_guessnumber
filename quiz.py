import random

print("Welcome to guessing number quiz!!")

#the fixed system (added function)
#function for difficulty. this functionn ask users to choose which defficulty they want to play.
def difficulty():
    print("Choose the game difficulty.")
    print("Easy") #the answer number is 1 to 50
    print("Normal")  #the answer number is 1 to 100
    print("Difficult")  #the answer number is 1 to 1000
    option = input("Your Dicision -> ")
    if option == "Easy":
        return 1
    elif option == "Normal":
        return 2
    elif option == "Difficult":
        return 3
    else:
        return difficulty()
#show the message to encourage users to put any number depends on user-selected difficulty.
def user_input(x,y):
    first_num = str(x)
    end_num = str(y)
    return int(input("Please enter the number from " + first_num + " to " + end_num + " -> "))

# create answer number for guessing depends on user-selected difficulty.
def create_number(user_option):
    if user_option == 1:
        x = 1
        y = 50
    elif user_option == 2:
        x = 1
        y = 100
    else: # user_option == 3
        x = 1
        y = 1000

    return random.randint(x,y),x,y

#check whether the user input number and answer is correct or not.
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
#the overview and run each movement.
def main():
    #this fuction effects create_number()
    user_option = difficulty() 
    #user_option (which refers difficulty) are assighned to create_number fuction. create_number results in deciding answer number, and scope that will be entered by user.
    answer,x,y = create_number(user_option)
    
    while(1):
        #user_input() ask users to input any number and that is assighned to input_num in this function.
        input_num = user_input(x,y)
        #answer and input_num are assighned to check_number function which results in checking whether user input number is correct or not. if it's correct, then while loop will be break.
        if check_number(answer,input_num) == 1:
            break
    #In the end, the system shows user input number and answer number just in case for checking by users.
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


