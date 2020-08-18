#anyNum = int(input("Please enter an integer "))

# tripleUp = anyNum
# quarterValue = anyNum

# anyNum -= 5
# print(anyNum)

# print('\n')

# tripleUp *= 3
# print(tripleUp)

# print('\n')

# quarterValue /= 4
# print(quarterValue)

# sum = 0

# for i in range (3):
#     num = int(input("Please enter an integer "))
#     sum += num
    
# print(sum)

# print("The square of {} is {}".format(anyNum, anyNum ** 2))

# print("{} modulo 3 is {}".format(anyNum, anyNum % 3))

# if (anyNum % 2) == 0:
#     print("{} is divisible by 2".format(anyNum))
    
    
# celestialObjects = [['Mercury', 'Venus', 'Earth', 'Mars'], ['Polaris', 'Arcturus', 'Spika', 'Alkaid'], ['Milky Way', 'Andromeda'], ['Opportunity', 'Curiosity', 'Perseverance']]

# print(celestialObjects[0])
# print(celestialObjects[1])
# print(celestialObjects[2])
# print(celestialObjects[3])

# print(celestialObjects[1][2])

# print(celestialObjects[3][::-1])


randomObjects = []

numOfStrings = int(input("How many strings would like to enter? "))

for i in range(numOfStrings):
    userInput = input("Please enter a string: ")
    randomObjects.append(userInput)
    
print(randomObjects)

letter = input("Which letter would you like to count? ")
letterCounter = 0

for i in range(numOfStrings):
    letterCounter += randomObjects[i].count(letter)
    
print("The number of occurrences of the letter '{}' is {}".format(letter, letterCounter))