#constants (for all User stories)
HOURS_PER_ECTS = 30
WEEKS_FOR_SELF_STUDY = 14
WEEKS_FOR_LECTURES = 13
REDUCTION_BY_LEVEL = {1: 0.0, 2: 0.30, 3: 0.60}
EXPERIENCE_NAMES = {1: "No previous experience", 2: "Intermediate experience", 3: "High experience"}
DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#--------------------------------------------------------------------------------------------------------------------------------

##functions
#rounding to 2 decimals, 0.005 always goes up.
def round_half_up(value):
    return round(value + 0.000001, 2)

#self-study hours of one module for the whole semester
def self_study_per_semester(ects, class_hours_semester, experience_level):
    subject_workload = HOURS_PER_ECTS * ects
    reduction = REDUCTION_BY_LEVEL[experience_level]
    return (subject_workload - class_hours_semester) * (1 - reduction)

#self-study hours of one module for one week
def self_study_per_week(hours_semester):
    return hours_semester / WEEKS_FOR_SELF_STUDY

#--------------------------------------------------------------------------------------------------------------------------------

#US-5: View Self-Study Hours per Module and Week
def view_self_study(selected_modules, ects_by_name, class_hours_by_name, experience_by_name):
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

        ects = float(ects_by_name[module])
        class_hours = class_hours_by_name[module]
        level = experience_by_name[module]

        hours_semester = self_study_per_semester(ects, class_hours, level)
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

##functions
#checking if the text typed by the student is a valid number of free hours


#US-6: Enter Weekly availability to assess self-study time