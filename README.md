# Fullstack Project

This project is a web application that dynamically renders test cases from a PostgreSQL database, allowing for real-time updates.

## Project Structure

fullstack-project/
├── backend/
│   ├── app.py
│   ├── .env
│   ├── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.css
│   │   ├── App.js
│   │   ├── index.js
│   ├── package.json
├── README.md
├── .gitignore

## Prerequisites

  - Node.js and npm installed
  - Python 3.x installed
  - PostgreSQL database set up

## Installation

### Backend

1. Navigate to the `backend` directory:

	cd backend

2.Create and activate a virtual environment:
	
	python -m venv venv
	source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required Python packages:

	pip install -r requirements.txt

4. Create a .env file and add your database credentials:
	
	DB_NAME=your_database_name
	DB_USER=your_database_user
	DB_PASSWORD=your_database_password
	DB_HOST=your_database_host

5. Run the Flask app:
	
	flask run


## Frontend
	
1. Navigate to the `frontend` directory:

	cd frontend

2. Install the required npm packages:
	
	npm install

3. Run the React app:
 	
 	npm start


### Running the Application
	
1. Start the backend server as described above.
2. Start the frontend development server.
3. Open your browser and navigate to `http://localhost:3000` to see the application.

## Initial Database Setup
	
	CREATE TABLE testcases (
    id SERIAL PRIMARY KEY,
    test_case_name VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50),
    estimate_time VARCHAR(50),
    module VARCHAR(255),
    priority VARCHAR(50),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

	INSERT INTO testcases (
    test_case_name,
    description,
    status,
    estimate_time,
    module,
    priority,
    last_updated
) VALUES
    ('Login Functionality Test', 'Test the login functionality with valid credentials.', 'true', '5', 'Authentication', 'High', '2024-07-25 14:00:00'),
    ('Signup Process Test', 'Verify the user registration process with valid data.', 'true', '5', 'User Management', 'Medium', '2024-07-24 09:00:00'),
    ('Password Reset Test', 'Ensure password reset process works with email verification.', 'false', '10', 'Authentication', 'Low', '2024-07-25 10:00:00'),
    ('Profile Update Test', 'Check if users can update their profile information.', 'true', '5', 'User Management', 'Medium', '2024-07-23 15:00:00');


