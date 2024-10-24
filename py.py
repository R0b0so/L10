string = input("put a word ")

char = input("put a letter ")
i = 0
count = 0
while(i < len(string)):
    if(string[i] == char):
        count = count + 1
    i= i + 1
print("The total number of times ", char, " has occurred = ", count)