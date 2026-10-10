# Study Planner

## A simple application to help part-time students organize their study time.

## The problem:
Part-time students (who) experiences difficulty planning how many hours of self study their 
modules require per week (what), when they plan their week alongside their job and FH 
lectures (where) resulting in too little time for self-study and fall behind (why).​

## Project Goal:
Make the weekly self-study planning of part-time students more efficient and more effective: 
less time needed for planning and fewer weeks with too little self-study.

## Scenario ## 

Study Planner solves the part of the problem where the weekly self-study hours are worked out and distributed: a student selects the modules of the semester, enters the class hours and the free hours of the week, and gets the self-study hours per module and a study plan for the week. 

## User Roles ## 

| Role | Description |
|------|-------------|
| **Student** | A part-time BSc BIT student who works alongside the degree programme and plans the weekly self-study for the modules of the current semester. |


## User stories:


## US-1 : List of the assesment modules
### As a **student**, **I want** to see a numbered list of the five assesment modules of my programm with their ECTS and a short description of each of them, **so that** I can have an overview of the modules of the first semester without looking them up somewhere else. 
#### Assigned to :
--> Marine
#### Acceptance criteria :
The assesment modules list, their ECTS and descritpion are diplayed when option 1 in the main menu.
Each module is shown on its own line in the format <No>. <Name of the module> - <number of ECTS> : <description>.
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
The list a modules with their associated number is displayed to allow the student to know with number should be selected depending on which class is taken, in the format <No>. <Name of the module>, when selecting option 2 in the main menu.
The programm will ask which module should be added to the personalised selection.
If the selection is done, the calculation of the overall hours of the selected modules will be displayed. Each line will display one module and its associated overall hours in the format <No>. <Name of the module> - <number of ECTS> ECTS : <Overall hours for the semester> hours for this module.
#### Example :
**Given** the selected modules are 1 and 2,**when** the selection is done, **then** the calculated overall hours for both of those modules will be displayed, eg :
1. Mathematics_1 - 3 ECTS : 90 hours overall for this module.
2. Statistics_1 - 3 ECTS : 90 hours overall for this module.
#### Edge cases :
**However, given** a number is not an option in the list,  **then** the message "This module doesn't exist." will be displayed and the selecting question will be asked again.
**However, given** a number is already selected, **then** the message "The module is already selected." will be displayed and the selecting question will be asked again.
**However, given** the selection comprise every possible modules, **then** the messsage "All modules are already selected!" will be displayed.

### 3. As a student, I want to remove a selected module, so that I can correct a wrong entry without re-entering everything. 
#### Assigned to :
--> Tahir
#### Acceptance criteria :

#### Example :

#### Edge cases :

### 4. As a student, I want to enter my class hours per week for each selected module, so that I do not plan my time in class twice.
#### Assigned to :
--> Tahir
#### Acceptance criteria :

#### Example :

#### Edge cases :

## US-5: View Self-Study Hours per Module and Week. 
### As a **student**, **I want** to see how many hours of self-study each module requires per semester and per week, **so that** I can plan my week realistically. 
#### Assigned to :
--> Marcela
#### Acceptance criteria :

#### Example :

#### Edge cases :

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

### 9. 	As a student, I want my selected modules, class hours and free time to be saved for the next session, so that I do not have to enter everything again every week.
#### Assigned to :
--> Tahir
#### Acceptance criteria :

#### Example :

#### Edge cases :



## Our assumptions and sources
1 ECTS equivalent to approx. 30 hours of work
Module weight -> Module overview BSc Business Information Technology part time, URL: https://www.fhnw.ch/++api++/de/wirtschaft/studium/angebot/studiengaenge/media/web_bit_cur25_moduluebersicht_tz.pdf/@@inline-file/file 
Structure of the year -> "Jahresstruktur 2025 bis FS 2031_Start Curriculum25", URL: https://fhnw365.sharepoint.com/sites/inside-HSW-Stud/Freigegebene%20Dokumente/Forms/AllItems.aspx?csf=1&web=1&e=BOKMeT&CID=edd24bad%2Daca8%2D4a72%2D8ee6%2D47d8fdc24d5f&FolderCTID=0x012000223CD24C15B3F34CBC643E657E20FD95&id=%2Fsites%2Finside%2DHSW%2DStud%2FFreigegebene%20Dokumente%2FTermine%2FDeutsch 
