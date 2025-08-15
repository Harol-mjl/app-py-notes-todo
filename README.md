# NOTES API NOTES

# Notes API

## Tech Stack
- Python 3.13.2
- Django 5.2.5
- Django REST Framework 3.16.1
- drf-spectacular (OpenAPI / Swagger)
- Implemented with Docker PostgreSQL

## Install Requirements
    - pip install -r requirements.txt

## Database Setup (BBDD)

### 1. Start the database in Docker
Run the following command to create and start the PostgreSQL container:

docker run -d --name notes-postgres \
  -e POSTGRES_DB=notes_db \
  -e POSTGRES_USER=notes_user \
  -e POSTGRES_PASSWORD=notes_pass \
  -p 5432:5432 \
  postgres:16

### 2. Configure environment variables
    - cp .env.example .env
### Edit .env and set: 
    
- DATABASE_URL=postgres://notes_user:notes_pass@localhost:5432/notes_db
- DJANGO_SECRET_KEY=CHANGE_ME

### 3. Apply migrations
python manage.py migrate

### 4. Run the development server
python manage.py runserver

