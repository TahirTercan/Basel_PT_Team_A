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
        if not answer.isdigit():
            print("This module is not in your selection.")
        elif int(answer) < 1 or int(answer) > count_selection:
            print("This module is not in your selection.")
        else:
            position_to_delete = int(answer) - 1
            name_of_selection = selected_modules[position_to_delete]
            del selected_modules[position_to_delete]
            print(f"Removed: {name_of_selection}")
    print("No modules selected")



#US 4

def enter_class_hours():
    print("US-4 in progress")


#US 9
def export_chart():
    print("US-9 in progress")