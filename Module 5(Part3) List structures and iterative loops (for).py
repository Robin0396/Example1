def is_prime(number):
    if number <=1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range( 3, int(number ** 0.5) +1, 2):
        if number % i == 0:
            return False
    return True
user_input = int(input('Enter a integer: '))
if is_prime(user_input):
    print(f'{user_input} is a prime number.')
else:
    print(f'{user_input} is not a prime number.')