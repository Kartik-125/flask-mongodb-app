# 🚀 Flask MongoDB Application

A simple and scalable **Flask REST API** integrated with **MongoDB**, containerized using **Docker**, and ready for **Kubernetes deployment**.

This project demonstrates backend development best practices including environment-based configuration, containerization, and clean project structure.

---

## 📌 Features

- Flask-based REST API
- MongoDB integration using PyMongo
- Environment variable configuration
- Docker support
- Kubernetes deployment manifests
- Clean and production-ready structure

---

## 📂 Project Structure

```text
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
