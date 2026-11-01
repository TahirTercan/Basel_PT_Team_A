
##functions
#creating dictionary for module-ects + module-description + module list
def load_modules(module_file) :
    ects_by_name = {}                                   #create empty dictionary for ects
    descriptio_by_name = {}                             #create empty dictionary for description
    module_name = list()                                #create empty module name list
    skipped_line = 0                                    #counting how many lines were skipped when not the right format

    file = open(module_file)

    for line in file :
        parts = line.strip().split(";")

        if line.strip() == "" or len(parts) != 3:       #checking for empty lines and lines not in the right format
            skipped_line += 1
            continue
       
        module, ects, description = parts
        ects_by_name[module] = ects                     #add key-value pairs for module-ects in dictionary
        descriptio_by_name[module] = description        #add key-value pairs for module-description in dictionary
        module_name = list(ects_by_name.keys())         #add module name in list

    file.close()

    return ects_by_name, descriptio_by_name, module_name, skipped_line

# US-1 : showing the modules
def show_modules_info(module_file) :
    ects_by_name, description_by_name, module_name, skipped_line = load_modules(module_file)
    if skipped_line > 0 :                               
        print(f"Skipping {skipped_line} invalid lines")
    for n in range(len(module_name)) :
        print(f"{n+1}. {module_name[n]} - {ects_by_name[module_name[n]]} ECTS : {description_by_name[module_name[n]]} ")


##main file
#makes the info of the modules.txt file usable easily
load_modules("modules.txt")

# US-1 : necessary function for US-01
show_modules_info("modules.txt")
