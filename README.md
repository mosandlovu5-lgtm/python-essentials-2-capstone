# Student Analytics Toolkit

A terminal-based Python application that generates messy student data, cleans and models it as objects, analyses academic performance, and exports a detailed report. The project combines Python Essentials 2 concepts including file handling, object-oriented programming, generators, closures, iterators, and standard-library modules.

## Author

**Name:** Mosa Ndlovu

**Cohort:** 2026 DS Jan Cohort

## Features

- Generates a sample file containing deliberately messy student names and scores
- Cleans names and converts scores into usable numeric data
- Models students with `Student` and `HonoursStudent` classes
- Calculates class average, pass rate, highest score, and lowest score
- Filters passing students with a generator
- Grades students against a user-selected pass mark using a closure
- Produces environment, date, and calendar information
- Exports analysis results to `data/report.txt`
- Saves program activity in `data/activity.log`
- Handles invalid menu and number input without crashing

## How to Run

1. Clone the repository:

   ```powershell
   git clone https://github.com/mosandlovu5-lgtm/python-essentials-2-capstone.git
   ```

2. Move into the project folder:

   ```powershell
   cd python-essentials-2-capstone
   ```

3. Install requirements:

   ```powershell
   pip install -r requirements.txt
   ```

4. Run the program:

   ```powershell
   python main.py
   ```

5. In the menu, choose option `1` to create sample data, then option `2` to load and clean it.

## Project Structure

- `main.py` - Runs the menu and connects all project modules.
- `models.py` - Contains the `Student` and `HonoursStudent` classes.
- `data_tools.py` - Generates, cleans, reads, writes, exports, and logs data.
- `analytics.py` - Contains statistics, the passing-students generator, the grading closure, and iterator use.
- `reporting.py` - Creates environment, date, and calendar reports.
- `requirements.txt` - Lists required packages; this project uses only the Python standard library.
- `data/` - Stores generated student data, reports, and activity logs.

## Concepts Demonstrated

This project demonstrates the Python Essentials 2 skills below:

- **File handling:** Uses `with open()` to generate data, read records, export reports, and append activity logs.
- **String cleaning:** Uses `strip()`, `split()`, `lower()`, `title()`, and `int()` to clean messy names and scores.
- **Object-oriented programming:** Uses classes, constructors, instance variables, class variables, methods, inheritance, `super()`, overriding, and `__str__`.
- **Generators:** Uses `yield` to produce passing students one at a time.
- **Closures:** Uses `make_grader(pass_mark)` to create a function that remembers a custom pass mark.
- **Iterators:** Uses `iter()` and `next()` to preview student scores safely.
- **Standard library:** Uses `random`, `pathlib`, `datetime`, `calendar`, `platform`, `os`, and `statistics`.
- **Error handling:** Uses `try-except` to prevent invalid user input from crashing the program.

## Sample Output

```text
===== STUDENT ANALYTICS TOOLKIT =====
1. Generate sample data file
2. Load & clean records from file
3. View all students
4. Analyse (averages, pass/fail, top student)
5. Filter students (generator)
6. Grade with a custom pass mark (closure)
7. Environment & date report
8. Export results to a file
9. Exit
Choose an option (1-9): 4

STUDENT ANALYSIS
Students loaded: 10
Class average: 69.40
Pass rate: 70.0%
Top student: S4: Lebo Molefe | Score: 91 | Grade: Distinction (Honours)
Lowest student: S8: James Brown | Score: 42 | Grade: Fail
First scores via iterator: [73, 65]
```
