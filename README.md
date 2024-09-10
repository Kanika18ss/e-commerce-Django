# E-commerce Web Application

A comprehensive e-commerce web application built with Django and SQL. This project includes complete functionalities for managing user accounts, placing orders, integrating a payment gateway, and handling shipping and returns.

## Demo Video 
https://www.loom.com/share/71f1274d40714679a92b210901840092?sid=75d22ba3-f742-4db9-81e7-92364ad525d2

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [ER Diagram](#ERDiagram)
- [Technologies](#technologies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

This e-commerce web application provides a robust platform for users to browse products, manage their accounts, and make purchases. The application is designed to handle various functionalities, including user registration, secure authentication, seamless order placement, payment processing, and shipping management.

## Features

- **User Management**: Secure user registration, authentication, authorization, and profile management.
- **Order Management**: Seamless order placement with automatic updates to the database.
- **Payment Integration**: Razorpay payment gateway integration for secure transactions.
- **Shipping Management**: Automated shipping cost calculations, delivery date estimates, and tracking.
- **Return and Cancellation**: Handling of return requests and order cancellations.
- **Database Management**: Complete database schema designed from scratch to support all functionalities.

## ER Diagram
![er](https://github.com/user-attachments/assets/430adaac-4e13-45af-a34c-d7cf8ac403d1)



## Technologies

- **Django**: Web framework used for building the application.
- **SQL**: Database management system for storing application data.
- **Razorpay**: Payment gateway integration for processing transactions.
- **Bootstrap**: Frontend framework used for styling the application (if applicable).

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

7. **Access the Application**

   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Configuration

Before running the application, ensure that you have configured the necessary settings:

1. **Database Configuration**

   Update the `DATABASES` setting in `settings.py` with your SQL database credentials.

2. **Razorpay Integration**

   Configure Razorpay API keys in `settings.py`:

   ```python
   RAZORPAY_API_KEY = 'your_api_key'
   RAZORPAY_API_SECRET = 'your_api_secret'
   ```

3. **Static Files**

   Ensure that static files are collected and served correctly:

   ```bash
   python manage.py collectstatic
   ```

## Usage

1. **Access the Admin Panel**

   Navigate to `http://127.0.0.1:8000/admin/` and log in using the superuser credentials to manage users, products, orders, and other data.

2. **Browse Products**

   Visit `http://127.0.0.1:8000/products/` to browse the available products.

3. **Place an Order**

   Add items to your cart and proceed to checkout to place an order.

4. **Make a Payment**

   Use the Razorpay payment gateway to complete your transactions.

5. **Manage Orders**

   View and manage orders, including cancellations and returns.

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.


---

Feel free to modify the content to better suit your specific needs and project details.
