##  Project Summary – INVENTORY_VENDOR

###  Overview

**INVENTORY_VENDOR** is a backend-focused Django project developed to design and implement **RESTful APIs for an Inventory Vendor Management System**.  
The project was built by analyzing provided UI screens and translating them into a structured **database schema** and **function-based REST APIs**.

The primary objective of this project is **API development**, not frontend implementation.

---

###  Project Objective

The main goals of this project are:

- Convert given UI requirements into a proper **database design**
- Implement **REST APIs** for inventory and vendor management
- Handle **Many-to-Many relationships** between items and vendors
- Use **MySQL** as the database with Django
- Build APIs using **function-based views (`@api_view`)**
- Perform database operations using **raw SQL queries**
- Provide clean, structured JSON responses suitable for frontend consumption

---

###  UI Reference (Given Requirement)

The following UI screens were provided only as **requirements** to design the database and APIs:

#### Add New Item Screen
![Add New Item](./Screenshot%202026-02-05%20160932.png)

#### Add New Vendor Screen
![Add New Vendor](./Screenshot%202026-02-05%20160947.png)

>  Note: No frontend code is implemented in this project.  
> These images are used strictly for backend planning and API design.

---

###  Database Design

Based on the UI requirements, the following tables were designed in **MySQL**:

#### 1️ `inventory_vendor`
Stores vendor-related information.
- abbreviation
- firm_name
- address
- village
- city
- pincode
- email
- phone_no
- fax_no

#### 2️ `inventory_item`
Stores inventory item details.
- ohe_code
- rin_no
- description
- drawing_no
- drawing_image

#### 3️ `inventory_item_vendors`
A junction table used to manage the **Many-to-Many relationship** between items and vendors.
- item_id (FK)
- vendor_id (FK)

---

###  Relationship Logic

- One **Item** can be supplied by **multiple Vendors**
- One **Vendor** can supply **multiple Items**
- Implemented using a **Many-to-Many relationship**
- Managed internally by Django and exposed through APIs

---

###  Technology Stack

- **Backend Framework**: Django
- **API Development**: Django REST Framework
- **API Style**: Function-based APIs (`@api_view`)
- **Database**: MySQL (MySQL Workbench)
- **Database Access**: Raw SQL (`connection.cursor`)
- **Version Control**: Git & GitHub

---

###  API Design Approach

- One API per table
- No class-based views
- No serializers
- Raw SQL queries for full control
- JSON-based responses
- Support for:
  - GET (list & detail)
  - POST (create)
  - DELETE (remove)
- Pagination support for list APIs

---

###  API Endpoints

#### Vendor APIs
GET /api/vendors/
GET /api/vendors/<vendor_id>/
DELETE /api/vendors/delete/<vendor_id>/
#### Item APIs
GET /api/items/
GET /api/items/<item_id>/
DELETE /api/items/delete/<item_id>/

#### Item–Vendor Mapping APIs
GET /api/item-vendors/
DELETE /api/item-vendors/delete/<mapping_id>/

---

###  Security & Best Practices

- MySQL credentials managed using **environment variables**
- `.env` file excluded using `.gitignore`
- No database files or secrets pushed to GitHub
- Clean separation of code and configuration

---

###  How to Run the Project

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver




