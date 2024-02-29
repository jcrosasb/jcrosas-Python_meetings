
def is_prime(integer: int):
    if integer > 1:
        for i in range(2, int(integer**0.5) + 1, 2):
             if integer % i == 0:
                 return False
        return True
    return False


def prime_factors(number: int):
    divisors = [divisor for divisor in range(2, int(number**0.5)+1) if number % divisor == 0]
    return [num for num in divisors if is_prime(integer=num)]

    # factors = [divisor for divisor in range(2, int(number**0.5)+1) if number % divisor == 0 and is_prime(integer=divisor)]
    # return factors


if __name__ == '__main__':

    num = 36
    print(prime_factors(number=num))


    print(is_prime(971))

# NOTES:
# Salvador:
#   1. naming conventions
#   2. styling (typing hints)
#   3. Use if main == name (put executable code below this)
# Ivan:
#   1. Check the step on is_prime()
#   2. 
# Dk:
#   1. Be careful about possible problems with data