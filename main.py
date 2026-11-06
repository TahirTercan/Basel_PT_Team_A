import Tahir 

MENU = (
    "1 Show module list",
    "2 Add modules",
    "3 Remove a module",
    "4 Enter class hours and experience",
    "5 View self-study hours per module and week",
    "6 Enter free hours per day",
    "7 Create study plan",
    "8 Record studied hours",
    "9 Export bar chart",
    "0 Exit the programm",
    
)

choice = ""
while choice != "0":
    print("\nMain Menu - select an option")
    for option in MENU:
        print(option)
    choice = input("Choose an option or 0 to exit: ")
    if choice == "1":
        print("US-1 in progress") #Marine.function US 1
    elif choice == "2":
        print("US-2 in progress") #Marine.function US 2
    elif choice == "3":
        Tahir.remove_module()
    elif choice == "4":
        Tahir.enter_class_hours()
    elif choice == "5":
        print("US-5 in progress") #Marcela.function US 5
    elif choice == "6":
        print("US-6 in progress") #Marcela.function US 6 
    elif choice == "7":
        print("US-7 in progress") #Marcela.function US 7
    elif choice == "8":
        print("US-8 in progress") #Marine.function US 8
    elif choice == "9":
        Tahir.export_chart()
    elif choice == "0":
        print("good bye")
    else:
        print("invalid choice")
