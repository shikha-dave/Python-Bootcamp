def checkListPattern():
    orderList = []

    user_input = input("Enter a list of numbers separated by commas: ")
    #user_list = [int(num) for num in user_input.split(',')]
    user_list = list(map(int, user_input.split(',')))
    
    for value in user_list:
        orderListLen = len(orderList)
        print(value)
        if (orderListLen == 0 or orderListLen == 1 )and value == 0:
            orderList.append(value)
        elif orderListLen == 2 and value == 7:
            orderList.append(value)
            print("Pattern found!") 
            print("The pattern is: " + str(orderList) + " and the length is: " + str(len(orderList)))
            break

    if len(orderList) < 3:
        print("Pattern not found.")
        print("The pattern is: " + str(orderList)+ " and the length is: " + str(len(orderList)))


# function to check if pattern 007 is found in a list of numbers
def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)

        if len(code) == 1:
            print("pattern found!")

    return False

        


checkListPattern()

spy_game([1, 0, 2, 4, 0, 5, 3])