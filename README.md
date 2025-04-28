---

# Company Management API

A simple RESTful API built with **Flask**, **SQLAlchemy**, and **JWT Authentication** to manage companies and user accounts.

---

## 📋 Features

- **User Authentication** (Register / Login / Refresh Token)
- **Protected Routes** with JWT (`access` and `refresh` tokens)
- **Company Management**:
  - View all companies
  - View a single company
  - Add a company (authenticated)
  - Update a company (authenticated)
  - Delete a company (authenticated)
- **Error Handling** for invalid requests and authorization failures

---

## 🛠️ Tech Stack

- **Backend**: Flask, Flask-JWT-Extended, SQLAlchemy
- **Database**: SQLite (can be switched easily to PostgreSQL, MySQL, etc.)
- **Authentication**: JSON Web Tokens (JWT)

---

## 📂 Project Structure

```
app/
 ├── __init__.py          # Initialize app, database, JWT
 ├── models/              # SQLAlchemy models (User, Company)
 ├── services/
 │    └── company_services.py  # Business logic for users and companies
 ├── routes/
 │    ├── auth.py          # Authentication routes (register, login, refresh, profile)
 │    └── company.py       # Company management routes
 └── config.py             # App configuration (secret key, database URI)
```

---

## 🚦 API Endpoints

### 🧑‍💻 Authentication

| Method | Endpoint | Description |
|:---|:---|:---|
| `POST` | `/register` | Register a new user |
| `POST` | `/login` | Login and get access and refresh tokens |
| `POST` | `/refresh` | Get a new access token using a refresh token |
| `GET`  | `/profile` | Get the current user's profile (Protected) |

---

### Company Management

| Method | Endpoint | Description |
|:---|:---|:---|
| `GET` | `/companies` | Get all companies |
| `GET` | `/companies/<id>` | Get a specific company by ID |
| `POST` | `/add` | Add a new company (Protected) |
| `PUT` | `/update/<id>` | Update a company (Protected) |
| `DELETE` | `/delete/<id>` | Delete a company (Protected) |

---

## Authentication Flow

- After **login**, you receive:
  - An **access token** (short-lived) — used to access protected endpoints.
  - A **refresh token** (longer-lived) — used to get a new access token.
- Attach the access token in the `Authorization` header:

```
Authorization: Bearer <access_token>
```

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/amr-hussain/CompanyAPI.git
cd CompanyAPI
```

2. **Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate    # For Linux/Mac
.venv\Scripts\activate       # For Windows
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Set environment variables**

```bash
export FLASK_APP=app    # For Linux/Mac
set FLASK_APP=app       # For Windows
```

5. **Set up the database**

- Initialize the migration directory:

```bash
flask db init
```

- Generate the initial migration:

```bash
flask db migrate -m "Initial migration."
```

- Apply the migration (create tables):

```bash
flask db upgrade
```

6. **Run the application**

```bash
flask run
```


## License

This project is open-source and available under the [MIT License](LICENSE).


