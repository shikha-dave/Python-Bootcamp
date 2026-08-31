print('print only the words that start with s in this sentence')
# Print only the words that start with s in this sentence
string = 'Print only the words that start with s in this sentence'
for word in string.split():
    if word[0] == 's':
        print(word) 

print('\n use range() to print all the even numbers from 0 to 10.')
# Use range() to print all the even numbers from 0 to 10.
for num in range(0, 11, 2):
    print(num)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print("\nList of all numbers between 1 and 50 that are divisible by 3:") 
divisible_by_3 = [num for num in range(1,51) if num % 3 == 0]
print(divisible_by_3)

# Print every word in this sentence that has an even number of letters
string = '\n Print every word in this sentence that has an even number of letters'
for word in string.split():
    if len(word) % 2 == 0:
        print('"' + word + '" has an even length!')

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

print("\nFizzBuzz from 1 to 100:")
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#Create a list of the first letters of every word in this string    
string = "\n Create a list of the first letters of every word in this string"
first_letters = [word[0] for word in string.split()]
print(first_letters)