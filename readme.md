# Nudge TV Icon Generation Django Project with Bitly Shortener

The website takes target URL inputs and outputs UTM codes, shortened links and customized icons.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
Python 3.6.3
Django 2.2.4
```

### Installing

* **Including all applications for Django models**

Go to NudgeTVIconGen/

```
python manage.py makemigrations URLShortener
python manage.py sqlmigrate URLShortener 0001
python manage.py migrate
```

* **Creating admin user**

```
python manage.py createsuperuser
```

* **Filling in Bitly account information**

Go to NudgeTVIconGen/refresh_db.py, fill in

```
API_USER =
API_KEY =
```

## Running the tests

* **Start the development server**

Go to NudgeTVIconGen/

```
python manage.py runserver
```

In browser, type http://localhost:8000/admin/ and log in with admin account


* **Refresh the database**

Go to NudgeTVIconGen/

```
python refresh_db.py
```

## Authors

* **Leying Hu**

If you meet any problems, please contact hu.leying@columbia.edu


## Acknowledgments

* Nudge TV: https://www.nudgetv.com/
