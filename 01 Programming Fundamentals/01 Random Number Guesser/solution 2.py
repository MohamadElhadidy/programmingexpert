import random

attempts = 0
guess = None
suffix = ''

start = input("Enter the start of the range: ")  
while not start.isdigit():
    print("Please enter a valid number.")
    start = input("Enter the start of the range: ")  
    

end = input("Enter the end of the range: ")    
while not end.isdigit() or int(end) < int(start):
    print("Please enter a valid number.")
    end = input("Enter the end of the range: ")  
    

num = random.randint(int(start),int(end))


while  guess != num :
    guess_num = input("Guess a number: ")  
    if not guess_num.isdigit():
        print("Please enter a valid number.")
        continue 
    attempts +=1
    guess = int(guess_num)


if attempts > 1:
    suffix = 's'

print(f"You guessed the number in {attempts} attempt{suffix}")




