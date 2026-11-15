# Automated Website Tester

## Description
This project is a website testing automation developed in Python using Selenium WebDriver. It automatically opens a website in Google Chrome and checks whether its main features work correctly.

## Features
The automation performs 9 tests:

- Checks whether the website loads with the correct title.
- Tests navigation through the About link.
- Tests navigation back to the homepage.
- Checks form validation when the name is missing.
- Checks form validation when the terms are not accepted.
- Checks form validation when the message is empty.
- Checks form validation with an invalid email address.
- Verifies that a correctly completed form can be submitted.
- Checks that an empty form cannot be submitted.

## Technologies Used
- Python
- Selenium WebDriver
- Google Chrome
- HTML
- CSS
- JavaScript

## How It Works
Selenium automatically opens Google Chrome, accesses the local website, interacts with its links and form fields, and checks the results using Python `assert` statements.

The browser is automatically closed after each test.

## Requirements
- Python 3
- Google Chrome
- Selenium

Install Selenium using:

```bash
pip install selenium