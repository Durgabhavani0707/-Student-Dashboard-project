🎓 **Student Progress Dashboard**

A simple full-stack web application to track student academic progress category-wise.

 🚀 Features

* 📊 Category-wise progress tracking
* ✅ Completed vs Remaining subjects
* 🎯 Fixed academic structure (AUC, PCC, etc.)
* 🎨 Modern animated UI
* ⚡ Fast API using Flask
* 🔗 Frontend connected with backend using Fetch API



 🛠️ Tech Stack

 🔹 Frontend

* HTML
* CSS (Glassmorphism + Animations)
* JavaScript

 🔹 Backend

* Python
* Flask

 🔹 Database

* MySQL



 📂 Project Structure


project/
│
├── app.py                # Flask backend
├── index.html           # Login page
├── dashboard.html       # Dashboard UI
└── database.sql         # MySQL table (optional)


 ⚙️ How It Works

1. User enters Register Number
2. Frontend sends request to backend API
3. Flask fetches data from MySQL
4. Calculates:

   * Total subjects (fixed)
   * Completed subjects
   * Remaining subjects
   * Progress %
5. Sends JSON response
6. Frontend displays animated dashboard



 🔌 API Endpoint

GET /dashboard/<regno>


 Example Response:

[
  {
    "category": "AUC",
    "total": 7,
    "completed": 3,
    "remaining": 4,
    "progress": 42
  }
]


 🧠 Logic Used

* Total subjects are predefined per category
* Completed subjects are counted from database
* Progress is calculated using:


progress = (completed / total) * 100

 ▶️ How to Run

 1️⃣ Install dependencies


pip install flask flask-cors mysql-connector-python


 2️⃣ Run backend

python app.py


 3️⃣ Open frontend

* Open `index.html` in browser

🗄️ Database Structure

Table: `subjects`

| Column       | Type     |
| ------------ | -------- |
| id           | int (PK) |
| regno        | varchar  |
| category     | varchar  |
| subject_name | varchar  |
| status       | varchar  |


📌 Future Improvements

* 🔐 Login authentication
* 📊 Charts & analytics
* 👨‍🏫 Admin panel
* 📱 Mobile responsive design

 👩‍💻 Author

A DURGA BHAVANI


LIVE DEMO : https://studentdashboard-project.vercel.app/

⭐ Note

This project is built for learning full-stack development using Flask and MySQL.
