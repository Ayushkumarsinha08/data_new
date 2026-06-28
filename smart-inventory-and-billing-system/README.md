# 🏪 Smart Inventory & Billing System with Sales Analytics

A cloud-hosted Inventory Management and Billing System built using **Python, PostgreSQL, Streamlit, and SQL**. The application enables businesses to efficiently manage customers, products, sales transactions, inventory, billing, and analytics through an interactive dashboard.

---

## 🔗 Live Demo

**Application:** https://sahil15573-smart-inventory-and-billing-system-app-iphxop.streamlit.app/

**GitHub Repository:** https://github.com/sahil15573/smart-inventory-and-billing-system

---

# 📌 Project Overview

The Smart Inventory & Billing System is designed to streamline retail inventory operations and sales management. It provides a centralized platform for managing customer records, product inventory, sales transactions, billing generation, and business analytics.

The project demonstrates practical implementation of:

* Relational Database Design
* PostgreSQL Database Management
* SQL Query Optimization
* Data Analytics & Reporting
* Inventory Tracking
* Business Intelligence Dashboards
* Cloud Deployment

The system is deployed using **Streamlit Cloud** with **Neon PostgreSQL** for persistent cloud-based database storage.

---

# 🚀 Features

## 👥 Customer Management

* Add new customers
* View customer records
* Update customer information
* Delete customer records
* Maintain customer purchase history

---

## 📦 Product Management

* Add products to inventory
* Update product details
* Modify stock quantity
* Remove products
* View complete inventory catalog

---

## 💰 Sales Management

* Create new sales transactions
* Associate sales with customers
* Add multiple products per sale
* Generate billing information
* Automatically calculate total transaction value

---

## 📊 Analytics & Reporting

### Sales Summary

* Total Sales
* Total Revenue
* Daily Revenue Trend

### Sales By Date Range

* Custom date filtering
* Revenue tracking within selected periods

### Top Selling Products

* Identify best-performing products
* Product demand analysis

### Low Stock Alerts

* Monitor inventory levels
* Prevent stock shortages

### Customer Purchase History

* Track customer transactions
* Analyze customer spending patterns

---

# 🛠️ Tech Stack

## Frontend

* Streamlit

## Backend

* Python

## Database

* PostgreSQL
* Neon PostgreSQL (Cloud Database)

## Libraries

* Streamlit
* Psycopg2
* Pandas
* NumPy
* Faker
* Python-dotenv

## Version Control

* Git
* GitHub

## Deployment

* Streamlit Community Cloud
* Neon Database

---

# 🏗️ System Architecture

```text
User Interface (Streamlit)
          │
          ▼
Business Logic (Python)
          │
          ▼
SQL Queries (Psycopg2)
          │
          ▼
PostgreSQL Database (Neon Cloud)
```

---

# 🗄️ Database Schema

The project follows a normalized relational database design.

## Customers Table

| Column  | Type               |
| ------- | ------------------ |
| id      | SERIAL PRIMARY KEY |
| name    | VARCHAR(100)       |
| contact | VARCHAR(20)        |

---

## Products Table

| Column      | Type               |
| ----------- | ------------------ |
| id          | SERIAL PRIMARY KEY |
| name        | VARCHAR(100)       |
| description | TEXT               |
| price       | DECIMAL(10,2)      |
| quantity    | INTEGER            |

---

## Sales Table

| Column       | Type               |
| ------------ | ------------------ |
| id           | SERIAL PRIMARY KEY |
| customer_id  | INTEGER            |
| date         | DATE               |
| total_amount | DECIMAL(10,2)      |

Foreign Key:

```sql
customer_id → customers(id)
```

---

## Sale Items Table

| Column     | Type               |
| ---------- | ------------------ |
| id         | SERIAL PRIMARY KEY |
| sale_id    | INTEGER            |
| product_id | INTEGER            |
| quantity   | INTEGER            |
| price      | DECIMAL(10,2)      |

Foreign Keys:

```sql
sale_id → sales(id)

product_id → products(id)
```

---

# 📈 Dataset Statistics

The deployed application contains realistic business data generated using Python and Faker.

### Current Dataset

| Metric             | Count |
| ------------------ | ----- |
| Customers          | 60+   |
| Products           | 80+   |
| Sales Transactions | 100+  |
| Sale Items         | 200+  |

This realistic dataset enables meaningful analytics and dashboard insights.

---

# 📊 Key Analytics Implemented

## Revenue Analysis

Tracks:

* Total Revenue
* Revenue Trends
* Sales Growth

---

## Product Performance Analysis

Tracks:

* Top Selling Products
* Product Demand
* Inventory Consumption

---

## Inventory Monitoring

Tracks:

* Available Stock
* Low Stock Products
* Inventory Health

---

## Customer Analytics

Tracks:

* Purchase History
* Customer Spending
* Customer Activity

---

# 💡 Business Value

The system helps businesses:

* Maintain organized inventory records
* Reduce manual billing errors
* Monitor stock availability
* Track sales performance
* Analyze customer purchasing behavior
* Generate actionable business insights

---

# ⚙️ Installation & Setup

## Clone Repository

```bash
git clone https://github.com/sahil15573/smart-inventory-and-billing-system.git

cd smart-inventory-and-billing-system
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file:

```env
DB_HOST=your_host
DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password
DB_PORT=5432
```

---

## Run Application

```bash
streamlit run app.py
```

---

# ☁️ Cloud Deployment

## Frontend Deployment

* Streamlit Community Cloud

## Database Deployment

* Neon PostgreSQL

The application uses secure environment variables and cloud-hosted PostgreSQL storage for persistent data management.

---

# 🔮 Future Enhancements

* Authentication & Role-Based Access Control
* Invoice PDF Generation
* Product Category Management
* Supplier Management
* Purchase Orders
* Advanced Power BI Dashboards
* Forecasting & Demand Prediction
* Sales Trend Prediction using Machine Learning
* Automated Email Reports

---

# 🎯 Learning Outcomes

Through this project, the following concepts were applied:

* PostgreSQL Database Design
* SQL Queries & Relationships
* CRUD Operations
* Foreign Key Constraints
* Data Analytics & Reporting
* Streamlit Dashboard Development
* Cloud Database Integration
* Application Deployment
* Git & GitHub Version Control

---

# 👨‍💻 Author

**Sahil Kumar**

B.Tech Undergraduate | Data Analytics | Data Engineering | AI/ML | GenAI

### Connect With Me

* LinkedIn: https://www.linkedin.com/in/sahil-kumar-a945191a6/
* GitHub: https://github.com/sahil15573

---

## ⭐ If you found this project useful, please consider giving it a star on GitHub.
