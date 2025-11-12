# 🧪 OOP Lab 3 — Data Processing with CSV, Tables, and Simple Database

## 📘 Lab Overview
This lab demonstrates how to design and implement an **object-oriented Python program** that can process and analyze CSV data.  
You will:
- Load data from CSV files using a reusable class.
- Represent tabular data using objects.
- Store and retrieve data using a simple in-memory database.
- Apply filtering, aggregation, and join operations — all using OOP principles.

The lab reinforces **encapsulation, abstraction, and composition** while working with real-world datasets such as `Cities.csv` and `Countries.csv`.

---

## 📁 Project Structure


---

## ⚙️ Design Overview

### **1. DataLoader**
Handles reading and loading CSV files.

**Attributes**
- `base_path`: The folder path where data files are stored.

**Methods**
- `load_csv(filename)`: Reads a CSV file and returns a list of dictionaries, each representing a row of data.

---

### **2. DB**
A simple in-memory database to store and retrieve tables.

**Attributes**
- `data`: Dictionary mapping table names to their `Table` objects.

**Methods**
- `insert(table)`: Inserts a table into the database.
- `search(name)`: Retrieves a table by name.

---

### **3. Table**
Represents and manipulates tabular data such as cities and countries.

**Attributes**
- `name`: Name of the table.
- `table_name`: Used for display in `__str__`.
- `table`: List of dictionaries (rows).

**Methods**
- `filter(condition)`: Returns a new `Table` with rows satisfying a given condition (lambda function).
- `aggregate(aggregation_function, aggregation_key)`: Performs calculations like average, min, max, or count.
- `join(other_table, key)`: Combines two tables based on a shared key (like SQL inner join).
- `__str__()`: Returns a string representation of the table.

---

## ▶️ How to Run and Test

### **Requirements**
- Python 3.7 or higher  
- `Cities.csv` and `Countries.csv` located in the same directory as `data_processing.py`

### **Steps**
1. Open a terminal or IDE.
2. Navigate to your project folder:
   ```bash
   cd path/to/oop_lab_3
