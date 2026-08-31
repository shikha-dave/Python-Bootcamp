def square(num):
    return num ** 2
mylist = [1, 2, 3, 4, 5]
for item in map(square, mylist):
    print(item)

print(list(map(square, mylist)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

print(list(map(splicer, ['Andy', 'Eve', 'Sally'])))



def even_check(num):
    return num % 2 == 0

print(list(filter(even_check, [1, 2, 3, 4, 5, 6])))

#lambda expression

print(list(filter(lambda num: num % 2 == 0, [1, 2, 3, 4, 5])))