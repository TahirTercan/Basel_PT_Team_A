# Study Planner (Console)

## 📝 Analysis

**Problem**
Part-time students (who) experiences difficulty planning how many hours of self study their 
modules require per week (what), when they plan their week alongside their job and FH 
lectures (where) resulting in too little time for self-study and fall behind (why).​


**Scenario**

Study Planner solves the part of the problem where the weekly self-study hours are worked out and distributed: a student selects the modules of the semester, enters the class hours and the free hours of the week, and gets the self-study hours per module and a study plan for the week. 

### 👤 User Roles

| Role | Description |
|------|-------------|
| **Student** | A part-time BSc BIT student who works alongside the degree programme and plans the weekly self-study for the modules of the current semester. |


### 📖 User Stories

> 🚧 **How to write a good user story**
>
> - Use the scheme **"As a *&lt;role&gt;*, I want *&lt;capability&gt;*, so that *&lt;benefit&gt;*."**
>   The benefit ("so that …") explains *why* the story is valuable. If you cannot name a benefit, question whether the story is needed.
> - A story consists of three parts, the "three Cs": the **Card** (the short sentence), the **Conversation** (the details discussed within the team), and the **Confirmation** (the acceptance criteria, which show when the story is done).
> - Check each story against **INVEST**: **I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall, **T**estable.
> - **Acceptance criteria** must be *specific* and *testable*. Use concrete values (e.g., "CHF 25.00", "two decimal places") and avoid vague words such as "fast", "easy", "correct", or "user-friendly". A good criterion can be turned directly into a test case with an input and an expected output.
> - Write acceptance criteria either as a **checklist** of observable rules or in the **Given–When–Then** structure:
>   *Given* a starting situation, *when* an action happens, *then* a specific, observable result occurs.
> - Include at least one criterion for the **normal case** and one for an **edge case or invalid input** (e.g., a quantity of 0, an empty order, a missing file).
>
> 💡 The stories below are examples for PizzaRP. Replace them with the stories of your own project.

All prices are in Swiss francs (CHF). The examples use the following menu from `menu.txt`:

| No. | Pizza | Size | Unit price |
|-----|-------|------|-----------:|
| 1 | Margherita | Medium | CHF 12.50 |
| 2 | Salami | Large | CHF 15.00 |
| 3 | Funghi | Small | CHF 9.00 |
| 4 | Hawaii | Medium | CHF 14.00 |
| 5 | Diavola | Large | CHF 17.50 |



## US-1 : List of the assesment modules
### As a **student**, **I want** to see a numbered list of the five assesment modules of my programm with their ECTS and a short description of each of them, **so that** I can have an overview of the modules of the first semester without looking them up somewhere else. 
#### Assigned to :
--> Marine
#### Acceptance criteria :
The assesment modules list, their ECTS and descritpion are diplayed when option 1 in the main menu.
Each module is shown on its own line in the format "Number. Name of the module - number of ECTS : description".
The displayed list starts at 1. and follows the order in modules.txt
#### Example :
**Given** modules.txt contains the five assesment modules, **when** the list is diplayed, **then** five line are shown.
#### Edge cases :
**However, given**   , **then**   .

## US-2 : Select modules to calculate overall hours for each 
### As a **student**, **I want** to add modules from the list to my selection, **so that** the calculated overall hours for the whole semester to match my own.
#### Assigned to :
--> Marine
#### Acceptance criteria :
The list a modules with their associated number is displayed to allow the student to know with number should be selected depending on which class is taken, in the format "Number. Name of the module", when selecting option 2 in the main menu.
The programm will ask which module should be added to the personalised selection.
If the selection is done, the calculation of the overall hours of the selected modules will be displayed. Each line will display one module and its associated overall hours in the format "Number. Name of the module - Number of ECTS : Overall hours for the semester".
#### Example :
**Given** the selected modules are 1 and 2,**when** the selection is done, **then** the calculated overall hours for both of those modules will be displayed, eg :
1. Mathematics_1 - 3 ECTS : 90 hours overall for this module.
2. Statistics_1 - 3 ECTS : 90 hours overall for this module.
#### Edge cases :
**However, given** a number is not an option in the list,  **then** the message "This module doesn't exist." will be displayed and the selecting question will be asked again.
**However, given** a number is already selected, **then** the message "The module is already selected." will be displayed and the selecting question will be asked again.
**However, given** the selection comprise every possible modules, **then** the messsage "All modules are already selected!" will be displayed.

---

### 3. As a student, I want to remove a selected module, so that I can correct a wrong entry without re-entering everything again. 
#### Assigned to :
--> Tahir
#### Acceptance criteria :

#### Example :

#### Edge cases :

---

### 4. As a student, I want to enter my class hours per week and my personal experience for each selected module, so that my self-study hours represents my personal starting point.
#### Assigned to :
--> Tahir
#### Acceptance criteria :

#### Example :

#### Edge cases :

---

## US-5: View Self-Study Hours per Module and Week. 
### As a **student**, **I want** to see how many hours of self-study each module requires per semester and per week, **so that** I can plan my week realistically. 
#### Assigned to :
--> Marcela
#### Acceptance criteria :

#### Example :

#### Edge cases :

---

## US-6: Enter Weekly Availability to Assess Self-Study Time.
### As a **student**, **I want** to enter my free hours for each day of the week, **so that** I can see whether my free time is enough for my self-study.
#### Assigned to :
--> Marcela
#### Acceptance criteria :

#### Example :

#### Edge cases :

## US-7: Generate a Personalized Weekly Study Plan.	
### As a **student**, **I want** to get a study plan that distributes my self-study hours over my free hours, **so that** I need less time to plan my week.
#### Assigned to :
--> Marcela
#### Acceptance criteria :

#### Example :

#### Edge cases :

## US-8 : Weekly record of studied hours
### As a **student**, **I want** to keep a weekly record of the hours I actually studied for each of my selected module, **so that** I can see if I am falling behind over the weeks and if so from how much.
#### Assigned to :
--> Marine
#### Acceptance criteria :
When the option 8 is selected in the main menu, the list of modules from the personalised selection will be displayed.
#### Example :
**Given**   , **when**   , **then**   .
#### Edge cases :
**However, given**   , **then**   .

---

### 9. 	As a student, I want to export a bar chart of my planned and actual study hours per module, so that I can see directly in which module I am behind.
#### Assigned to :
--> Tahir
#### Acceptance criteria :

#### Example :

#### Edge cases :

---

**Use cases:**

## ✅ Project Requirements

---

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

- **Input file:** `menu.txt` — Contains the pizza menu, one item per line in the format `PizzaName;Size;Price`.
	- Example:
		```
		Margherita;Medium;12.50
		Salami;Large;15.00
		Funghi;Small;9.00
		```
	- The application reads this file at startup to display available pizzas.

- **Output file:** `invoice_001.txt` (and similar) — Generated when an order is completed. Contains a summary of the order, including items, quantities, prices, discounts, and totals.
	- Example:
		```
		🍕 PIZZA RP INVOICE
		---------------------
		3x Diavola (Large) - CHF 52.50
		---------------------
		Discount: 10% discount (-CHF 5.25)
		TOTAL: CHF 47.25
		```
		- The output file serves as a record for both the user and the pizzeria, ensuring accuracy and transparency.

## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces
- No external libraries

### 📂 Repository Structure
```text
PizzaRP/
├── main.py             # main program logic (console application)
├── menu.txt            # pizza menu (input data file)
├── invoice_001.txt     # example of a generated invoice (output file)
├── docs/               # optional screenshots or project documentation
└── README.md           # project description and milestones
```

### How to Run
> 🚧 Adjust if needed.
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

> 🚧 Fill in the names of all team members and describe their individual contributions below. Each student should be responsible for at least one part of the project.

| Name       | Contribution                                 |
|------------|----------------------------------------------|
| Student A  | Menu reading (file input) and displaying menu|
| Student B  | Order logic and data validation              |
| Student C  | Invoice generation (file output) and slides  |


## 🤝 Contributing

> 🚧 This is a template repository for student projects.  
> 🚧 Do not change this section in your final submission.

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)


## Our assumptions and sources
1 ECTS equivalent to approx. 30 hours of work
Module weight -> Module overview BSc Business Information Technology part time, URL: https://www.fhnw.ch/++api++/de/wirtschaft/studium/angebot/studiengaenge/media/web_bit_cur25_moduluebersicht_tz.pdf/@@inline-file/file 
Structure of the year -> "Jahresstruktur 2025 bis FS 2031_Start Curriculum25", URL: https://fhnw365.sharepoint.com/sites/inside-HSW-Stud/Freigegebene%20Dokumente/Forms/AllItems.aspx?csf=1&web=1&e=BOKMeT&CID=edd24bad%2Daca8%2D4a72%2D8ee6%2D47d8fdc24d5f&FolderCTID=0x012000223CD24C15B3F34CBC643E657E20FD95&id=%2Fsites%2Finside%2DHSW%2DStud%2FFreigegebene%20Dokumente%2FTermine%2FDeutsch 
