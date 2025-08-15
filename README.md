# 🏦 Credit Approval System

A robust Django REST API system for managing customer credit approvals and loan processing with intelligent credit scoring algorithms.

## ✨ Features

- 🔐 **Customer Registration** - Secure customer onboarding
- 📊 **Credit Score Calculation** - Dynamic credit assessment based on payment history
- ✅ **Loan Eligibility Check** - Real-time approval decisions
- 💰 **Loan Management** - Complete loan lifecycle management
- 📈 **EMI Calculations** - Automated monthly installment calculations
- 🐳 **Docker Ready** - Containerized deployment with PostgreSQL

## 🚀 Quick Start

### Prerequisites

- Docker & Docker Compose
- Git

### Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd credit_approval
   ```

2. **Start the application**

   ```bash
   docker-compose up --build
   ```

3. **Access the API**
   - API Base URL: `http://localhost:8000`
   - Admin Panel: `http://localhost:8000/admin`

## 📋 API Endpoints

### 🏠 Home

```
GET /
```

Returns available API endpoints and system information.

### 👤 Customer Management

```
POST /register
```

Register a new customer in the system.

**Request Body:**

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

### 🔍 Loan Eligibility

```
POST /check-eligibility
```

Check if a customer is eligible for a loan.

**Request Body:**

```json
{
  "customer_id": 1,
  "loan_amount": 100000,
  "interest_rate": 10.5,
  "tenure": 12
}
```

**Response:**

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

### 💳 Loan Creation

```
POST /create-loan
```

Create a new loan for an eligible customer.

**Request Body:** Same as eligibility check

**Response:**

```json
{
  "loan_id": 1,
  "customer_id": 1,
  "loan_approved": true,
  "message": "Loan approved successfully",
  "monthly_installment": 8792.59
}
```

### 📄 Loan Details

```
GET /view-loan/<loan_id>
```

View details of a specific loan.

**Response:**

```json
{
  "loan_id": 1,
  "customer": {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "phone_number": "1234567890",
    "age": 30
  },
  "loan_amount": 100000,
  "interest_rate": 10.5,
  "monthly_installment": 8792.59,
  "tenure": 12
}
```

### 📊 Customer Loans

```
GET /view-loans/<customer_id>
```

View all loans for a specific customer.

## 🧮 Credit Scoring Algorithm

The system uses a sophisticated credit scoring algorithm based on:

- **Payment History** (35%): On-time EMI payments
- **Credit Utilization** (30%): Current debt vs approved limit
- **Loan History** (20%): Number and types of past loans
- **Account Age** (15%): Length of credit history

### Approval Rules

| Credit Score | Approval Criteria                          |
| ------------ | ------------------------------------------ |
| > 50         | ✅ Automatic approval at requested rate    |
| 30-50        | ⚠️ Approval with minimum 12% interest rate |
| 10-30        | ⚠️ Approval with minimum 16% interest rate |
| ≤ 10         | ❌ Loan rejected                           |

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Django API    │────│   PostgreSQL    │────│     Docker      │
│   (Port 8000)   │    │   (Port 5432)   │    │   Environment   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Tech Stack

- **Backend**: Django 5.2.5 + Django REST Framework
- **Database**: PostgreSQL 15
- **Containerization**: Docker & Docker Compose
- **Web Server**: Gunicorn (Production) / Django Dev Server (Development)

## 🛠️ Development

### Project Structure

```
credit_approval/
├── 📁 credit_approval/     # Main Django project
├── 📁 customers/           # Customer management app
├── 📁 loans/              # Loan management app
├── 📁 system/             # System utilities
├── 📄 docker-compose.yml  # Docker orchestration
├── 📄 dockerfile          # Container definition
├── 📄 requirements.txt    # Python dependencies
└── 📄 manage.py           # Django management
```

### Running Tests

```bash
docker-compose exec web python manage.py test
```

### Database Migrations

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### Create Superuser

```bash
docker-compose exec web python manage.py createsuperuser
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with:

```env
POSTGRES_DB=credit_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=root
DB_HOST=db
DB_PORT=5432
```

### Docker Services

- **web**: Django application server
- **db**: PostgreSQL database with health checks
- **volumes**: Persistent data storage

## 📊 Sample Data

To test the API, you can use these sample requests:

### Register a Customer

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

### Check Loan Eligibility

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

## 🚨 Troubleshooting

### Common Issues

**Database Connection Error**

```
Solution: Ensure PostgreSQL container is healthy
docker-compose logs db
```

**404 Not Found**

```
Solution: Check if you're using the correct endpoints
Visit http://localhost:8000 for available routes
```

**Permission Denied**

```
Solution: Make sure entrypoint script is executable
chmod +x entrypoint.sh
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django REST Framework for the robust API foundation
- PostgreSQL for reliable data persistence
- Docker for seamless containerization

---

<div align="center">
  <strong>Built with ❤️ using Django & Docker</strong>
</div>
