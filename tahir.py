#US 3
def remove_module(selected_modules):
    if len(selected_modules) == 0:
        print("No modules selected. Please add modules with option 2.")
        return # return back to main menu
    while len(selected_modules) > 0:
        for i in range(len(selected_modules)):
            print(f"{i+1}. {selected_modules[i]}")
        answer = input("Number of the module to remove (or done): ")
        if answer == "done":
            return # return back to main menu
        count_selection = len(selected_modules)
        highest = str(count_selection)
        if len(answer) != 1:
            print("This module is not in your selection.")
        elif answer < "1" or answer > highest:
            print("This module is not in your selection.")
        else:
            position_to_delete = int(answer) - 1
            name_of_selection = selected_modules[position_to_delete]
            del selected_modules[position_to_delete]
            print(f"Removed: {name_of_selection}")
    print("No modules selected.")



#------------US 4-------------

class_hours_by_name = {}
experience_by_name = {}

def enter_class_hours(selected_modules, ects_by_name):
    if len(selected_modules) == 0:
        print("No modules selected. Please add modules with option 2.")
        return # return back to main menu
    for module in selected_modules:
        workload_semester = int(ects_by_name[module]) * 30
        hours_per_week = float(input(f"{module} - class hours per week: "))
        while hours_per_week < 0 or hours_per_week * 13 >= workload_semester: #solange die Std negativ sind oder mehr als workload
            if hours_per_week < 0:
                print("Invalid number.")
            else: 
                print(f"Class hours must be less than the workload of {workload_semester} h.")
            hours_per_week = float(input(f"{module} - class hours per week: ")) #in while, not in if else condition, asking after condition again
        experience = int(input(f"{module} - experience (1 = no previous experience, 2 = intermediate, 3 = high): "))
        while experience < 1 or experience > 3:
            print("Invalid choice.")
            experience = int(input(f"{module} - experience (1 = no previous experience, 2 = intermediate, 3 = high): "))
        if experience == 1:
            experience_name = "no previous experience"
        elif experience == 2:
            experience_name = "intermediate"
        elif experience == 3:
            experience_name = "high"
        hours_per_semester = 13 * hours_per_week
        print(f"{module}: {hours_per_week:.2f} h per week, {hours_per_semester:.2f} h per semester, experience: {experience_name}")
        #writing in dict for -> us 5
        class_hours_by_name[module] = hours_per_week 
        experience_by_name[module] = experience
        print()
    
     


#US 9
def export_chart():
    print("US-9 in progress")

#Test
enter_class_hours(["Mathematics_1", "Statistics_1"], {"Mathematics_1": 3, "Statistics_1": 3})

print(class_hours_by_name)
print(experience_by_name)