import random

number = random.randint(1,100)
input_number = 0

print("Welcome to guessing number quiz!!")

while(1):
    input_number = int(input("Please enter the number 1 to 100 "))

    if (input_number > 100) | (input_number < 1):
        print("that is out of bound")
    else:
        if input_number < number:
            print("Your number is smaller than the number.")
        elif input_number > number:
            print("Your number is larger than the number.")
        else:
            print("Your number is correct!!")
            break


print("Your input number: " + str(input_number))
print("Correct number: " + str(number))


