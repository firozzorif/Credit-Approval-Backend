# 🏦 **Credit Approval System**

> **A Smart Django REST API for Seamless Credit Approvals & Loan Management**
> Built with ❤️ using Django, PostgreSQL & Docker.

<p align="center">
  <img src="https://img.shields.io/badge/Django-5.2.5-092E20?style=for-the-badge&logo=django" />
  <img src="https://img.shields.io/badge/PostgreSQL-15-316192?style=for-the-badge&logo=postgresql" />
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

---

## ✨ **Key Features**

* 🔐 **Secure Customer Registration** — Encrypted data storage & safe onboarding
* 📊 **Dynamic Credit Score Calculation** — Based on payment history & credit utilization
* ✅ **Instant Loan Eligibility Checks** — Real-time approval logic
* 💰 **Loan Lifecycle Management** — From approval to closure
* 📈 **Automated EMI Calculations** — Accurate monthly installment breakdown
* 🐳 **Dockerized Deployment** — With PostgreSQL integration

---

## 🚀 **Quick Start**

### **Prerequisites**

* [Docker](https://docs.docker.com/get-docker/) & Docker Compose
* [Git](https://git-scm.com/)

### **Installation**

```bash
# 1️⃣ Clone the repository
git clone <your-repo-url>
cd credit_approval

# 2️⃣ Start the application
docker-compose up --build

# 3️⃣ Access the API
# API Base URL: http://localhost:8000
# Admin Panel: http://localhost:8000/admin
```

---

## 📋 **API Endpoints**

### 🏠 **Home**

```http
GET /
```

Returns available endpoints & system info.

---

### 👤 **Customer Management**

```http
POST /register
```

**Request:**

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "age": 30,
  "phone_number": "1234567890",
  "monthly_income": 50000,
  "approved_limit": 500000
}
```

---

### 🔍 **Loan Eligibility**

```http
POST /check-eligibility
```

**Response Example:**

```json
{
  "customer_id": 1,
  "approval": true,
  "interest_rate": 10.5,
  "corrected_interest_rate": 10.5,
  "tenure": 12,
  "monthly_installment": 8792.59
}
```

---

### 💳 **Loan Creation**

```http
POST /create-loan
```

Creates a new loan for eligible customers.

---

### 📄 **Loan Details**

```http
GET /view-loan/<loan_id>
```

---

### 📊 **Customer Loans**

```http
GET /view-loans/<customer_id>
```

---

## 🧮 **Credit Scoring Algorithm**

| **Credit Score** | **Decision**                    |
| ---------------- | ------------------------------- |
| > 50             | ✅ Approved at requested rate    |
| 30–50            | ⚠️ Approved with ≥ 12% interest |
| 10–30            | ⚠️ Approved with ≥ 16% interest |
| ≤ 10             | ❌ Rejected                      |

**Factors:**

* Payment History (35%)
* Credit Utilization (30%)
* Loan History (20%)
* Account Age (15%)

---

## 🏗 **Architecture**

```
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│   Django API  │ ─── │  PostgreSQL   │ ─── │   Docker Env  │
│   (Port 8000) │     │  (Port 5432)  │     │               │
└───────────────┘     └───────────────┘     └───────────────┘
```

---

## 🛠 **Development**

### **Project Structure**

```
credit_approval/
├── credit_approval/      # Django project
├── customers/            # Customer app
├── loans/                # Loan app
├── system/               # Utilities
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── manage.py
```

### **Useful Commands**

```bash
# Run tests
docker-compose exec web python manage.py test

# Make migrations
docker-compose exec web python manage.py makemigrations

# Apply migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser
```

---

## 📊 **Sample Requests**

**Register a Customer**

```bash
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Alice",
    "last_name": "Johnson",
    "age": 28,
    "phone_number": "9876543210",
    "monthly_income": 75000,
    "approved_limit": 750000
  }'
```

**Check Loan Eligibility**

```bash
curl -X POST http://localhost:8000/check-eligibility \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "loan_amount": 200000,
    "interest_rate": 12.0,
    "tenure": 24
  }'
```

---

## 🚨 **Troubleshooting**

* **Database Connection Error** → `docker-compose logs db`
* **404 Not Found** → Visit `http://localhost:8000` to check routes
* **Permission Denied** → `chmod +x entrypoint.sh`

---

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to branch
5. Open a Pull Request

---

## 📝 **License**

This project is under the **MIT License** — see [LICENSE](LICENSE).

---

<p align="center">
  💡 <i>"Financial decisions made smarter, faster, safer."</i> 💡
</p>

---
