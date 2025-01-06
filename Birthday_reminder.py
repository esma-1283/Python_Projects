from datetime import datetime

def main():
    print("""
Welcome to birthday reminder.
With this program, you can find out whose birthday it is that day,
You can add new people and their birth dates, and find out the ages of the people you added.      

Press e to exit.

Press p to add a person.
          
Press c to see whose birthday it is today.
          
Press z to find out who is how old.       

Developed by Esma Tanşa
          
          """)
    current_date = datetime.now()
    year = current_date.year
    month = current_date.month
    day = current_date.day

    Dict = {"Esma": {"year": 2005, "month": 5, "day": 15},
            "Devrim": {"year": 2004, "month": 7, "day": 14}}

    while True:
        İnput = input("Please enter the action you want to take: ")
        if İnput.lower() == "e":
            break
        elif İnput.lower() == "p":
            inf1 = input("Please enter name: ").capitalize()

            while True:
                try:
                    inf2 = int(input("Please enter the year of birth with a number: "))
                    break
                except ValueError:
                    print("Please enter a valid number for the year.")

            while True:
                try:
                    inf3 = int(input("Please enter the month of birth with a number: "))
                    if inf3>12 or inf3<1:
                        print("Please enter a valid month (1-12).")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number for the month.")

            while True:
                try:
                    inf4 = int(input("Please enter the day of birth with a number: "))
                    if inf4<1 or inf4>30:
                        print("Please enter a valid day (1-30)")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number for the day")

            Dict.update({inf1: {"year": inf2, "month": inf3, "day": inf4}})
            print("Person added")

        elif İnput.lower() == "c":
            found = False
            for key, inner_dict in Dict.items():
                if month == inner_dict["month"] and day == inner_dict["day"]:
                    found = True
                    print(f"Today is {key}'s birthday.")
            if not found:
                print("Today is not anyone's birthday.")

        elif İnput.lower() == "z":
            who = input("Whose age are you wondering? ").capitalize()

            for i, inner in Dict.items():
                control=True
                if i == who:
                    control=False
                    birth_year = inner["year"]
                    birth_month = inner["month"]
                    birth_day = inner["day"]
                    birth_date = datetime(birth_year, birth_month, birth_day)

                    age_in_days = (current_date - birth_date).days
                    age_in_years = age_in_days / 365.25  
                    print(f"{i} is {age_in_years:.2f} years old.")

            if not control:
                print("There is no one registered with this name.")

        else:
            print("Please enter a valid input")

if __name__ == "__main__":
    main()