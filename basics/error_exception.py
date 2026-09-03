try:
    for i in [1,2,'3']:
        print(i**2) 
except Exception as e:
    print(f"An error occurred: {e}")



try:
    x = 5
    y = 0
    z = x / y
except ZeroDivisionError as e:
    print(f"Cannot divide by zero: {e}")
finally:
    print("All done!")


while True:
    try:
        num = int(input("Enter a number: "))
        print(num ** 2)
    except:
        print("Invalid input: Please enter a valid integer.")
    else:
        print(f"Thank you! Your number squared is: {num ** 2}")
        break
    finally:
        print("Execution of the try-except block is complete.")