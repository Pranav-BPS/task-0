# Task 0 — Python Fundamentals, Data Analysis & Git

**Name:** Pranav

## Description

This repository contains solutions to Task 0, a progressive set of exercises covering Python fundamentals, NumPy, Pandas, and Matplotlib, along with a Git/GitHub submission workflow.

- **Q1** — List analyzer (largest, smallest, sum, even/odd counts, reversed list) without using built-in `max()`, `min()`, `sum()`, `sort()`, or `sorted()`.
- **Q2** — `process_list()` function demonstrating list copying, filtering, appending, and sorting without mutating the original list.
- **Q3** — Prime number checker using Python's `for-else` control flow.
- **Q4** — NumPy array operations on student performance data (shape, dtype, mean, min/max, std, boolean indexing).
- **Q5** — Pandas analysis of `student_performance.csv` (missing values, aggregations, new columns, filtering, sorting, CSV export).
- **Q6** — Matplotlib visualizations of the processed dataset (bar chart, scatter plot, histogram, and one custom plot).

## Repository Structure

task-0/
├── README.md
├── q1.py
├── q2.py
├── q3.py
├── q4.py
├── q5.py
├── q6.py
├── data/
│ ├── student_performance.csv
│ └── processed_student_performance.csv
└── plots/
├── final_scores.png
├── study_vs_score.png
├── score_distribution.png
└── custom_plot.png


## Setup Instructions

1. Clone the repository:
```bash
   git clone https://github.com/Pranav-BPS/task-0.git
   cd task-0
```

2. (Recommended) Create a virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
```

3. Install dependencies:
```bash
   pip install numpy pandas matplotlib
```

## How to Run

Each question is a standalone script. Run them individually from the repository root:

```bash
python q1.py
python q2.py
python q3.py
python q4.py
python q5.py
python q6.py
```

- **Q1** prompts for N integers as input.
- **Q3** prompts for an upper limit N to print all primes up to that value.
- **Q5** reads `data/student_performance.csv` and writes `data/processed_student_performance.csv`.
- **Q6** reads the processed CSV from Q5 and saves all four plots into the `plots/` folder.

> Run scripts in order (Q4 → Q5 → Q6) if you're regenerating processed data and plots from scratch, since Q6 depends on Q5's output.

## Notes

- The original dataset (`student_performance.csv`) is left unmodified; all processing is saved to a separate file.
- `.gitignore` excludes virtual environment folders and Python cache files.
