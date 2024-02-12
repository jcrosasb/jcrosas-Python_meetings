import random

# Generated random number
lower_bound = 0
upper_bound = 1_000_000
random_number = random.randint(lower_bound, upper_bound)
print(random_number)

# Initialize guess to None to start loop
guess = None

# Loop to find the random number. These are the rules:
#   * If the distance between the guess and the random number is < 1/4 of the whole range, 
#     then you are very hot
#   * If the distance between the guess and the random number is between 1/4 and 1/2 of the whole range, 
#     then you are hot
#   * If the distance between the guess and the random number is between 1/2 and 3/4 of the whole range, 
#     then you are cold
#   * If the distance between the guess and the random number is > 3/4 of the whole range, 
#     then you are very cold
while guess != random_number:

    # Input initial guess
    guess = int(input("Enter a number (integer between 1 and 100): "))

    # distance between the guess and the selected random number
    distance = abs(random_number - guess)

    if guess < lower_bound or guess > upper_bound:
        print('outer space')
    else:
        if lower_bound <= distance <= upper_bound//4:
            print('very hot')
        elif upper_bound//4 < distance <= upper_bound//2:
            print('hot')
        elif upper_bound//2 < distance <= 3*upper_bound//4:
            print('cold')
        else:
            print('very cold')

print(f'The number is {random_number}. You won')