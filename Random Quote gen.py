#A small python project using random functions which generates quotes for the user 
import random

#Defining the main function as the game itself
def main():

# Welcome statement
    print("Hi, your today's quote is:")

#List of all the quotes
    quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
        "The way to get started is to quit talking and begin doing. -Walt Disney",
        "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
        "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron",
        "The only thing we have to fear is fear itself. -Franklin D. Roosevelt"]

#Choosing a random quote from the "Quotes" list and printing it out
    quote = random.choice(quotes)
    print(quote)

#Creating a loop using while function to provide option to the user whether they would like to leave or get another quote simultaneously
    while True:

#Taking input from the user 
        option = input("You can exit, get another quote or add your own\nExit/Another/Add:\n")

#Using if statements for filtering "Exit", "Another" and "Add" output
        if option == "Exit":
            print("You have a great day!")
            break #Breaking through the loop when input is "Exit"
        elif option == "Another":
            quote = random.choice(quotes) #Choosing a random quote
            print(quote)
        elif option == "Add": # Adding a custom quote
            def take_input():
                print("Input your Quote:")
                take_input = str(input(""))
                quotes.append(take_input)
                print("Operation completed successfully.")
                print(quotes)
            take_input()
        else:

#If the input is anything else than "Done" or "Another", this handles errors
            print("Invalid option, please enter 'Exit', 'Another' or 'Add'")
            continue #Using continue to keep the user in the loop unless a valid input is provided

if __name__ == "__main__":
    main()
