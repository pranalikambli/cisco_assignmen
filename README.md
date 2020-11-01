# cisco_assignment

# Installation

Running the Project Locally First, clone the repository to your local machine.
```bash
git clone https://github.com/pranalikambli/cisco_assignmen.git
```

For Python & Django Installation check our blogs.

For Windows : https://techpluslifestyle.com/technology/how-to-install-django-3-on-windows

For Ubuntu :  https://techpluslifestyle.com/technology/how-to-install-django-3-on-ubuntu/

Database : Sqlite (Django's Default DB)

Install the requirements.
```bash
pip install -r requirements.txt
```

Apply the migrations Exe1->Q1-2->router_App.
```bash
python manage.py migrate 
```
```bash
python manage.py makemigrations api
```
```bash
python manage.py migrate
```

Apply the migrations Exe3->
```bash
python manage.py migrate 
```
```bash
python manage.py makemigrations router
```
```bash
python manage.py migrate
# Running the Project Locally

```bash
python manage.py runserver 
```
The project will be available at 127.0.0.1:8000
