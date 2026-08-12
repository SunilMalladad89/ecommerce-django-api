\# E-Commerce Backend API



A fully functional E-Commerce Backend API built with Django and Django REST Framework.



\## Live Demo

\- \*\*API Root:\*\* https://ecommerce-django-api.onrender.com/api/

\- \*\*Products:\*\* https://ecommerce-django-api.onrender.com/api/products/

\- \*\*Categories:\*\* https://ecommerce-django-api.onrender.com/api/categories/



\## Tech Stack

\- Python

\- Django

\- Django REST Framework

\- JWT Authentication (SimpleJWT)

\- PostgreSQL (Production)

\- SQLite (Development)

\- WhiteNoise (Static Files)

\- Gunicorn (Production Server)

\- Render (Deployment)



\## Features

\- Product CRUD operations

\- Category management

\- User Registration and Login

\- JWT Authentication

\- Image Upload

\- Admin Panel

\- REST API with DRF

\- ViewSets and Routers



\## API Endpoints



\### Authentication

| Method | URL | Description |

|--------|-----|-------------|

| POST | /api/register/ | Register new user |

| POST | /api/token/ | Get JWT token |

| POST | /api/token/refresh/ | Refresh token |



\### Products

| Method | URL | Description |

|--------|-----|-------------|

| GET | /api/products/ | List all products |

| POST | /api/products/ | Create product |

| GET | /api/products/{id}/ | Get one product |

| PUT | /api/products/{id}/ | Update product |

| PATCH | /api/products/{id}/ | Partial update |

| DELETE | /api/products/{id}/ | Delete product |



\### Categories

| Method | URL | Description |

|--------|-----|-------------|

| GET | /api/categories/ | List all categories |

| POST | /api/categories/ | Create category |

| GET | /api/categories/{id}/ | Get one category |

| PUT | /api/categories/{id}/ | Update category |

| DELETE | /api/categories/{id}/ | Delete category |



\## Installation



\### 1. Clone repository

