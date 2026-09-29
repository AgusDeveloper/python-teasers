iterable = range(9)
iterator = iter(iterable)

while True:
    try:
        n = next(iterator)
        print(n, end = ',')
        n = 9
    except StopIteration:
        break

print()