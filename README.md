# Student Grade Analyzer

A NumPy project that analyzes student grades across multiple subjects — computing per-student and per-subject averages, ranking students by performance, and flagging those below a pass threshold.

## What it does

- Loads student grade data into a structured NumPy array (`load_data.py`)
- Cleans each subject column — detects `inf`/`NaN`, converts `inf` → `NaN`, and imputes missing values with the column mean (`clean_data.py`)
- Stacks the cleaned subject columns into a single 2D array (students × subjects) using `np.column_stack()`
- Computes:
  - **Per-student average** (`axis=1`) — average score across all subjects for each student
  - **Per-subject average** (`axis=0`) — average score across all students for each subject
- Ranks students from highest to lowest average using `np.argsort()`
- Flags students below a pass threshold using boolean masking

## Why `axis=0` vs `axis=1` matters

In a 2D array, aggregation functions need to know *which direction* to collapse:
- `axis=0` collapses rows → one result per **column** (per subject)
- `axis=1` collapses columns → one result per **row** (per student)

Getting this backwards silently gives the wrong numbers (e.g. per-subject averages where per-student ones were needed) without raising an error — so it's worth checking output makes sense, not just that the code runs.

## Project structure

```
student-grade-analyzer/
├── load_data.py    # loads grade data into a structured NumPy array
├── clean_data.py   # clean_column(): detects inf/NaN, imputes with mean
│                    # clean_all_subjects(): applies clean_column() to every
│                    # subject and stacks results into a 2D array
├── analyze.py       # per-student & per-subject averages, ranking, pass/fail flagging
├── main.py          # runs the full pipeline
├── student_grades.csv
└── README.md
```

## Usage

```bash
python main.py
```

Loads the dataset, cleans each subject's scores, prints per-subject averages, a ranked list of students (highest to lowest average), and flags any student below the pass threshold.

## Key concepts practiced

- 2D array construction with `np.column_stack()`
- `axis=0` vs `axis=1` aggregation
- `np.argsort()` for ranking without losing track of original student positions
- Boolean masking for pass/fail flagging
- Missing-value handling extended from a single 1D column to multiple columns via a reusable function

## Status

Complete — pipeline verified end-to-end (load → clean → analyze) with a dummy dataset of 20 students across 5 subjects. Built while learning NumPy fundamentals: 2D arrays, axis-based aggregation, sorting, and boolean masking.