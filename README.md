# AI Placement Mentor API

An intelligent placement readiness assessment API built with FastAPI, Machine Learning, and Google's Gemini AI.

The project evaluates student performance in Aptitude, Communication, and Coding skills, predicts placement eligibility using a Decision Tree Classification model, and generates personalized improvement suggestions using Gemini AI.

## Project Overview

Preparing for campus placements often requires students to understand their strengths and weaknesses across multiple skill areas.

This project acts as an AI-powered placement mentor by:

* Evaluating student scores
* Predicting placement eligibility using Machine Learning
* Generating personalized preparation advice using Gemini AI
* Storing student records for future analysis

The API demonstrates how traditional Machine Learning and Large Language Models can work together to create practical career guidance applications.

## Features

* Aptitude
* Communication
* Coding

### Student Assessment

Calculates:

* Total Score
* Average Score

using a custom evaluation module.

### Placement Prediction

Uses a Decision Tree Classifier trained on historical student data to predict:

* Eligible
* Not Eligible

placement status.

### AI Mentor Advice

Integrates with Gemini AI to provide:

* Skill analysis
* Personalized recommendations
* Practical improvement plans

based on student performance.

### Data Persistence

Stores all student records in a CSV-based database: student_data.csv

### REST API

Built using FastAPI for fast and modern API development.

---

## Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Core Programming Language       |
| FastAPI       | REST API Framework              |
| Pandas        | Data Management                 |
| NumPy         | Numerical Operations            |
| Scikit-Learn  | Machine Learning                |
| Gemini AI     | Personalized Mentor Advice      |
| Pydantic      | Request Validation              |
| Python Dotenv | Environment Variable Management |

## Project Structure

```text
AI-Placement-Mentor-API/
│
├── app.py
├── evaluation.py
├── prediction_model.py
├── student_data.csv
│
├── .env.example
├── .gitignore
├── requirements.txt
│
└── README.md
```

## How It Works

### Step 1: Student Data Submission

The user submits:

```json
{
  "name": "Rahul",
  "aptitude": 80,
  "communication": 75,
  "coding": 90
}
```

### Step 2: Score Evaluation

The API calculates:

```text
Total Score
Average Score
```

using the custom evaluation module.

### Step 3: Placement Prediction

The trained Decision Tree model predicts placement eligibility based on:

* Aptitude
* Communication
* Coding

scores.

### Step 4: AI Career Guidance

Gemini AI analyzes the student's performance and generates practical recommendations for improvement.

### Step 5: Data Storage

The student record is appended to:

```text
student_data.csv
```

for future reference.

## API Endpoint

### Create New Student Assessment

**POST**

```http
/new_student
```

### Request Body

```json
{
  "name": "Rahul",
  "aptitude": 80,
  "communication": 75,
  "coding": 90
}
```

### Response

```json
{
  "Student Name": "Rahul",
  "Aptitude": 80,
  "Communication": 75,
  "Coding": 90,
  "Placement_Status": "Eligible",
  "Mentor advice": "Focus on communication practice while maintaining strong coding skills..."
}
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/vennabharat/AI-Placement-Mentor-API.git

cd AI-Placement-Mentor-API
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install numpy pandas scikit-learn fastapi uvicorn pydantic python-dotenv google-genai
```

---

## Environment Setup

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

You can use `.env.example` as a reference.

---

## Running the API

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

to access the automatically generated Swagger UI.

---

## Machine Learning Model

Model Used:

```text
Decision Tree Classifier
```

Training Features:

* Aptitude
* Communication
* Coding

Target Variable:

```text
Placement_Status
```

Evaluation Metrics:

* Accuracy Score
* Precision
* Recall
* F1 Score

---

## Learning Objectives

This project was built to practice and demonstrate:

* REST API Development
* FastAPI
* Data Validation
* Pandas Data Processing
* Machine Learning Workflows
* Model Training and Prediction
* Environment Variable Security
* Gemini AI Integration
* End-to-End AI Application Development

---

## Future Improvements

* Replace CSV database with PostgreSQL
* Retrain model automatically when new data is added
* Add authentication and authorization
* Add student performance dashboard
* Deploy on Render or AWS
* Add multiple ML models for comparison
* Store mentor conversations
* Build a frontend using React

---

## Author

Bharat Venna

Aspiring AI Engineer focused on building practical Machine Learning and Generative AI applications.
