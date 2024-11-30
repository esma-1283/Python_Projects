import random
def main():
    print("""Welcome to Dice Roll Code\n\n\nPress "0" to roll the dice\n\n\nPress e to exit.""")
    while True:
        try:
            key_pressed=input("Please enter the transaction:")
            if key_pressed=="e" or key_pressed=="E":
                print("Exiting the program, Bye...")
                break
            elif key_pressed=="0":
                print("Your number:",random.randint(1,6))
            else:
                raise ValueError 
        except ValueError:
            print("Please enter a valid transaction.")
if __name__ == "__main__":
    main()   
