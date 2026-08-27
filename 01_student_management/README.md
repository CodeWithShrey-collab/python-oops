# Student Management System

A beginner-friendly Python project built to understand the fundamentals of **Object-Oriented Programming (OOP)** through a simple Student Management System.

## Features

* Add a new student
* View all students
* Search student by roll number
* Update student marks
* Automatically calculate grades
* Save student data using JSON
* Load saved student data when the program starts
* Handle missing JSON file without crashing

## OOP Concepts Used

* Classes and Objects
* `__init__()` constructor
* `self`
* Instance attributes
* Instance methods
* Object creation
* Lists of objects
* Separation of data and behaviour

## Additional Python Concepts

* JSON file handling
* `try-except`
* File read/write operations
* Loops and conditions
* Functions
* Lists and dictionaries

## Project Structure

```text
01_student_management/
│
├── main.py
├── README.md
└── students.json
```

> `students.json` is generated automatically while running the program and is ignored by Git.

## How It Works

When a student is added, a `Student` object is created:

```python
student = Student(name, roll, marks)
```

The object stores information such as:

```text
name
roll number
marks
```

All student objects are stored inside a list.

```python
students = []
```

Before saving the data, each `Student` object is converted into a dictionary.

```python
def to_dict(self):
    return {
        "name": self.name,
        "roll": self.roll,
        "marks": self.marks
    }
```

The dictionaries are then stored inside `students.json`.

When the program starts again, the JSON data is loaded and converted back into `Student` objects.

## Menu

```text
1. Add Student
2. View Students
3. Search Student
4. Update Marks
5. Exit
```

## Grade Calculation

```text
90 and above  -> A
75 - 89       -> B
60 - 74       -> C
Below 60      -> D
```

## Run the Project

Navigate to the project folder:

```bash
cd 01_student_management
```

Run:

```bash
python main.py
```

## Learning Progression

### Version 1

The first version focused on basic OOP concepts:

* Creating a class
* Creating objects
* Using `self`
* Using `__init__`
* Instance methods
* Storing multiple objects in a list

### Version 2

The project was upgraded with persistent storage using JSON.

The flow is:

```text
Student Object
      ↓
Dictionary
      ↓
JSON File
```

When loading:

```text
JSON File
      ↓
Dictionary
      ↓
Student Object
```

This allows student information to remain available even after the program is closed and restarted.

## Key Learning

The main goal of this project was to understand the difference between:

```text
Data stored in RAM
        vs
Data stored permanently
```

A Python list only exists while the program is running.

Using JSON allows the program to save the data permanently and recreate the objects the next time the program starts.

---

This is **Project 01** of my Python OOP learning journey from basic to advanced.
