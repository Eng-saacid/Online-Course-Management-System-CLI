# Online Course Management System CLI

## 📌 Project Description

Online Course Management System CLI is a command-line based application developed using Python.
The system helps manage students, teachers, courses, enrollments, and grades efficiently.

This project uses:

* Python
* JSON file storage
* Object-Oriented Programming (OOP)
* Role-Based Authentication System

---

# 🚀 Features

## 👨‍💼 Admin

* Manage students
* Manage teachers
* Manage courses
* Manage enrollments
* Manage grades
* Register new users

## 👨‍🏫 Teacher

* View students
* View courses
* Add and manage grades

## 👨‍🎓 Student

* View enrolled courses
* View grades

---

# 🔐 Authentication System

The system includes:

* Login system
* Register system
* Role-based access control

Roles:

* Admin
* Teacher
* Student

---

# 📚 Modules Included

* Student Management
* Teacher Management
* Course Management
* Enrollment Management
* Grade Management
* Authentication System

---

# 🧠 Grade System

The grading system supports:

* Numeric grades (0–100)
* Automatic letter grade conversion

Example:

* 90–100 → A+
* 80–89 → A
* 70–79 → B
* 60–69 → C
* 50–59 → D
* Below 50 → F

---

# 🗂️ Project Structure

```bash
project/
│
├── main.py
├── auth.py
├── dashboards.py
│
├── services/
│   ├── student_service.py
│   ├── teacher_service.py
│   ├── course_service.py
│   ├── grade_service.py
│
├── utils/
│   ├── helpers.py
│   ├── storage.py
│
├── data/
│   └── data.json
│
└── README.md
```

---

# ⚙️ Technologies Used

* Python 3
* JSON
* OOP Concepts
* CLI Interface

---

# ▶️ How to Run

## 1. Clone Repository

```bash
git clone <repository-link>
```

## 2. Open Project Folder

```bash
cd project-folder
```

## 3. Run Application

```bash
python main.py
```

---

# 📦 Data Storage

The project stores all data inside:

```bash
data.json
```

Data includes:

* Users
* Students
* Teachers
* Courses
* Enrollments
* Grades

---

# 🛡️ System Validation

The system prevents:

* Duplicate users
* Duplicate enrollments
* Duplicate grades
* Invalid grade values

---

# 🎯 Learning Objectives

This project demonstrates:

* Python OOP
* File Handling
* CRUD Operations
* Authentication Systems
* Data Validation
* CLI Application Development

---

# 👨‍💻 Author

Developed by: Eng-Saacid Abdiaziz yusuf

---

# 📄 License

This project is for educational purposes.
