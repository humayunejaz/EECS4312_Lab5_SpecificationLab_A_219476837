## TODO: 
## Student Name: Humayun Ejaz
## Student ID: 219476837

# Meeting Slot Suggestion Lab Repository

This repository contains the starter code, templates, and tests for the **Requirements Specification II** lab. Students will implement a meeting slot suggestion function, write specifications, and explore the impact of requirements completeness on AI‑assisted coding.

## System Description
You are asked to implement a Python function that suggests possible meeting time slots for a given day. The function takes as input a list of existing calendar events for that day and a desired meeting duration. Its goal is to return a list of valid start times at which the meeting could be scheduled. A valid time slot should respect typical working hours and should not conflict with existing events. If no suitable time slots are available, the function should return an empty list. You may assume that time values are provided in a standard string format (e.g., “09:30”), and you are free to choose an appropriate internal representation. You may use ChatGPT to assist with reasoning about the problem, generating code, or writing tests. 

## Structure

- **src/solution.py** – starter file where you implement `suggest_slots`. Do not rename this file.
- **test_solution.py** – Public tests you can run to check basic correctness. Use a test runner such as `pytest` to execute these tests.


## Running Tests

1. Install Python 3 if not already installed.
2. Implement your solution in `solution.py`.
3. Optionally create `student_tests.py` and write at least 5 test cases.
4. Run tests using:

```bash
pytest file_name.py
```

5. Fix any failing tests before moving on. Remember that hidden tests will check additional requirements.

## Submitting Your Work
Follow the instruction in the manual.
