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
- Each module is shown on its own line in the format "Number Name of the module - number of ECTS : description".
- The displayed list starts at 1. and follows the order in modules.txt
- **Given** modules.txt contains the five assesment modules, **when** the list is diplayed, **then** five line are shown.
- **However, given**   , **then**   .

forgot to push last Wednesday(tahir): **However, given** a line in modules.txt does not have the format “Number. Name; ECTS; description”, **then** this line is skipped with the message “Skipping invalid line: ...” and the other modules are still displayed.

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
When option 3 is selected in the main menu, the selected modules are displayed as a numbered list in the format "Number. Name of the module", followed by the question "Number of the module to remove (or done):".
A valid input is a number from this list. After removing, the message "Removed: Name of the module" and the remaining selection are displayed, and the question is asked again. Entering "done" returns to the main menu.
The class hours and the experience of a removed module are removed as well, so US-5 no longer counts it.
**Given** the selection is 1. Mathematics_1 and 2. Statistics_1, **when** the student enters 2, **then** the message "Removed: Statistics_1" and the remaining selection "1. Mathematics_1" are displayed, and the question is asked again.
**However, given** the student enters a number that is not in the list for example 3 or 0, text instead of a number, or nothing, **then** the message "This module is not in your selection." is displayed and the question "Number of the module to remove (or done):" is asked again.


---
#### US-4: Enter class hours and personal experience
**As a** student, **I want** to enter my class hours per week and my personal experience for each selected module, between no previous experience, intermediate or high, **so that** my self-study hours represents my personal starting point.

**Acceptance criteria**
When option 4 is selected in the main menu, the program asks two questions for each selected module: "Name of the module - class hours per week:" and "Name of the module - experience (1 = no previous experience, 2 = intermediate, 3 = high):".
Class hours are a number of 0 or more. The class hours per semester are the class hours per week times 13 class weeks. The class hours per semester must be smaller than the total workload of the module (ECTS x 30 hours). Otherwise no time would be left for self-study.
The experience is entered as the number 1, 2 or 3. It reduces the self-study hours calculated in US-5:
For no previous experience = 0%
For intermediate experience = 30%
For high experience = 60%
Self study hours for Math module (3ECTS) = ((30hrs * 3 ECTS) - class hours per semester) * (1 - experience %)
After both inputs, the line "Name of the module: class hours per week, class hours per semester, experience" is displayed, hours with two decimal places. New inputs replace the old values

**Given** Math represents 3 ECTS and 19.5 hours of class, **when** the student input intermediate experience, **then** the self study hours will be 49.35 hours.
**However, given** no modules were selected previously, **then** the message “No modules selected. Please add modules with option 2.” is displayed and the main menu is shown again.

---
#### US-5: View Self-Study Hours per Module and Week
**As a** student, **I want** to see how many hours of self-study each module requires per semester and per week, **so that** I can plan my week realistically. 

**Acceptance criteria**
- 
- **Given**   , **when**   , **then**   .
- **However, given**   , **then**   .

---
#### US-6: Enter Weekly availability to assess self-study time
**As a** student, **I want** to enter my free hours for each day of the week, **so that** I can see whether my free time is enough for my self-study.

**Acceptance criteria**
- 
- **Given**   , **when**   , **then**   .
- **However, given**   , **then**   .

---
#### US-7: Generate a Personalized Weekly Study Plan
**As a** student, **I want** to get a study plan that distributes my self-study hours over my free hours, **so that** I need less time to plan my week.

**Acceptance criteria**
- 
- **Given**   , **when**   , **then**   .
- **However, given**   , **then**   .

---
#### US-8: Weekly record of studied hours
**As a** student, **I want** to keep a weekly record of the hours I actually studied for each of my selected module, **so that** I can see if I am falling behind over the weeks and if so from how much.

**Acceptance criteria**
- When the option 8 is selected in the main menu, the list of modules from the personalised selection will be displayed.
- The number of the week and if the self-study is finished for said week will be asked of the student. Only if the studying is done, will the student be able to recorded how many hours of self-study was done per module for the chosen week.
- The amount of selt-study hours the students should have invested per module per week will be displayed, as well as the previously recorded self-studied hours for the week, allowing the student to compare the two and see if the invested time was sufficient or not.
- **Given** the personalised selection of module is 1 Mathematics_1 and the student selected intermediate experience in the module, **when** the week selected is week 1, the student is all done with the self-study this week and the recorded self-study hours for this module are 2 hours, **then** the student will see that the self study hours invested for week 1 were insufficent.
- **However, given** no modules were selected, **then** the program will ask the student to come to the main menu and select number 2.

---
#### US-9: Bar chart export from beginning of semester until given week.
**As a** student, **I want** to export a bar chart of my planned and actual study hours per module from the beginning of the semester until a given week, **so that** I can see directly in which module I am behind.
**Acceptance criteria**
When option 9 is selected in the main menu, the program asks "Until which week? (1 to N):", where N is the last week recorded in US-8.
The chart compares, for each selected module, the planned self-study hours (hours per week from US-5 times the number of weeks from week 1 to the given week) with the actual hours recorded in US-8 for these weeks. Weeks without a record count as 0 actual hours.
**Given**   , **when**   , **then**   .
**However, given** modules are selected but no week is recorded yet, **then** the message "No weeks recorded yet." is displayed and no file is created.
**However, given** no modules were selected previously, **then** the message "No modules selected. Please add modules with option 2." is displayed and the main menu is shown again.
---

**Use cases:**

Show Assessement modules (from modules.txt)
Create personalised selection (choose modules)
Generate personalised weekly study plan
Print Bar chart (to ----.txt)

## ✅ Project Requirements
Each app must meet the following three criteria in order to be accepted :

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)
---
The application interacts with the user via the console. Users can:
- View the assessement modules, their ECTS and a short description
- Select modules that are taken to create a personalised selection
- Remove a module from this selection
- Enter the amount of weekly hours of class per module and select their personnal experience
- View how many hours of self-study should be invested per week and per module
- Enter weekly availability to compare with the amount of self-study that should be invested
- Generate a personalised weekly study plan
- Record self-studied hours on a weekly basis
- Create a bar chart export to compare should be and done study hours

### 1. Interactive App (Console Input)

---

### 2. Data Validation

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
├── ---.txt             # example of a generated recorded self-study hours (output file)
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
