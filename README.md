
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
- 🔐 Secure Customer Registration  
- 📊 Dynamic Credit Score Calculation  
- ✅ Instant Loan Eligibility Checks  
- 💰 Loan Lifecycle Management  
- 📈 Automated EMI Calculations  
- 🐳 Dockerized Deployment with PostgreSQL  

---

## 🚀 **Quick Start**

### **Prerequisites**
- [Docker](https://docs.docker.com/get-docker/) & Docker Compose  
- [Git](https://git-scm.com/)  

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
````

---

## 📋 **API Endpoints & Screenshots**

---

### 👤 **Customer Registration**

```http
POST /register
```

**Sample Request**

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

| Screenshot                                         |
| -------------------------------------------------- |
| ![Register Customer](Test/Register%20Customer.png) |

---

### 🔍 **Check Loan Eligibility**

```http
POST /check-eligibility
```

**Sample Request**

```json
{
  "customer_id": 1,
  "loan_amount": 100000,
  "interest_rate": 10.5,
  "tenure": 12
}
```

**Sample Response**

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

| Screenshot                                         |
| -------------------------------------------------- |
| ![Check Eligibility](Test/Check%20Eligibility.png) |

---

### 💳 **Create Loan**

```http
POST /create-loan
```

| Screenshot                             |
| -------------------------------------- |
| ![Create Loan](Test/Create%20Loan.png) |

---

### 📄 **View Loan by Loan ID**

```http
GET /view-loan/<loan_id>
```

| Screenshot                                                           |
| -------------------------------------------------------------------- |
| ![View Loan using loan id](Test/View%20Loan%20using%20loan%20id.png) |

---

### 📊 **View All Loans by Customer**

```http
GET /view-loans/<customer_id>
```

| Screenshot                                                       |
| ---------------------------------------------------------------- |
| ![View Loans By Customer](Test/View%20Loans%20By%20Customer.png) |

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

## 📂 **Project Structure**

```
credit_approval/
├── customers/          
├── loans/              
├── system/             
├── Test/               # Screenshots for API tests
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── manage.py
```

---

## 📊 **Sample Requests**

**Register a Customer**

```bash
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Alice","last_name":"Johnson","age":28,"phone_number":"9876543210","monthly_income":75000,"approved_limit":750000}'
```

**Check Loan Eligibility**

```bash
curl -X POST http://localhost:8000/check-eligibility \
  -H "Content-Type: application/json" \
  -d '{"customer_id":1,"loan_amount":200000,"interest_rate":12.0,"tenure":24}'
```

---

## 🖼 **Test Screenshots Overview**

<p align="center">
  <img src="Test/Register%20Customer.png" width="220" alt="Register Customer" />
  <img src="Test/Check%20Eligibility.png" width="220" alt="Check Eligibility" />
  <img src="Test/Create%20Loan.png" width="220" alt="Create Loan" />
  <img src="Test/View%20Loan%20using%20loan%20id.png" width="220" alt="View Loan by ID" />
  <img src="Test/View%20Loans%20By%20Customer.png" width="220" alt="View Loans by Customer" />
</p>

---

## 🚨 **Troubleshooting**

| Issue                     | Possible Solution                                            |
| ------------------------- | ------------------------------------------------------------ |
| Database connection error | Run `docker-compose logs db` and ensure container is healthy |
| 404 Not Found             | Verify endpoint paths and check `http://localhost:8000` root |
| Permission denied         | Make script executable: `chmod +x entrypoint.sh`             |

---

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 **License**

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) file for details.

---

<p align="center">
  <strong>💡 "Financial decisions made smarter, faster, safer."</strong>
</p>
```

---
