\# E-Commerce Backend API



A fully functional E-Commerce Backend API built with Django and DRF.



\## Tech Stack

\- Python

\- Django

\- Django REST Framework

\- JWT Authentication

\- SQLite



\## API Endpoints



\### Authentication

\- POST /api/register/ → Register

\- POST /api/token/ → Get token

\- POST /api/token/refresh/ → Refresh token



\### Products

\- GET    /api/products/ → List all

\- POST   /api/products/ → Create

\- GET    /api/products/{id}/ → Get one

\- PUT    /api/products/{id}/ → Update

\- PATCH  /api/products/{id}/ → Partial update

\- DELETE /api/products/{id}/ → Delete



\### Categories

\- GET    /api/categories/ → List all

\- POST   /api/categories/ → Create

\- GET    /api/categories/{id}/ → Get one

\- PUT    /api/categories/{id}/ → Update

\- DELETE /api/categories/{id}/ → Delete



\## Installation



1\. Clone repository

git clone https://github.com/SunilMalladad89/ecommerce-django-api.git



2\. Create virtual environment

python -m venv venv

venv\\Scripts\\activate



3\. Install dependencies

pip install -r requirements.txt



4\. Create .env file

SECRET\_KEY=your\_secret\_key

DEBUG=True



5\. Run migrations

python manage.py migrate



6\. Create superuser

python manage.py createsuperuser



7\. Run server

python manage.py runserver

