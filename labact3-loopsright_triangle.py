num = int(input("how many rows? :"))

for row in range(1,(num) +1):
# for each row in range 1-6 
    for num in range(1, row + 1):
    # for each number in range 1-6 put 1 in front of each line then add the range 1-6 but each line +1
        print(num, end=' ')
    print()


try:
    a = int(input("Enter a number: "))
    formula = ' + '.join(str(NUM) for NUM in range(1, a+1))
    print("Formula:", formula)
    result = sum(range(1, a+1))
    print("Output:", result)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

Num = int(input("how many rows? :"))

for row in range((Num), 0, -1):
    for num in range(1, row + 1):
        print(num, end=' ')
    print()