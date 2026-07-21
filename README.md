# NumPy Grade Tracker

A simple command-line tool that takes a student's subject-wise marks as input and generates a formatted report card — built to practice core NumPy operations like `mean`, `max`, `min`, `argmax`, `argmin`, and boolean masking.

## What it does

- Takes the number of subjects, subject names, and marks as user input
- Calculates the average mark across all subjects
- Identifies the best and worst performing subjects
- Flags each subject as PASS or FAIL (pass mark: 50)
- Displays everything in a clean, aligned report card format

## Example Output

```
=============================================
            STUDENT REPORT CARD
=============================================
Subject                  Marks     Status    
---------------------------------------------
Anthropology             91        PASS      
IT                       89        PASS      
Financial Accounting     85        PASS      
Management Accounting    78        PASS      
Economics                64        PASS      
Statistics-II            66        PASS      
---------------------------------------------
Average Marks   : 78.83
Best Subject    : Anthropology (91)
Weakest Subject : Economics (64)
=============================================
```


You'll be prompted to enter the number of subjects, followed by each subject's name and marks.


## Tech Stack

- Python 3
- NumPy
