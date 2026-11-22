import tahir 
import marine
import marcela

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

ects_by_name, descriptions, names, skipped = (marine.load_modules("modules.txt"))
free_hours_by_day = {} #filled with US6 and used later for US7
choice = ""
while choice != "0":
    print("\nMain Menu - select an option")
    for option in MENU:
        print(option)
    choice = input("\nChoose an option or 0 to exit: ")
    print()
    if choice == "1":   #US-1(Marine)
        marine.show_modules_info("modules.txt")
    elif choice == "2":    #US-2(Marine)
        marine.select_modules("modules.txt")
    elif choice == "3":
        tahir.remove_module(marine.my_modules)
    elif choice == "4":
        tahir.enter_class_hours(marine.my_modules, ects_by_name)
    elif choice == "5":
        marcela.view_self_study(marine.my_modules, "modules.txt", tahir.class_hours_by_name, tahir.experience_by_name)
    elif choice == "6":
        total_week = marcela.total_self_study_per_week(marine.my_modules, "modules.txt", tahir.class_hours_by_name, tahir.experience_by_name)
        free_hours_by_day = marcela.enter_free_hours(total_week)
    elif choice == "7":
        marcela.create_study_plan(marine.my_modules, "modules.txt", tahir.class_hours_by_name, tahir.experience_by_name, free_hours_by_day)
    elif choice == "8":
        print("US-8 in progress") #Marine.function US 8
    elif choice == "9":
        tahir.export_chart()
    elif choice == "0":
        print("Good bye")
    else:
        print("Invalid choice.")
