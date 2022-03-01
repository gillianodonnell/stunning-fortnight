
######################################################################
def encrypt(w):

    vowels = {'a':0, 'e':1, 'i':2, 'o':2, 'u':3}

    '''Step 1 reverse the input e.g. if w is 'apple', it should be 'elppa' '''
    #Your code here
    w = w[::-1] #strings can be reversed using slicing. The slice means start at string length, end at position 0, move with -1 steps, one step backward

    '''Step 2 Replace all vowels using the dictionary provided e.g. elppa becomes 1lpp0 '''
    #Your code here
    emptystring = '' #create empty string that can have elements concatenated to it, outside for loop so it elements keep getting added
    for letter in w: #for loop to iterate through the elements in string #letter is a variable that changes with each iteration
        if letter in vowels: #if is a conditional statement, if condition in true it executes the next line
            newvalue = vowels[letter] #dictionary method d[key] = value, newvalue is assigned to the value in list associated with key
            newvalue = str(newvalue) #str() casts the newvalue to a str so that it can be concatenated
            emptystring += newvalue #string concatenation = adds newvalue string to the empty string
        else: #condition is false
            emptystring += letter #adds letter that isn't in the dictionary to the empty string
    w = emptystring #w is now assigned to emptystring so we can use w in next question


    '''Step 3 Add 'a5a' to the end of w e.g. 1lpp0a5a '''
    #Your code here
    w = w + 'a5a' #string concatenation

    return w   #output should be 1lpp0a5a for an input of apple

word = input("Enter a single word: ")
encryptedWord = encrypt(word)
print (encryptedWord)

#####################################################################
def someFunction (L1):
    newList = []
    length = len(L1)
    counter = 0
    while counter < length:
        if L1[counter] > 5:
            newList.append(L1[counter])
        counter += 1
    return newList
#Your code here to rewrite with for loop - test
#For Loop
def someFunction (L1):
    newList = [] #empty list
    for number in L1: #for loop, variable = number, iterating through the list
        if number > 5: #if statement, conditional, if number is greater than 5
            newList.append(number) #if true add to newList
    return newList

#Your code here to rewrite with as list comprehension - test
#list comprehension
def someFunction(L1):
    newList = [number for number in L1 if number >5] #newlist = [expression for item in iterable(list in this case) if condition == True]
    return newList

print(someFunction([3, 4, 15, 7, 5, 6, 7]))
######################################################################
def totalEvenlyDivides (start, stop, divisor):
    #Your code here
    total = 0 #accumulator variable
    for digit in range(start,stop+divisor,divisor): #start, stop, step, I add divisor to stop incase the next variable value is too big
        if start != 0: #'!=' means 'not equal to' if start is not equal to 0
            digit = digit - 1 #let the iteration start at 0
            total += digit
        if digit % divisor != 0: #modulus, if there is a remainder left that means it does not divide evenly hence total =0
            total = 0
    #print(total)

    return total

print (totalEvenlyDivides(1, 10, 2)) 
print (totalEvenlyDivides(1, 10, 3))
print (totalEvenlyDivides(2, 6, 25)) 


######################################################################
def calculate_score (board):

    symbols = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}
    rowTotals = []
    colTotals = []

    '''Calculate the score per row and append it to the rowTotals list'''
    #Your code goes here

    for row in board: #for loop to iterate through row, innerlist is row
        scorePerRow = 0 #accumulator variable
        for symbol in row: #for element(value) in item(list which is a row)
            if symbol in symbols: #conditional #if symbol is in the dictionary, default is dictionary.keys() so i just say symbols
                score = symbols[symbol] #get dict value #d[key]=value #assign value to score
            scorePerRow += score #add the score to the accumulator variable
        rowTotals.append(scorePerRow) #append to scorePerRow to list
    

    ''''Calculate the score per column and append it to the colTotals list'''
    #Your code goes here
    for value in range(len(board[0])): #for loop using range(len()) to access each item by index, #board[0]is for the length of the row- number of columns
        scorePerCol = 0 #accumulator
        for rowNo in range(len(board)):#for loop using range(len()) to access each item by index, #board for length of board - rows
            symbolx =  board[rowNo][value] #get symbol that is in the row number and column number we want, here rowNo will change as we are adding columns
            if symbolx in symbols: #if statement #check if the symbol is in the dictionary keys
                scoreCol = symbols[symbolx] #get value #d[key]= value and assign it to the score
            scorePerCol += scoreCol #add to scorePerCol
        colTotals.append(scorePerCol)  #append scorePerCol to colTotals


    return rowTotals, colTotals

rTotals, cTotals = calculate_score([["#", "!"],["!!", "X"]])
print (rTotals, cTotals)
rTotals, cTotals = calculate_score([["!!!", "O", "!"],["X", "#", "!!!"],["!!", "X", "O"]])
print (rTotals, cTotals)
rTotals, cTotals = calculate_score([
  ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
  ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
  ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
  ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
  ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
  ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
  ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
  ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
  ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
  ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
  ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
  ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
  ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
  ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]])
print (rTotals, cTotals)

######################################################################
def read_file (input_file):
    Users = {}
    #Your code goes here
    tuplefile = open(input_file,'r') #must ‘open’ before use #Variable textfile points to a file object. Think of this like a pipe (We haven’t covered objects yet)
    lines = tuplefile.readlines() #.readlines() method of a file handle object devours entire file and return contents as list of lines(strings)
    #print(lines)

    for line in lines: #iterating through the list of strings
        line = line.strip() #default of .strip() is it strips off '\n' #gets rid of '\n'
        line = line.strip('(') #use .strip('(') to get rid of '('
        line = line.strip(')') #use .strip(')') to get rid of ')'
        line = line.replace('"','') #.strip() only strips of characters at either the end only or the start only so I used .replace(old,new) to replace '"' on bothsides of a sting at the same time
        #print(line)
        line = line.split(',') #.split() method splits the string into a list, you can specify the delimiter so I chose ','
        #print(line)
        for dictvalues in line: #variable dictvalue iterates through line
            keyvalue = int(line[0]) #assign keyvalue to the first item in the list, hardcoding line[0] to key value and casting it to an interger as the question asked for an integer
            Users[keyvalue] = list(line[1:]) #assigning the keyvalue to the dictionary Users as a key and letting that equal to the 2nd and 3rd items in list format
            #d[key] = value, #list is an inbuilt function- takes sequence types and converts them to a list, I used stringslicing here.
            #string slicing - you can return a range of characters by using the slice syntax
            #In line 183 line[1:] says that the 2nd string in the list to the last string in the list 
            
        #print(Users.keys())
        #print(Users.values())
    tuplefile.close() #must ‘close’ when done
    return Users
    

print(read_file ("details.txt"))


    
 


