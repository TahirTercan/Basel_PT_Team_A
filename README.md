# Study Planner (Console)

## 📝 Analysis

**Problem**
Part-time students (who) experiences difficulty planning how many hours of self study their 
modules require per week (what), when they plan their week alongside their job and FH 
lectures (where) resulting in too little time for self-study and fall behind (why).​


**Scenario**

Study Planner solves the part of the problem where the weekly self-study hours are worked out and distributed: a student selects the modules of the semester, enters the class hours and the experience level and the free hours of the week, and gets the self-study hours per module and a study plan for the week. Every week, the student records the hours actually studied and can export a chart that compares the planned and the actual hours from the beginning of the semester until a chosen week.

### 👤 User Roles

| Role | Description |
|------|-------------|
| **Student** | A part-time BSc BIT student who works alongside the degree programme and plans the weekly self-study for the modules of the current semester. |


### 📖 User Stories

---
#### US-1 : List of the assesment modules
**As a** student, **I want** to see a numbered list of the five assesment modules of my programm with their ECTS and a short description of each of them, **so that** I can have an overview of the modules of the first semester without looking them up somewhere else. 

**Acceptance criteria**
- The assesment modules list, their ECTS and descritpion are diplayed when option 1 in the main menu.
- Each module is shown on its own line in the format "Name of the module - number of ECTS : description".
- The displayed list starts at 1. and follows the order in modules.txt
- **Given** modules.txt contains the five assesment modules, **when** the list is diplayed, **then** five line are shown.
- **However, given** a line in modules.txt does not have the format "Name; ECTS; description", **then** this line is skipped with the message "Skipping invalid line: ...” and the other modules are still displayed.

---
#### US-2: Select modules to calculate overall hours for each 
**As a** student, **I want** to add modules from the list to my selection, **so that** I can calculate the total semester workload for the modules I am taking.

**Acceptance criteria**
- The list of modules with their associated number is displayed to allow the student to know which number should be selected depending on which class is taken, in the format "Number Name of the module", when selecting option 2 in the main menu.
- The programm will ask which module should be added to the personalised selection.
- If the selection is done, the calculation of the overall hours of the selected modules will be displayed. Each line will display one module and its associated overall hours in the format "Number Name of the module - Number of ECTS : Overall hours for the semester".
- **Given** the module 1 Mathematics_1 which represents 3 ECTS,**when** selected, **then** the overall hours for this module will be displayed, i.e. 90 hours.
- **However, given** a number is not an option in the list,  **then** the message "Error : select a number for the list." will be displayed and the selecting question will be asked again.
- **However, given** a number is already selected, **then** the message "Error : the module is already selected." will be displayed and the selecting question will be asked again.

---
#### US-3: Remove a module 
**As a** student, **I want** to remove a selected module, **so that** I can correct a wrong entry without re-entering everything again. 

**Acceptance criteria**
- When option 3 is selected in the main menu, the selected modules are displayed as a numbered list in the format "Number. Name of the module", followed by the question "Number of the module to remove (or done):".
- A valid input is a number from this list. After removing, the message "Removed: Name of the module" and the remaining selection are displayed, and the question is asked again. Entering "done" returns to the main menu.
- The class hours and the experience of a removed module are removed as well, so US-5 no longer counts it.
- **Given** the selection is 1. Mathematics_1 and 2. Statistics_1, **when** the student enters 2, **then** the message "Removed: Statistics_1" and the remaining selection "1. Mathematics_1" are displayed, and the question is asked again.
- **However, given** the student enters a number that is not in the list for example 3 or 0, text instead of a number, or nothing, **then** the message "This module is not in your selection." is displayed and the question "Number of the module to remove (or done):" is asked again.
- **However, given** the student removes the last module of the selection, **then** the messages "Removed: Name of the module" and "No modules selected." are displayed and the program displays the main menu.
- **However, given** no modules were selected previously, **then** the message “No modules selected. Please add modules with option 2.” is displayed and the main menu is shown again.


---
#### US-4: Enter class hours and personal experience
**As a** student, **I want** to enter my class hours per week and my personal experience for each selected module, between no previous experience, intermediate or high, **so that** my self-study hours reflect my personal starting point.

**Acceptance criteria**
- When option 4 is selected in the main menu, the program asks two questions for each selected module: "Name of the module - class hours per week:" and "Name of the module - experience (1 = no previous experience, 2 = intermediate, 3 = high):".
- Class hours are a number of 0 or more. The class hours per semester are the class hours per week times 13 class weeks. The class hours per semester must be smaller than the total workload of the module (ECTS x 30 hours). Otherwise no time would be left for self-study.
- The experience is entered as the number 1, 2 or 3. It reduces the self-study hours calculated in US-5:
	- For no previous experience = 0%
	- For intermediate experience = 30%
	- For high experience = 60%
Self study hours for Math module (3ECTS) = ((30hrs * 3 ECTS) - class hours per semester) * (1 - experience %)
- After both inputs, the line "Name of the module: class hours per week, class hours per semester, experience" is displayed, hours with two decimal places. New inputs replace the old values.
- **Given** Mathematics_1 (3 ECTS) is selected, **when** the student enters 1.5 and 2, **then** the program shows "Mathematics_1: 1.50 h per week, 19.50 h per semester, experience: intermediate".
- **Given** Mathematics_1 with 19.5 class hours per semester, **when** the student chooses level 2, **then** the self-study is 49.35 hours (shown in US-5).
- **However, given** the student enters 7 class hours for a 3 ECTS module (7 x 13 = 91 h, more than 90 h), **then** the program shows "Class hours must be less than the workload of 90 h." and asks again.
- **However, given** the student enters -1, "1,5", letters or nothing as class hours, **then** the program shows "Invalid number." and asks again.
- **However, given** the student enters 0, 4, 1.5 or letters as level, **then** the program shows "Invalid choice." and asks again.
- **However, given** no modules are selected, **then** the program shows "No modules selected. Please add modules with option 2." and goes back to the main menu.


---
#### US-5: View Self-Study Hours per Module and Week
**As a** student, **I want** to see how many hours of self-study each module requires per semester and per week, **so that** I can plan my week realistically. 

**Acceptance criteria**
- When the option to view self-study hours is selected in the main menu, the list of modules from the personalised selection will be displayed, together with the class hours and the experience level entered by the student in US-4.
- For each module, the program will display the self-study hours per semester, calculated as ((30 hrs * ECTS) - class hours) * (1 - experience %), and the self-study hours per week, calculated as self-study hours per semester / 14.
- The program will display the total self-study hours per week across all selected modules, so the student can plan the whole week realistically.
- All values will be displayed rounded to 2 decimals, while the totals are calculated from the unrounded values.
- **Given** Math represents 3 ECTS and 19.5 hours of class, **when** the student selected intermediate experience, **then** the program will display 49.3 hours of self-study per semester and 3.5 hours per week.
- **Given** the personalised selection contains Math (3 ECTS, 19.5 hours of class, intermediate experience) and Programming (6 ECTS, 39 hours of class, no previous experience), **when** the student views the self-study hours, **then** the program will display 49.3 hours per semester and 3.5 hours per week for Math, 141.00 hours per semester and 10 hours per week for Programming, and a total of 190.3 hours per semester and 13.5 hours per week.
- **However**, **given** a module was selected but its class hours or experience were not entered, **then** the program will ask the student to complete the data for that module in option 3 (US-4), and the module will not be included in the totals.

---
#### US-6: Enter Weekly availability to assess self-study time
**As a** student, **I want** to enter my free hours for each day of the week, **so that** I can see whether my free time is enough for my self-study.

**Acceptance criteria**
- When the option to enter free hours is selected in the main menu, the program will ask the student for the free hours of each day of the week, from Monday to Sunday, one day at a time.
- Each value must be a number between 0 and 24, and only 2.5 is accepted as decimals. If the value is not valid, the program will ask the student to enter it again.
- Once all seven days are entered, the program will display the free hours per day and the total free hours per week.
- The program will compare the total free hours per week with the total self-study hours per week from US-5, and will tell the student whether the free time is enough or not. If it is not enough, it will display how many hours are missing. If it is enough, it will display how many hours are left over.
- **Given** the total self-study is 16.1 hours per week (Math with intermediate experience and Programming with no previous experience), **when** the student enters 2 free hours from Monday to Friday, 4 hours on Saturday and 3.5 hours on Sunday, **then** the total free time is 14.5 hours and the program will display that the free time is not enough, with 1.4 hours left over.
- **Given** the total self-study is 16.1 hours per week, **when** the student enters 1 free hour from Monday to Friday and 0 hours on Saturday and Sunday, **then** the total free time is 5.0 hours and the program will display that the free time is not enough, with 11.1 hours missing.
- **However**, **given** a student enters a negative number, or a number higher than 24, or a non-numeric value (eg. Tbc), **then** the program will display an error message, and ask the student to enter the value again, without moving on to the next day.

---
#### US-7: Generate a Personalized Weekly Study Plan
**As a** student, **I want** to get a study plan that distributes my self-study hours over my free hours, **so that** I need less time to plan my week.

**Acceptance criteria**
- When the option to get a study plan is selected in the main menu, the program will display a weekly plan with, for each day from Monday to Sunday, the modules to study and the hours assigned to each of them.
- The weekly self-study hours of each module (US-5) will be distributed over the free hours of each day (US-6), and the hours assigned to a day will never exceed the free hours of that day.
- The program will display, for each day, the total hours planned and the free hours that remain, and, for each module, the total hours planned for the week, so the student can check that they match the weekly self-study hours of US-5.
- All values will be displayed rounded to 2 decimals, while the plan is calculated from the unrounded values.
- **Given** Math needs 3.5 hours per week (3 ECTS, 19.5 hours of class, intermediate experience), Programming needs 10 hours per week (6 ECTS, 39 hours of class, no previous experience), **when** the student has 17.5 free hours per week (2.5 hours from Monday to Friday, 3 hours on Saturday and 2 hours on Sunday), **then** the program will display the following plan: 
	- Monday: Math 2.5 h, 0.0 h remaining.
	- Tuesday: Math 1.0 h and Programming 1.5 h, 0.0 h remaining.
	- Wednesday, Thursday and Friday: Programming 2.5 h each, 0.0 h remaining.
	- Saturday: Programming 1.0 h, 2.0 h remaining.
	- Sunday: free day, 2.0 h remaining.
- The total planned is 13.5 hours (Math 3.5 h, Programming 10.0 h) and 4.0 free hours remain (2.0 h on Saturday and 2.0 h on Sunday).

- **However**, **given** the free hours were not entered, **then** the program will ask the student to enter them in the option for free hours (US-6) before coming back.

---
#### US-8: Weekly record of studied hours
**As a** student, **I want** to keep a weekly record of the hours I actually studied for each of my selected module, **so that** I can see if I am falling behind over the weeks and if so from how much.

**Acceptance criteria**
- When the option 8 is selected in the main menu, the list of modules from the personalised selection will be displayed.
- The number of the week and if the self-study is finished for said week will be asked of the student. Only if the studying is done, will the student be able to record how many hours of self-study was done per module for the chosen week.
- The amount of self-study hours the student should have invested per module per week will be displayed, as well as the previously recorded self-studied hours for the week, allowing the student to compare the two and see if the invested time was sufficient or not.
- After each recording, the program writes the file study_log.txt in the project folder: one line per selected module in the format “module;Name;class hours;level” and one line per recorded week and module in the format “week;N;Name;planned;actual”, e.g. “week;1;Mathematics_1;3.5;2.0”.
- At program start, the file is read and the message “Loaded M module(s) and W week(s).” is displayed, so the student does not have to select the modules again.
- If a week is recorded a second time, the new value replaces the old one. There is one value per module and week.
- **Given** the personalised selection of module is 1 Mathematics_1 and the student selected intermediate experience in the module, **when** the week selected is week 1, the student is all done with the self-study this week and the recorded self-study hours for this module are 2 hours, **then** the student will see that the self study hours invested for week 1 were insufficent.
- **However, given** no modules were selected, **then** the program will show the error message "No modules selected, please add modules with option 2".
- **However, given** study_log.txt does not exist at start, **then** the message “No saved data found.” is displayed and the program starts with an empty selection.

---
#### US-9: Bar chart export from beginning of semester until given week.
**As a** student, **I want** to export a bar chart of my planned and actual study hours per module from the beginning of the semester until a given week, **so that** I can see directly in which module I am behind.

**Acceptance criteria**
#### US-9: Bar chart export from beginning of semester until given week.
**As a** student, **I want** to export a bar chart of my planned and actual study hours per module from the beginning of the semester until a given week, **so that** I can see directly in which module I am behind.

**Acceptance criteria**
- When option 9 is selected in the main menu, the program asks "Show progress up to week (1 to N, Enter for N):", where N is the last week recorded in US-8. An empty input means week N. The entered week is called W below.
- For each selected module, the chart compares the planned hours (hours per week from US-5 times W) with the hours recorded in US-8 for the weeks 1 to W. A week without a record counts as 0 hours.
- The chart shows two bars per module, planned in green and actual in blue, with the title "Study progress after week W", the module names on the x-axis and "Hours" on the y-axis.
- The program saves the chart as "progress_week_WW.png" in the project folder (W as two digits, an existing file is replaced) and shows "Chart saved as progress_week_WW.png".
- **Given** Mathematics_1 and Statistics_1 are selected, Statistics_1 needs 4.8 hours per week and the student recorded 3.0 hours in week 1 and 4.0 hours in week 2 for it, **when** the student enters 2, **then** the file "progress_week_02.png" shows both modules, Statistics_1 with 9.6 h planned and 7.0 h actual, and the program shows "Chart saved as progress_week_02.png".
- **However, given** the student enters 0, a week after the last recorded one, or letters, **then** the program shows "Invalid week. Enter a number from 1 to N." and asks again.
- **However, given** no week is recorded yet, **then** the program shows "No weeks recorded yet." and creates no file.
- **However, given** no modules are selected, **then** the program shows "No modules selected. Please add modules with option 2." and displays the main menu.

---
**Use cases:**

- Show Assessement modules (from modules.txt)
- Create personalised selection (choose modules)
- Generate personalised weekly study plan
- Save recorded self-study hours (study_log.txt)
- Print Bar chart (to ----.txt)

## ✅ Project Requirements
Each app must meet the following three criteria in order to be accepted :

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)
---

### 1. Interactive App (Console Input)
The application interacts with the user via the console. Users can:
- View the assessement modules, their ECTS and a short description
- Select modules that are taken to create a personalised selection
- Remove a module from this selection
- Enter the amount of weekly hours of class per module and select their personnal experience
- View how many hours of self-study should be invested per week and per module
- Enter weekly availability to compare with the amount of self-study that should be invested
- Generate a personalised weekly study plan
- Record and save self-studied hours on a weekly basis
- Create a bar chart export to compare should be and done study hours
---

### 2. Data Validation
#To be updated with our examples.
The application validates all user input to ensure data integrity and a smooth user experience. This is implemented in `main-invoice.py` as follows:

- **Menu selection:** When the user enters a pizza number, the program checks if the input is a digit and within the valid menu range:
	```python
	if not choice.isdigit() or not (1 <= int(choice) <= len(menu)):
			print("⚠️ Invalid choice.")
			continue
	```
	This ensures only valid menu items can be ordered.

- **Quantity input:** After a pizza is selected, the program asks for the quantity until a whole number of at least 1 is entered:
	```python
	if not quantity.isdigit() or int(quantity) < 1:
			print("⚠️ Invalid quantity.")
			continue
	```
	This rejects `0`, negative numbers, decimal numbers, and text.

- **Menu file validation:** When reading the menu file, the program checks for valid price values and skips invalid lines:
	```python
	try:
			menu.append({"name": name, "size": size, "price": float(price)})
	except ValueError:
			print(f"⚠️ Skipping invalid line: {line.strip()}")
	```

- **Main menu options:** The main menu checks for valid options and handles invalid choices gracefully:
	```python
	else:
			print("⚠️ Invalid choice.")
	```

These checks prevent crashes and guide the user to provide correct input, matching the validation requirements described in the project guidelines.

---

---



### 3. File Processing

The application reads and writes data using files:

- **Input file:** `modules.txt` — Contains the assessement modules, one item per line in the format `ModuleName;ECTS;Description`.
	- Example:
		```
		Mathematics_1; 3; Think logically
		Statistics_1; 3; Decrypt data, get insights
		```
	- The application reads this file at startup to display the assessement modules.

- **Output file:** ` ` (and similar) — Generated when the weekly self-study hours are recorded. Contains the number of self-study hours per selected module per week and a total of said hours for the week.
	- Example:
		```
		
		```
		- The output file serves as a record for the user, ensuring a following on self-studied hours during the semester.

## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces
- No external libraries

### 📂 Repository Structure
```text
Basel_PT_Team_A/
├── main.py             # main program logic (console application)
├── modules.txt         # assessement modules (input data file)
├── study_log.txt             # example of a generated recorded self-study hours (output file)
├── meeting-notes.md    # our notes, deadlines and objectives for the duration of the project
└── README.md           # project description and milestones
```

### How to Run
1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
	```bash
	python3 main.py
	```

### Libraries Used

- `os`: Used for file and path operations, such as checking if the menu file exists and creating new files.
- `glob`: Used to find all invoice files matching a pattern (e.g., `invoice_*.txt`) to determine the next invoice number.

These libraries are part of the Python standard library, so no external installation is required. They were chosen for their simplicity and effectiveness in handling file management tasks in a console application.


## 👥 Team & Contributions

| Name       | Contribution                                 |
|------------|----------------------------------------------|
| Marine     | US-1, US-2 and US-8                          |
| Marcela    | US-5, US-6 and US-7                          |
| Tahir      | US-3, US-4 and US-9                          |


## 🤝 Contributing

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.


## 📝 Our assumptions and sources

1 ECTS equivalent to approx. 30 hours of work

| No. | Module | ECTS | Description |
|-----|-------|------|-----------:|
| 1 | Mathematics_1 | 3 | Think logically |
| 2 | Statistics_1 | 3 | Decrypt data, get insights |
| 3 | Principles_of_Management | 6 | Recognize organizational structures, shape and manage compagnies |
| 4 | Programming_Fundations | 6 | Gain an overall view, get to know key technologies |
| 5 | Digital_Business | 6 | Learn to code, discover the world of 0s and 1s |

Module weight -> Module overview BSc Business Information Technology part time, URL: https://www.fhnw.ch/++api++/de/wirtschaft/studium/angebot/studiengaenge/media/web_bit_cur25_moduluebersicht_tz.pdf/@@inline-file/file 
Structure of the year -> "Jahresstruktur 2025 bis FS 2031_Start Curriculum25", URL: https://fhnw365.sharepoint.com/sites/inside-HSW-Stud/Freigegebene%20Dokumente/Forms/AllItems.aspx?csf=1&web=1&e=BOKMeT&CID=edd24bad%2Daca8%2D4a72%2D8ee6%2D47d8fdc24d5f&FolderCTID=0x012000223CD24C15B3F34CBC643E657E20FD95&id=%2Fsites%2Finside%2DHSW%2DStud%2FFreigegebene%20Dokumente%2FTermine%2FDeutsch 
