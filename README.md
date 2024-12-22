# CodeLeap Network API

## Technologies

- Python 3.9
- Django
- Django Rest Framework
- PostgreSQL
- Docker

## Local Development Setup

1. Clone this repository
2. Create and activate a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python src/manage.py migrate`
5. Run server: `python src/manage.py runserver`

## Docker Setup

1. Clone this repository
2. Run: `docker-compose up --build`
3. The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access the API documentation at:

- Swagger UI: `http://localhost:8000/api/docs/`
- OpenAPI Schema: `http://localhost:8000/api/schema/`

## Endpoints

- `GET /careers/` - List all posts
- `POST /careers/` - Create a new post
- `PATCH /careers/{id}/` - Update a post
- `DELETE /careers/{id}/` - Delete a post

## Request Examples

### Create a Post

```json
POST /careers/
{
    "username": "john_doe",
    "title": "My First Post",
    "content": "Hello World!"
}
```

### Update a Post

```json
PATCH /careers/1/
{
    "title": "Updated Title",
    "content": "Updated content"
}
```

## Running Tests locally

```bash
python src/manage.py test posts.tests
```

## Running Tests via Docker

```bash
docker-compose exec backend python src/manage.py test
```

## Admin Interface

- URL: `http://localhost:8000/admin/`
- Superuser credentials:
  Username: `admin`
  Password: `Z8FEFXPF*7uCw~k},G$(t~'-8K"7|n`
