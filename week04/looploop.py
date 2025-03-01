# Lab 4.1 - Topic 04-Flow control if elif and else
# Author Linda Nikolajeva
# Hpow to use a while loop to modify 1 so that it keeps prompting the user for a number 
# until the user enters -1 

while True: # The while True: creates an infinite loop
    number = int(input("Enter a number (-1 to stop): "))
    if number == -1:
        print("Exiting...")
        
        break  # Exit the loop when -1 is entered

# source https://chatgpt.com/c/67c35d51-4e1c-8005-9040-c74f3363fb29