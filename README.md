# Expense Analytics & Personal Finance System 💰

A Python-based personal finance system for managing, storing, and eventually analyzing personal expense data.

The project is being developed progressively, starting with a command-line expense management system and expanding into a complete data analytics project using **Pandas, data cleaning, exploratory data analysis, and visualization**.

---

## 📌 Project Overview

Managing personal expenses manually makes it difficult to understand where money is being spent and identify spending patterns.

This project aims to build a system that can:

* Store and manage expense transactions
* Add, view, update, and delete expenses
* Validate user input
* Persist transaction data using CSV
* Analyze spending patterns
* Generate meaningful financial insights
* Visualize expense trends

The project is currently in the **Expense Management / Data Management phase**. The analytics layer will be added progressively.

---

## 🎯 Current Features

The current version is a command-line application that supports:

### Expense Management

* Add a new expense
* View all transactions
* Update an existing expense
* Delete an expense
* Automatically generate transaction IDs
* Save changes to the CSV dataset

### Input Validation

The application currently validates:

* Integer inputs
* Expense amounts
* Dates
* Categories
* Transaction IDs

For example, expense amounts must be positive and dates must follow:

```text
YYYY-MM-DD
```

Categories are not restricted to a predefined list, allowing users to create categories according to their own requirements.

---

## 🗂️ Project Structure

```text
Expense-Analytics/
│
├── data/
│   └── transactions.csv
│
├── src/
│   ├── __init__.py
│   └── expense_manager.py
│
├── main.py
├── problem_statement.txt
└── README.md
```

### File Description

**`main.py`**

Contains the command-line interface and controls the main application flow.

**`src/expense_manager.py`**

Contains the core expense-management functionality, including:

* Loading transactions
* Saving transactions
* Adding expenses
* Viewing transactions
* Updating expenses
* Deleting expenses
* Input validation

**`data/transactions.csv`**

Stores the expense transaction data.

**`problem_statement.txt`**

Contains the original problem definition and project requirements.

---

## 🛠️ Technologies Used

Currently:

* **Python**
* **CSV**
* **datetime**
* **Git & GitHub**

Planned:

* **Pandas**
* **Matplotlib**
* **Seaborn**

---

## 🔄 Current Data Flow

```text
User Input
     ↓
Python CLI
     ↓
Input Validation
     ↓
Expense Management
     ↓
transactions.csv
```

The application loads the existing transactions when it starts and saves changes back to the CSV file whenever transactions are added, updated, or deleted.

---

## 📊 Planned Analytics

The next phase of the project will introduce **Pandas** and transform the project from an expense management application into a data analytics system.

Planned analysis includes:

* Total expenditure
* Average transaction amount
* Spending by category
* Spending by payment method
* Daily spending patterns
* Highest and lowest expenses
* Category-wise spending comparison
* Spending trends
* Data cleaning and validation
* Exploratory Data Analysis (EDA)
* Data visualization
* Financial insights

---

## 🚧 Project Status

### Completed

* [x] Project setup
* [x] CSV dataset creation
* [x] CSV data loading
* [x] CSV data saving
* [x] Add expense
* [x] View expenses
* [x] Update expense
* [x] Delete expense
* [x] Transaction ID generation
* [x] Integer input validation
* [x] Amount validation
* [x] Date validation
* [x] Category validation
* [x] Basic CLI interface
* [x] Git/GitHub setup

---

## 🚀 Future Goal

The final goal is to turn this project into an end-to-end personal finance analytics system:

```text
Transaction Dataset
        ↓
Data Loading & Validation
        ↓
Expense Management
        ↓
Data Cleaning
        ↓
Pandas Analysis
        ↓
Exploratory Data Analysis
        ↓
Visualization
        ↓
Financial Insights
```

The project will be expanded incrementally as new analytics capabilities are implemented.
