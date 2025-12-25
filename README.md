🚀 Flask MongoDB Application
A simple Flask REST API connected to MongoDB, containerized with Docker and ready for Kubernetes deployment.
This project demonstrates:
Flask backend API
MongoDB integration
Environment-based configuration
Docker & Kubernetes setup
Clean GitHub project structure

📌 Features
Flask REST API
MongoDB CRUD operations
Uses environment variables for security
Dockerized application
Kubernetes deployment manifests included

📂 Project Structure
flask-mongodb-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
│
├── flask-deployment.yaml
├── flask-service.yaml
├── flask-hpa.yaml
│
├── mongo-statefulset.yaml
├── mongo-service.yaml
├── mongo-secret.yaml
│
└── README.md

⚙️ Prerequisites
Make sure you have the following installed:
Python 3.10+
Git
MongoDB (local or cloud)
Docker (optional)
Kubernetes (optional)

🐍 Create & Activate Virtual Environment (venv)
▶️ Windows (PowerShell)
python -m venv venv
venv\Scripts\activate
▶️ macOS / Linux
python3 -m venv venv
source venv/bin/activate

📦 Install Dependencies
pip install -r requirements.txt

🔐 Environment Variables
Create a .env file (DO NOT commit this file):
MONGODB_URI=mongodb://localhost:27017/
Or export it directly:
**Windows**
setx MONGODB_URI "mongodb://localhost:27017/"
**macOS / Linux**
export MONGODB_URI="mongodb://localhost:27017/"

▶️ Run the Application
python app.py
App will start at:
http://localhost:5000

📡 API Endpoints
🔹 GET /
Returns a welcome message with current server time.
🔹 GET /data
Fetch all stored records from MongoDB.
🔹 POST /data
Insert data into MongoDB.

🐳 Run with Docker (Optional)
**Build image**
docker build -t flask-mongodb-app .
**Run container**
docker run -p 5000:5000 \
-e MONGODB_URI="mongodb://host.docker.internal:27017/" \
flask-mongodb-app

☸️ Kubernetes Deployment 

Apply MongoDB resources:
kubectl apply -f mongo-secret.yaml
kubectl apply -f mongo-service.yaml
kubectl apply -f mongo-statefulset.yaml

Apply Flask resources:
kubectl apply -f flask-deployment.yaml
kubectl apply -f flask-service.yaml
kubectl apply -f flask-hpa.yaml

