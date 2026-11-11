import Tahir 
import Marine
import Marcela

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
    "0 Exit the program",
)

choice = ""
while choice != "0":
    print("\nMain Menu - select an option")
    for option in MENU:
        print(option)
    choice = input("\nChoose an option or 0 to exit: ")
    if choice == "1":
        Marine.show_modules_info("modules.txt")
    elif choice == "2":
        Marine.select_modules("modules.txt")
        print("US-2 in progress") #Marine.function US 2
    elif choice == "3":
        Tahir.remove_module(Marine.my_modules)
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
        print("Good bye")
    else:
        print("Invalid choice.")
