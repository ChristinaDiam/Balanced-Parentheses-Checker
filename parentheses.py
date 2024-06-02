

#	AM: 1115201800046
#   NAME: ΧΡΙΣΤΙΝΑ ΔΙΑΜΑΝΤΗ


class mystack:
    
    def __init__(self):

        #makes an empty list
        self.__index= []

    
    def __len__(self):

        #returns the number of items in our list
        return len(self.__index)


    #checks if stack is empty
    def empty(self):

        #if the length of list is 0, the stack is empty
        if len(self)== 0:
            print("Empty stack")

            return True
        
        #if the stack in NOT empty return False
        return False


    def push(self,item):

        #inserts a new item to list
        self.__index.append(item)


    def pop(self):

        #checks if stack is empty
        if mystack.empty(self)== True:
            print("Nothing to pop.")
            return

        #if stack is not empty, removes an item
        print('Item removed.')
        return self.__index.pop()



#asks user to enter a string and prints it
#user can type anything, but program keeps only parenthesis
str = input("Enter a string:\n")
print(f'You entered: {str}')

#creates an object
s= mystack()


i=0
flag=False

#search for parenthesis in string
for i in str:

    #if character is opening parenthesis push item to stack
    if i=='(' or i=='[' or i=='{':
        s.push(i)
    
    #else character must be closing parenthesis
    elif i==')' or i==']' or i=='}':

        #if character is closing parenthesis,stack cannot be empty
        #if stack is empty, then string of parenthesis is unbalanced
        if s.empty()== True:
            flag=False
            break


        #use pop to keep the last opening parenthesis   
        last_opening= s.pop()
        
        #checking if closing parenthesis is the pair of the last opening parenthesis
        #if there is a pair, then flag turns True (balanced)
        if (last_opening=='(' and i==')') or (last_opening=='[' and i==']') or (last_opening=='{' and i=='}'):
 
            flag=True

        else:
        #else string is unbalanced, flag turns False
            flag=False
            break


#if stack is empty and flag is True, then string is balanced
if s.empty()==True and flag==True:
    print('Balanced.')

else:
    print('Unbalanced.')
