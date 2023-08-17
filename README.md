# Expense Tracker

An Expense Tracker application that allows you to manage your expenses through CRUD operations and visualize data using charts.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
  - [CRUD Operations](#crud-operations)
  - [Data Visualization](#data-visualization)
- [Locally Installation](#installation)


## Introduction

Expense Tracker is a web application built with Django and designed to help you manage your expenses effectively. It provides a user-friendly interface to perform CRUD operations on your expenses and visualize your spending patterns through charts.

## Features

### CRUD Operations

Expense Tracker allows you to perform the following CRUD operations:

- Create: Add new expenses with details like date, category, amount, etc.
- Read: View and sort your expenses based on various parameters.
- Update: Modify details of existing expenses.
- Delete: Remove expenses you no longer need.

### Data Visualization

The application offers charts to visualize your expenses, helping you gain insights into your spending habits. Charts include pie charts, line charts representing expense categories, amounts spent over time, and more.

## Installation

To run the Expense Tracker locally, follow these steps:

1. Clone the repository:
   git clone https://github.com/Nandansingh007/Expense-Tracker.git
   
   cd mysite

2. Set up a virtual environment and activate it:
   
     python -m venv venv
   
    source venv/bin/activate  # On Windows: venv\Scripts\activate
   
3. Install project dependencies:
   
     pip install -r requirements.txt

4. Apply database migrations:
   
   python manage.py migrate

5. Run the development server:
   
   python manage.py runserver

