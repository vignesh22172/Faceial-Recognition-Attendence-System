# Faceial-Recognition-Attendence-System
🎓 Face Recognition Attendance System
📌 Project Description

This project implements a Face Recognition-based Attendance System using the LBPH (Local Binary Patterns Histogram) algorithm in Python with OpenCV.
The system automatically detects and recognizes student faces through a webcam, then records their attendance in a MySQL database.

It aims to replace manual attendance methods with a faster, more secure, and contactless solution.

⚡ Features

📷 Face Detection & Recognition using OpenCV and LBPH.

🧑‍🎓 Student Management System – add, update, delete student records.

💾 Database Integration with MySQL to store student details and attendance logs.

📊 Attendance Records stored securely for future retrieval.

🖼️ GUI Interface built with Tkinter for user-friendly interaction.

📂 Dataset Generation – captures multiple face samples per student for robust training.

🛠️ Tech Stack

Programming Language: Python

Libraries: OpenCV, Tkinter, NumPy, Pillow

Database: MySQL

Algorithm: LBPH (Local Binary Patterns Histogram)

🔑 How It Works

Dataset Collection – Capture face samples of each student via webcam.

Training the Model – Train LBPH recognizer using collected dataset.

Face Recognition – During attendance, system recognizes faces in real-time.

Attendance Marking – Recognized student’s ID, Name, Roll, and Department are logged in the database.

🚀 Future Enhancements

Improve accuracy with deep learning models (CNN, FaceNet, etc.).

Add cloud database support for remote access.

Build a web dashboard for attendance visualization.

Enable real-time alerts for unknown faces.

📚 References

OpenCV Documentation – LBPH Face Recognizer

Research Papers on LBPH and Face Recognition
