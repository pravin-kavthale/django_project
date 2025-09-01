<h1 align="center">📝 Blogiin – A Modern Blog Platform with Django</h1>

<p align="center">
  <b>A clean, responsive, and full-featured blogging application built with Django.</b><br>
  Create, manage, and share your ideas effortlessly.
</p>

---

## 🔍 Overview

**Blogiin** is a full-stack blog platform developed using the Django framework.  
It provides a secure and user-friendly interface for bloggers to post, update, and manage content.  
Whether you're a casual writer or a tech blogger, Blogiin gives you the tools to express yourself.

---

## 🚀 Features

💡 **User-Friendly Authentication**  
- Secure registration & login system  
- Django's built-in auth with role-based access  

📝 **Blog Management (CRUD)**  
- Create, edit, and delete your own posts  
- View posts in a clean and organized format  
- Only authors can edit/delete their posts

🎨 **Clean & Responsive UI**  
- Built with Bootstrap 5  
- Mobile, tablet, and desktop support  
- Minimal and distraction-free layout

🛠 **Admin Interface**  
- Django admin panel for managing users and blog posts  
- Fully customizable backend for superusers

📁 **Modular & Scalable Codebase**  
- Template inheritance  
- Reusable components  
- Follows Django best practices

---

## 🧑‍💻 Tech Stack

| Technology     | Usage                        |
|----------------|------------------------------|
| Python 3.x     | Backend language             |
| Django         | Web framework                |
| SQLite         | Lightweight development DB   |
| HTML / CSS     | Markup & styling             |
| Bootstrap      | Responsive UI components     |

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally:

```bash
# Clone the repository
git clone https://github.com/your-username/blogiin.git
cd blogiin

# Create a virtual environment
python -m venv env
source env/bin/activate        # For Windows: env\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start development server
python manage.py runserver
