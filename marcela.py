#constants (for all User stories)
HOURS_PER_ECTS = 30
WEEKS_FOR_SELF_STUDY = 14
WEEKS_FOR_LECTURES = 13
REDUCTION_BY_LEVEL = {1: 0.0, 2: 0.30, 3: 0.60}
EXPERIENCE_NAMES = {1: "No previous experience", 2: "Intermediate experience", 3: "High experience"}
DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#--------------------------------------------------------------------------------------------------------------------------------

##functions US-5
#rounding to 2 decimals, 0.005 always goes up.
def round_half_up(value):
    return round(value + 0.000001, 2)

#self-study hours of one module for the whole semester
def self_study_per_semester(module, module_file, class_hours_semester, experience_level):
    ects_by_name, description_by_name, module_name, skipped_line = load_modules(module_file)  #function from Marine's file
    ects = float(ects_by_name[module])
    subject_workload = HOURS_PER_ECTS * ects
    reduction = REDUCTION_BY_LEVEL[experience_level]
    return (subject_workload - class_hours_semester) * (1 - reduction)

#self-study hours of one module for one week
def self_study_per_week(hours_semester):
    return hours_semester / WEEKS_FOR_SELF_STUDY

#--------------------------------------------------------------------------------------------------------------------------------

#US-5: View Self-Study Hours per Module and Week
def view_self_study(selected_modules, module_file, class_hours_by_name, experience_by_name):
    if len(selected_modules) == 0:
        print ("No modules selected. Please add modules with option 2.")
        return 0, 0                        #return back to main menu

    total_semester = 0
    total_week = 0
    counted_modules = 0                     #how many modules have complete data

    for module in selected_modules:
        if module not in class_hours_by_name or module not in experience_by_name:
            print (f"{module}: data missing. Please complete it with option 4.")
            continue

        class_hours = class_hours_by_name[module]
        level = experience_by_name[module]

        hours_semester = self_study_per_semester(module, module_file, class_hours, level)
        hours_week = self_study_per_week(hours_semester)

        total_semester += hours_semester
        total_week += hours_week
        counted_modules += 1

        print(f"{module}: {class_hours:.2f} hours class, {EXPERIENCE_NAMES[level]}, "
              f"{round_half_up(hours_semester):.2f} hours per semester, {round_half_up(hours_week):.2f} hours per week")

    if counted_modules > 0 :
        print(f"Total: {round_half_up(total_semester):.2f} hours per semester, {round_half_up(total_week):.2f} hours per week")
    else :
        print("No module has complete data yet.")

    return total_semester, total_week

#--------------------------------------------------------------------------------------------------------------------------------

##function US-6
#ask student the free hours of one day, asking again until the value is valid
def ask_free_hours(day):
    hours = -1              #start value that is not valid
    while hours < 0:
        answer = input(f"Free hours on {day}: ")
        if not answer.replace(".", "", 1).isdigit():    #only digits and one point are allowed, so letters, or negative values are not valid
            print("Invalid number.")
        else:
            value = float(answer)
            if value > 24 or value % 0.5 != 0:
                print("Free hours must be between 0 and 24, in steps of 0.5.") #only hours between 0 and 24, and only 0.5 decimals is accepted. eg: 2.5, or 4.5. (7.8 is not accepted).
            else:
                hours = value
    return hours


#--------------------------------------------------------------------------------------------------------------------------------
#US-6: Enter Weekly availability to assess self-study time

def enter_free_hours(total_self_study_week):
    free_hour_by_day = {}            #empty dictionary for the free hours/day
    total_free = 0

    for day in DAYS_OF_WEEK:
        hours = ask_free_hours(day)
        free_hour_by_day[day] = hours
        total_free += hours

    print("Free hours per day:")
    for day in DAYS_OF_WEEK:
        print(f"{day}: {round_half_up(free_hour_by_day[day]):.2f} hours")
    print(f"Total free time: {round_half_up(total_free):.2f} hours per week")

    if total_self_study_week == 0:
        print("No self-study total available. Please complete the module data first with option 4.")
    else:
        difference = total_free - total_self_study_week
        if difference >= 0:
            print(f"The free time is enough, {round_half_up(difference):.2f} hours left over.")
        else:
            missing = - difference
            print(f"The free time is not enough, {round_half_up(missing):.2f} hours missing.")
    return free_hour_by_day


#--------------------------------------------------------------------------------------------------------------------------------
##function US-7