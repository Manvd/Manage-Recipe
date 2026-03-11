# 🍲 Recipe Manager (Django)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-Framework-green)
![Database](https://img.shields.io/badge/Database-SQLite-orange)
![Status](https://img.shields.io/badge/Project-Learning-blue)

A simple **Recipe Manager Web Application** built with **Django** that allows users to add, view, update, and delete recipes along with images.

This project demonstrates **Django CRUD operations**, image uploads, and basic project structure.

---

# 🚀 Features

✅ Add new recipes
✅ View list of recipes
✅ Update recipes
✅ Delete recipes
✅ Upload recipe images
✅ Simple and clean UI

---

# 🛠 Tech Stack

| Technology | Use                  |
| ---------- | -------------------- |
| Python     | Backend programming  |
| Django     | Web framework        |
| HTML       | Frontend             |
| CSS        | Styling              |
| SQLite     | Database             |
| Django ORM | Database interaction |

---

# 📂 Project Structure

```
recipe-manager/
│
├── vege/                # Django project folder
│
├── vegetable/           # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── templates/           # HTML templates
│
├── media/               # Uploaded recipe images
│
├── db.sqlite3
│
├── manage.py
│
└── README.md
```

---

# ⚙️ Installation Guide

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/recipe-manager.git
cd recipe-manager
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate it

**Windows**

```
venv\Scripts\activate
```

**Mac / Linux**

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install django
```

or

## 📦 Requirements

Make sure the following packages are installed before running the project.

### Required Packages

```bash
Django==4.2.7
Pillow==10.2.0
```


```bash
pip install django
pip install pillow
```

---

### 4️⃣ Run database migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Start the development server

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

# 📌 Future Improvements

🔹 User authentication (login/register)
🔹 Recipe search functionality
🔹 Pagination
🔹 Recipe categories
🔹 Improved UI using Bootstrap
