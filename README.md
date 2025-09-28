# GrowAutomation – Payment Processes and Automated Testing

This project demonstrates the use of **Flask** for integration with the **Meshulam API**, along with automated testing using **Pytest** and **Selenium**.

---

## Installation and Run Instructions

### Prerequisites
- Python 3.10+
- Google Chrome installed
- ChromeDriver matching your browser version

### Installing Dependencies
```bash
pip install -r requirements.txt
```

Running web Automation script
```bash
cd webAutomation
python main.py
````

Running the Flask API
```bash
cd PostmanTest
python PostmanGrow.py
```
By default, the app will be available at:
http://127.0.0.1:5000

Running Automated Tests
```bash
pytest -v
```
## Configuration and Environment Variables
Environment variables are loaded from the .env file.

Test Mode Flag
CORRENT_CASE=yes → Run only with valid parameters (tests expected to pass).

CORRENT_CASE=no → Intentionally send invalid parameters (tests expected to fail and return error messages).

## Test Scenarios and Coverage
Three main scenarios were implemented:

Valid request – Returns status=200 and a valid payment form URL.

Missing required field – For example, missing userId; returns status=0 and an appropriate error message.

Invalid value – For example, sum=0; returns status=0 and an appropriate error message.

This ensures that all critical features are covered:

Both success and failure flows

Validation of returned API values (status code, error message, and URL)

## Future Improvements: Docker
Currently, to run the project you need to:

Set up Python

Install dependencies from requirements.txt

Ensure Chrome and ChromeDriver versions match

Provide a .env file

In a CI/CD pipeline or when other developers set up the project, it’s easy to miss one of these steps → leading to the classic “works on my machine but not on yours” problem.

With Docker, you can create a single unified container that already includes Python and all dependencies → ensuring a consistent environment with no surprises.

yaml
Copy code



