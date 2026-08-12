hungry = "no"
if hungry == "hungry":
    print("I am hungry.")
elif hungry == "no":
    print("I donot know.")
else:
    print("I am not hungry.")    

# for loop
myList = [1, 2, 3, 4, 5]
for item in myList:
    print(item) 
# while loop
count = 0
while count < 5:
    print(f"while loop value: {count}")
    count += 1