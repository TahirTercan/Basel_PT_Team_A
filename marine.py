
##functions
#creating dictionary for module-ects + module-description + module list
def load_modules(module_file):
     ects_by_name={}
     description_by_name={}
     skipped_line=0
     try :
         with open(module_file, "r", encoding="utf-8") as infile :
             infile.readline()
             for line in infile:
                 parts=line.strip().split(";")

                 if line.strip()=="" or len(parts)!=3:   #checking for empty lines and lines not in the right format
                    skipped_line+=1
                    continue
        
                 module,ects,description=parts
                 ects_by_name[module]=int(ects)    
                 description_by_name[module]=description
                 module_name=list(ects_by_name.keys())   
             return ects_by_name, description_by_name, module_name, skipped_line
     except(FileNotFoundError):
         print("The file does not exist.")

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

my_modules=[]   #personalised module list
hours_by_module={}  #overall hours/module dictionary 

#calculates overall hours/module from personalised module list
def hours_per_modules(module_file):   
    import marcela  #to have constant(hours/ECTS)
    ects_by_name, description_by_name, module_name, skipped_line=load_modules(module_file)
    for module in my_modules:
        if module in ects_by_name:
            hours_by_module[module]=ects_by_name[module]*marcela.HOURS_PER_ECTS  
    return hours_by_module

#displays selected modules with nb ECTS and calculated overall hours
def show_overall_hours(module_file):    
    ects_by_name, description_by_name, module_name, skipped_line=load_modules(module_file)
    for module in hours_by_module:
        print(f"{module} - {ects_by_name[module]} ECTS : {hours_by_module[module]} hours.")   

#making personalised module selection
def select_modules(module_file):
    selection=""
    ects_by_name, description_by_name, module_name, skipped_line=load_modules(module_file)
    if my_modules!=[]:  #showing the personalised list if smth is already in it
                print("Your current personalised module list is:", my_modules)
                print()
    while selection!=0:
        print("Creating personalised module list - select an option: ")
        for n in range(len(module_name)):
            print(f"{n+1} {module_name[n]}")    
        print("0 Exit selection")   #add option to exit on the displayed list
        selection=input("\nSelect which module you are taking this semester or 0 to exit: ")
        print()
        if not selection.isdigit():
            print("Invalid choice. Please select a number from the list.\n")
        else :
            selection=int(selection)
            if selection==0:    
                print("Exiting module selection.\n")
            elif selection < 1 or selection > len(module_name):    
                print("Invalid choice. Please select a number from the list.\n")
            elif len(my_modules)==5:  
                print("All possible modules are selected, your personalised module list is full.")
                print("Exiting module selection.\n")
                selection=0   
            elif module_name[selection-1] in my_modules:    
                print("The selected module is already in your personalised list:")
                if len(my_modules)!=0:    
                    print(my_modules)
                print()
            else:
                my_modules.append(module_name[selection-1])    
                print("Module added. Your list is now: ")
                print(my_modules)   
                print()
    print("Your personalised module selection with the associated overall hours to be invested per module is:")
    hours_per_modules(module_file)    #calculates overall hours/module in personalised list
    show_overall_hours(module_file)  #shows selected modules with nb ECTS and calculated overall hours
    print("\nIf you wish to delete a module from your selection, select option 3 in the main menu.")
    return my_modules   


#---------------------------------------------------------------------------------------------
# US-8 : Record weekly self study hours and save output file




