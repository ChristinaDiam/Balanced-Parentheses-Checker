# Balanced Parentheses #

This code is an implementation of a balanced parentheses checker using a stack data structure. 

It defines a "mystack" class with methods to initialize the stack, check if it is empty, push items onto the stack, and pop items from it. The user is prompted to input a string, which is then processed to check for balanced parentheses. 

The program uses a dictionary to match opening and closing parentheses. As it iterates through each character in the input string, it pushes opening parentheses onto the stack and checks for matching closing parentheses by popping from the stack. 
If an unmatched closing parenthesis is found or if the stack is not empty after processing the entire string, the program prints **"Unbalanced"** Otherwise, it prints **"Balanced"**.
