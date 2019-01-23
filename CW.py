def main():
    # prob1()
    # prob2()
    # prob3()
    # prob4()
    prob5()
# Create a function with the variable below.
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# a) Print the 3rd element of the numberList.
# b) Print the size of the array
# c) Delete the second element.
# d) Print the 3rd element.
def prob1():
    listNames = ["Kenn", "Kevin", "Erin", "Meka"]
    print(listNames)
    print(listNames[2])
    print(len(listNames))
    listNames.remove("Kevin")
    print(listNames)
    print(listNames[2])
# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
def prob2():
    userInput = ""
    while userInput != "q":
        userInput = input("Enter a string: ").lower()
# Create a function that contains a collection of information for the following.
# Jonathan/John
# Michael/Mike
# William/Bill
# Robert/Rob
# a) Print the collection
# b) Print William's nickname
def prob3():
    nicknames = {"johnathan":"john","michael":"mike","william":"bill","robert":"rob"}
    print(nicknames)
    for long, short in nicknames.items():
        print(long, short)
    print(nicknames["william"])
# Create an array of 5 numbers. Using a loop, print the elements in the array reverse order. Do not use a function
def prob4():
    listNum = [2, 4, 6, 8, 10]
    for numbers in range(len(listNum)-1, -1, -1):
        print(listNum[numbers])
# Create a function that will have a hard coded array then ask the user for a number.
# Use the userInput to state how many numbers in an array are higher, lower, or equal to it.
def prob5():
    listofnumbers = [1, 2, 3, 4, 5]
    userInput =int(input("Enter a number: "))
    lowerCounter = 0
    higherCounter = 0
    equalCounter = 0
    for numbers in listofnumbers:
        if userInput > numbers:
            lowerCounter += 1
        if userInput < numbers:
            higherCounter += 1
        if userInput == numbers:
            equalCounter += 1
    print(" lower: ", lowerCounter, "\n", "higher counter: ", higherCounter, "\n", "equal counter:", equalCounter)



if __name__ == '__main__':
    main()