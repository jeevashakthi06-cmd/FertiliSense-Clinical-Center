# FertiliSense – AI-Powered Fertility Intelligence System

## Overview

FertiliSense is an AI-driven fertility management platform designed to support both patients and healthcare professionals by integrating intelligent report analysis, appointment management, and personalized fertility guidance into a single web application.

The platform leverages Optical Character Recognition (OCR), AI-assisted medical report analysis, automated data extraction, and secure role-based authentication to simplify fertility assessment while improving clinical efficiency and patient engagement.

## Problem Statement
Fertility assessment often involves manual interpretation of blood reports and ultrasound scans, making the process time-consuming and susceptible to human error. Patients also face challenges in managing appointments, tracking fertility-related health information, and receiving timely recommendations.

FertiliSense addresses these challenges by automating report processing, identifying potential abnormalities, providing personalized lifestyle recommendations, and facilitating seamless communication between patients and fertility specialists.

## Objectives
- Digitize fertility assessment and patient management.
- Automate extraction of medical parameters from laboratory reports.
- Detect fertility-related abnormalities using AI-assisted analysis.
- Provide personalized lifestyle recommendations based on patient health data.
- Simplify appointment scheduling and notifications.
- Improve communication between patients and healthcare professionals.

# Key Features

### User Authentication

- Secure Patient and Doctor Registration
- Role-Based Login
- JWT Authentication
- BCrypt Password Encryption
- Protected Routes and Authorization

### Patient Portal

- View Personal Health Dashboard
- Upload Blood Reports and Ultrasound Reports
- Book and Manage Appointments
- Track Fertility Health Parameters
- Receive Personalized Lifestyle Recommendations
- View AI-Based Report Analysis

### Doctor Portal
- Access Patient Medical Records
- Review Uploaded Reports
- Verify AI-Extracted Medical Values
- Manage Patient Appointments
- Monitor Fertility Indicators
- View Clinical Recommendations

### AI-Assisted Medical Report Analysis
The system automatically analyzes uploaded reports to identify fertility-related abnormalities.
#### Blood Report Analysis
- Anti-Müllerian Hormone (AMH)
- Follicle-Stimulating Hormone (FSH)
- Luteinizing Hormone (LH)
- Thyroid-Stimulating Hormone (TSH)
- Estradiol
- Progesterone
- Prolactin

#### Ultrasound Report Analysis

- Polycystic Ovary Syndrome (PCOS)
- Ovarian Cysts
- Endometriosis
- Fibroids
- Endometrial Thickness
- Antral Follicle Count

### OCR-Based Data Extraction

Supports

- PDF
- JPG
- JPEG
- PNG

Automatically extracts

- Hormone Levels
- Ultrasound Findings
- Medical Observations

The extracted values are automatically populated into the patient's profile for clinical review.

### Appointment Management

- Online Appointment Booking
- Appointment Scheduling
- Doctor Availability Management
- Date Validation
- Appointment History
- WhatsApp Appointment Notifications

### Personalized Lifestyle Recommendation Engine

Recommendations are generated using

- Age
- Body Mass Index (BMI)
- Hormonal Profile
- Medical History
- Lifestyle Factors
- Fertility Risk Indicators

# System Architecture

Patient / Doctor
        │
        ▼
 React.js Frontend
        │
 REST API Communication
        │
 Node.js + Express.js
        │
 ├── Authentication Service
 ├── OCR Processing
 ├── Medical Report Analysis
 ├── Recommendation Engine
 ├── Appointment Management
 └── WhatsApp Notification Service
        │
 Prisma ORM
        │
 PostgreSQL Database

# Technology Stack

## Frontend

- React.js
- Vite
- HTML5
- CSS3
- JavaScript
- Axios

## Backend

- Node.js
- Express.js

## Database

- PostgreSQL
- Prisma ORM

## Authentication

- JSON Web Token (JWT)
- BCrypt

## AI & OCR

- Tesseract OCR
- Rule-Based Medical Analysis
- Medical Parameter Extraction

## Notifications

- WhatsApp Business API

---

# Database Design

The system consists of the following primary entities:

- User
- Appointment
- MedicalReport
- ExtractedMedicalValues
- Recommendation
- Notification

# Medical Parameters Analysed

- Anti-Müllerian Hormone (AMH)
- Follicle-Stimulating Hormone (FSH)
- Luteinizing Hormone (LH)
- Thyroid-Stimulating Hormone (TSH)
- Estradiol
- Progesterone
- Prolactin
- Body Mass Index (BMI)
- Age
- Hormonal Markers

# Workflow

Patient Login
       │
       ▼
Upload Medical Report
       │
       ▼
OCR Extracts Medical Text
       │
       ▼
Medical Parameter Identification
       │
       ▼
AI-Based Report Analysis
       │
       ▼
Risk Assessment
       │
       ▼
Lifestyle Recommendation
       │
       ▼
Doctor Verification
       │
       ▼
Appointment Management

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/FertiliSense.git

cd FertiliSense
```

---

## Backend

```bash
cd backend

npm install

npx prisma generate

npx prisma db push

npm run dev
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev

# Project Structure

FertiliSense
│
├── frontend
│   ├── src
│   │   ├── api
│   │   ├── components
│   │   ├── context
│   │   ├── pages
│   │   ├── App.jsx
│   │   └── main.jsx
│
├── backend
│   ├── prisma
│   ├── src
│   ├── uploads
│   ├── logs
│   └── package.json
│
└── README.md

# Security Features

- JWT-Based Authentication
- Role-Based Authorization
- Password Hashing with BCrypt
- Secure REST APIs
- Input Validation
- Protected Application Routes

# Future Enhancements

- AI Conversational Assistant
- Wearable Device Integration
- Predictive Fertility Analytics
- IVF Success Prediction
- Electronic Health Record (EHR) Integration
- Cloud Deployment
- Mobile Application
- Multi-language Support

# Conclusion

FertiliSense provides an intelligent digital platform for fertility management by combining secure web technologies with AI-assisted medical report analysis. The application reduces manual effort in interpreting fertility reports, enhances communication between patients and healthcare providers, and supports informed clinical decision-making through automated data extraction and personalized recommendations.

# Contributors

**Project:** FertiliSense – AI-Powered Fertility Intelligence System

Developed as an academic healthcare technology project to demonstrate the application of Artificial Intelligence, OCR, secure web development, and intelligent healthcare automation in fertility management.

