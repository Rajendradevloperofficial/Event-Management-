# Threat Monitoring & Alert Management Backend

## Project Overview
This project is a backend REST API system built using Django and Django REST Framework
for ingesting security events and automatically generating alerts based on severity.
It is developed as part of the Cyethack Solutions Django Developer Assignment.

The system simulates a simplified threat monitoring module that can integrate with
surveillance systems, SIEM tools, or AI-based threat detection platforms.

---

## Tech Stack
- Python
- Django
- Django REST Framework (DRF)
- JWT Authentication (SimpleJWT)
- SQLite (for local development)

---

## Features
- JWT based user authentication
- Role-based access control (Admin / Analyst)
- Event ingestion API
- Automatic alert generation for High & Critical severity events
- Alert listing with filtering by severity and status
- Admin-only alert status update
- Pagination and optimized database queries

---

## User Roles
- **Admin**
  - Can ingest events
  - Can view alerts
  - Can update alert status

- **Analyst**
  - Read-only access to alerts

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-github-repo-url>
cd cyethack_monitor
