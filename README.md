# Employee Management API

This project is a basic REST API built with Django and Django Rest Framework (DRF) to manage employees in a company. It focuses on CRUD operations, RESTful principles, and includes token-based authentication using Simple JWT.

## Features

- CRUD operations for Employee model
- Token-based authentication (JWT)
- Filtering employees by department and role
- Pagination (10 employees per page)
- Basic unit tests for each endpoint

## Setup

1. Clone the repository:
   git clone `https://github.com/theMerovingian03/company_api.git`

2. Create a virtual environment and activate it:

   ```
   python -m venv myenv
   myenv\Scripts\activate
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   cd company_api
   ```

4. Set up the database:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (for accessing the admin panel):
   ```
   python manage.py createsuperuser
   ```

## Running the Server

To start the development server, run: <br>
`    python manage.py runserver
   `

The API will be available at
`http://127.0.0.1:8000/api/`.

## Running Tests

To run the unit tests, use the following command:

```
python manage.py test
```

## API Endpoints

All endpoints require authentication. Use the token obtained from the login endpoint in the Authorization header as `Bearer <token>`.

- Create an Employee: POST `/api/employees/`
- List all Employees: GET `/api/employees/`
- Retrieve a Single Employee: GET `/api/employees/{id}/`
- Update an Employee: PUT `/api/employees/{id}/`
- Delete an Employee: DELETE `/api/employees/{id}/`

### Filtering

You can filter employees by department and role:

- GET `/api/employees/?department=HR`
- GET `/api/employees/?role=Manager`

### Pagination

Results are paginated with 10 employees per page:

- GET `/api/employees/?page=2`

## Authentication

To obtain a token, send a POST request to `/api/token/` with username and password. This will return an access token and a refresh token.

Example:

```

POST /api/token/
{
"username": "your_username",
"password": "your_password"
}

```

To use the token, include it in the Authorization header of your requests:

```

Authorization: Bearer <your_access_token>

```

To refresh the token, send a POST request to `/api/token/refresh/` with the refresh token.

## Employee Model

- `id`: Unique identifier (auto-generated)
- `name`: String, required
- `email`: Email field, required and unique
- `department`: String, optional (e.g., "HR", "Engineering", "Sales")
- `role`: String, optional (e.g., "Manager", "Developer", "Analyst")
- `date_joined`: Date, auto-generated on creation

## Error Handling

- 201 Created: Successful creation
- 200 OK: Successful retrieval or update
- 204 No Content: Successful deletion
- 400 Bad Request: Validation errors
- 401 Unauthorized: Authentication failure
- 404 Not Found: Resource not found
