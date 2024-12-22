# CodeLeap Network API

## Technologies

- Python 3.12
- Django
- Django Rest Framework
- PostgreSQL
- Docker

---

## Running the API Locally

Follow these steps to set up and run the application locally:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/MarcosAllysson/codeleap_api.git
   cd codeleap-api
   ```

2. **Set up a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your `.env` file:**
   Update the `.env` file with appropriate settings (e.g., database credentials).

5. **Apply database migrations:**
   ```bash
   python src/manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python src/manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python src/manage.py runserver
   ```

8. **Access the application:**
   - API: `http://localhost:8000`
   - Admin Interface: `http://localhost:8000/admin`

---

## Running the API via Docker

Follow these steps to set up and run the application using Docker:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/MarcosAllysson/codeleap_api.git
   cd codeleap-api
   ```

2. **Build and start the containers:**
   ```bash
   docker-compose up --build
   ```

3. **Access the application:**
   - API: `http://localhost:8000`
   - Admin Interface: `http://localhost:8000/admin`

4. **Pre-configured Superuser:**
   - Username: `admin`
   - Password: `Z8FEFXPF*7uCw~k},G$(t~'-8K"7|n`

   > **Note:** The superuser is automatically created when using Docker.

---

## API Documentation

Once the server is running, you can access the API documentation at:

- **Swagger UI:** `http://localhost:8000/api/docs/`
- **OpenAPI Schema:** `http://localhost:8000/api/schema/`

---

## Endpoints

- `GET /careers/` - List all posts
- `POST /careers/` - Create a new post
- `PATCH /careers/{id}/` - Update a post
- `DELETE /careers/{id}/` - Delete a post

---

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

---

## Running Tests

### Locally

Run the following command:
```bash
python src/manage.py test posts.tests
```

### Via Docker

Run the following command:
```bash
docker-compose exec backend python src/manage.py test
```

---

## Notes

- Ensure Docker and Docker Compose are installed before running the Docker setup.
- For local development, make sure PostgreSQL is running and properly configured in the `.env` file.
- The superuser is created automatically when running the application via Docker. If running locally, create the superuser manually.

