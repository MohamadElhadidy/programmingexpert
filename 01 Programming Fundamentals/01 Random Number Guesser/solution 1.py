import random

i = 0
while True:
    start = input("Enter the start of the range: ")
    if start.isdigit():
        start = int(start)
        break
    print("Please enter a valid number.")


while True:
    end = input("Enter the end of the range: ")    
    if end.isdigit():
        end = int(end)
    if start < end:
        break
    print("Please enter a valid number.")
    
num = random.randint(start,end)


while True:
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
        i += 1
        if guess == num:
            break
    else:
        print("Please enter a valid number.")
    

if  i == 1:
    print(f"You guessed the number in {i} attempt")
else:
    print(f"You guessed the number in {i} attempts")




