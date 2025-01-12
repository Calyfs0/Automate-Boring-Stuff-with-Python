def collatz(number):
    if number % 2 == 0:
        output = number // 2
        print(output)
        return output
    else:
        output = 3 * number + 1
        print(output)
        return output


try:

    print("Enter a number:")
    number = int(input())

    while number != 1:
        output = collatz(number)
        number = output
except ValueError:
    print("Please enter an integer.")
