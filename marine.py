
##functions
#creating dictionary for module-ects + module-description + module list
def load_modules(module_file):
    ects_by_name={}   #create empty dictionary for ects
    description_by_name={}    #create empty dictionary for description
    module_name=list()    #create empty module name list
    skipped_line=0    #counting how many lines were skipped when not the right format

    file=open(module_file)

    for line in file:
        parts=line.strip().split(";")

        if line.strip()=="" or len(parts)!=3:   #checking for empty lines and lines not in the right format
            skipped_line+=1
            continue
       
        module,ects,description=parts
        ects_by_name[module]=ects    #add key-value pairs for module-ects in dictionary
        description_by_name[module]=description    #add key-value pairs for module-description in dictionary
        module_name = list(ects_by_name.keys())    #add module name in list

    file.close()

    return ects_by_name, description_by_name, module_name, skipped_line

#---------------------------------------------------------------------------------------------
# US-1 : showing the modules

def show_modules_info(module_file):
    ects_by_name, description_by_name, module_name, skipped_line=load_modules(module_file)
    if skipped_line>0:                               
        print(f"Skipping {skipped_line} invalid lines")    #shows the number of invalid lines in the txt file
    for n in range(len(module_name)):
        print(f"{n+1}. {module_name[n]} - {ects_by_name[module_name[n]]} ECTS : {description_by_name[module_name[n]]} ")


#---------------------------------------------------------------------------------------------
# US-2 : add module to selection and show overall hours to invest

my_modules=[]

def hours_per_modules(module_file):
    import marcela  #to have constant(hours/ECTS)
    ects_by_name, description_by_name, module_name, skipped_line=load_modules(module_file)
    for module in my_modules:
        if module in ects_by_name:
                hours=int(ects_by_name[module])*marcela.HOURS_PER_ECTS  #calculate overall hours/module depending on associated nb of ECTS
                print(f"{module} -{ects_by_name[module]} ECTS : {hours} hours.")

def select_modules(module_file):
    selection=""
    while selection!=0:
        ects_by_name, description_by_name, module_name, skipped_line=load_modules(module_file)
        print("Creating personalised module list - select an option: ")
        for n in range(len(module_name)):
            print(f"{n+1} {module_name[n]}")    #shows list of module option
        print("0 Exit selection")   #add option to exit on the displayed list
        selection=int(input("\nSelect which module you are taking this semester or 0 to exit: "))
        print()
        if selection==0:    #option to exit
            print("Exiting module selection.\n")
        elif selection < 1 or selection > len(module_name):    #option for input that is not an option in the list
            print("Invalid choice. Please select a number from the list.\n")
        elif len(my_modules)==5:   #option if all modules are already selected
            print("All possible modules are selected, your personalised module list is full.")
            print("Exiting module selection.\n")
            break      #exit module selection and comes back to main menu
        elif module_name[selection-1] in my_modules:    #option if module already in the personalised list
            print("The selected module is already in your personalised list:")
            if len(my_modules)!=0:    #showing personalised list
                print(my_modules)
            print()
        else:
            my_modules.append(module_name[selection-1])    #option to add selection to personalised list
            print("Module added. Your list is now: ")
            print(my_modules)   #showing personalised list
            print()
    print("Your personalised module selection with teh associated overall hours to be invested per module is:")
    hours_per_modules(module_file)  #shows selected modules with nb ECTS and calculated overall hours
    print("If you wish to delete a module from your selection, select option 2 in the main menu.")
    return my_modules   #to be able to reuse it in other US
    



