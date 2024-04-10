#Maya Akins
#1001651922
#November 17, 2023
#Mac OS
#Python 3.11.5

f = open('input.txt', 'r')
stack = []
indent = 0
line = []

closebrace = False #closebrace flag to show 
comment = False
term = False

while 1: # loop through everyline in file
    line=f.readline()     #saving current line into expression
    if bool(line) == False:       #if end of file quit 
        break
    elif line != '\n':    #if line is not empty
        for i in range(len(line)):
            if line[i] == '{' and comment == False:    #if current char is { and comment flag is false then push to stack
                stack.append('{')
                indent += 1
            elif line[i] == '}' and comment == False:   #if current char is } and comment flag is false then pop from stack
                if stack == []: #if stack is empty then terminate flag is true and break
                    term=True
                    break
                stack.pop() 
                indent -= 1
                closebrace = True  #closebrace flag is true
            elif line[i]  == '\"':  #if current char is " then skip to next " and break
                i+=1  
                while 1:
                    if line[i] == '\"':
                        break   
                    i+=1
                break
            elif line[i] == '/':   #if current char is / then check next char
                if line[i+1] == '/':   #if next char is / then break 
                    break
                elif line[i+1] == '*': #if next char is * then comment flag is true
                    comment = True
            elif line[i] == '*' and line[i+1] == '/': #if current char is * and next char is / then comment flag is false
                    comment = False     

        if closebrace == True:  #if closebrace flag is true then set false and print current line with indent
            closebrace = False
            print(indent+1, end=' ')
            print(line, end='')
        elif term == True:  #if terminate flag is true then print error message and terminate program
            print(indent, end=' ')
            print(line)
            break
        else:   #else print empty current line with indent
            print(indent, end=' ')  
            print(line, end='')
    else:   #else print empty current line without indent
        print(line, end='')

if stack != [] or term is True: #if stack is not empty at the end or terminate flag then print error message
    print('\n\nERROR : expected ‘}’ but found EOF') 
    

    
            
            

