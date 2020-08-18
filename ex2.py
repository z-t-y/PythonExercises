for i in range(0, 101):
    if not i:
        print(f"{i}, ", end='')
        continue
    if i == 100:
        print("Buzz")
        break
    if (i % 3 != 0 and i % 5 != 0):
        print(i, end='')
    if i % 3 == 0:
        print("Fizz", end='')
    if i % 5 == 0:
        print("Buzz", end='')
    print(", ", end='')
