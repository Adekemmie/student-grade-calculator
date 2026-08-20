# Student Grade Calculator

A simple Python application that calculates students' grades based on their course scores.

## Features

- Calculates individual course grades
- Calculates total score
- Calculates average score
- Calculates overall grade
- Validates user input
- Handles invalid inputs without crashing
- Allows multiple students to be calculated

## Grade Scale

| Score | Grade |
|-------|-------|
| 70 - 100 | A |
| 60 - 69 | B |
| 50 - 59 | C |
| 45 - 49 | D |
| 40 - 44 | E |
| Below 40 | F |

## Technologies Used

- Python 3
- PyCharm
- Git
- GitHub

## How to Run

1. Clone this repository.
2. Open the project in PyCharm.
3. Run `main.py`.
4. Enter the student's name.
5. Enter the number of courses.
6. Enter the course names and scores.
7. The program will display the results.

## Example

```text
STUDENT GRADE CALCULATOR

Enter your name: Funmibi
How many courses do you have? 3

Enter course 1 name: Python
Enter score (0-100): 85

Enter course 2 name: Mathematics
Enter score (0-100): 62

Enter course 3 name: Database
Enter score (0-100): 48

RESULTS

Course              Score     Grade
----------------------------------------
Python              85        A
Mathematics         62        B
Database            48        D

Total Score: 195
Average Score: 65.00
Overall Grade: B