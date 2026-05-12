# API / REST API / FastAPI

---

# 1. What is an API?

**API = Application Programming Interface**

## Simple Meaning

An API is a mechanism that allows two software systems to communicate with each other.

It defines:
- how requests are sent
- how responses are returned
- what data format is used

APIs enable:
- frontend ↔ backend communication
- app ↔ database interaction
- service ↔ service integration

---

## Real-World Analogy

Imagine ordering food in a restaurant:

| Component | Real World | Software World |
|---|---|---|
| Customer | You | Client / Frontend |
| Kitchen | Chef | Backend Server |
| Waiter | Takes order | API |

The customer does not directly enter the kitchen.

Instead:
1. Customer places an order
2. Waiter carries request to kitchen
3. Kitchen prepares response
4. Waiter returns food

Similarly:
- Client sends request to API
- API communicates with backend
- Backend processes data
- API returns response

---

## Why APIs Are Important

APIs allow:
- Mobile apps to access servers
- Websites to fetch data dynamically
- Third-party integrations
- Microservices communication
- Automation between systems

### Examples
- Payment APIs
- Weather APIs
- Authentication APIs
- Maps APIs

---

# 2. What is a REST API?

**REST = Representational State Transfer**

REST is a set of architectural principles used for designing web APIs.

A REST API uses:
- HTTP protocol
- URLs for resources
- Stateless communication
- Standard HTTP methods
- JSON data format

---

# Core Principles of REST APIs

---

## 1. HTTP Methods

HTTP methods define the type of action to perform.

| Method | Purpose | Example |
|---|---|---|
| GET | Read data | Get all users |
| POST | Create new data | Add new product |
| PUT | Replace existing data | Replace user info |
| PATCH | Partially update data | Update only email |
| DELETE | Remove data | Delete user |

---

## Example Requests

### GET Request

```http
GET /users
```

Fetch all users.

---

### POST Request

```http
POST /users
```

Create a new user.

---

### PUT Request

```http
PUT /users/1
```

Replace complete user data.

---

### PATCH Request

```http
PATCH /users/1
```

Update only specific fields.

---

### DELETE Request

```http
DELETE /users/1
```

Remove a user.

---

# 2. Resources (URLs)

In REST APIs, everything is treated as a **resource**.

A resource is represented using URLs.

## Examples

| Resource | URL |
|---|---|
| All users | `/users` |
| Single user | `/users/1` |
| All products | `/products` |
| Single product | `/products/101` |

---

## REST URL Best Practices

### Use nouns, not verbs

✅ Good:
```txt
/users
/products
/orders
```

❌ Bad:
```txt
/getUsers
/createProduct
/deleteOrder
```

---

# 3. Stateless Architecture

REST APIs are **stateless**.

This means:
- Each request is independent
- Server does NOT remember previous requests
- Every request must contain all required information

---

## Example

If authentication is required:

```http
Authorization: Bearer token
```

The token must be sent with EVERY request.

The server does not remember previous authentication automatically.

---

## Benefits of Stateless APIs

- Easier scaling
- Better reliability
- Simpler architecture
- Faster performance in distributed systems

---

# 4. JSON Responses

Most REST APIs use JSON format.

JSON = JavaScript Object Notation

It is:
- lightweight
- human-readable
- easy to parse

---

## Example JSON

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 1200,
  "in_stock": true
}
```

---

## JSON Array Example

```json
[
  {
    "id": 1,
    "name": "Laptop"
  },
  {
    "id": 2,
    "name": "Phone"
  }
]
```

---

# 5. HTTP Status Codes

Status codes indicate request result.

| Code | Meaning |
|---|---|
| 200 | Success |
| 201 | Created Successfully |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

## Example

```http
HTTP/1.1 200 OK
```

Request completed successfully.

---

# 6. Request and Response Structure

## Client Request

```http
POST /users
Content-Type: application/json
```

```json
{
  "name": "John",
  "email": "john@example.com"
}
```

---

## Server Response

```json
{
  "id": 1,
  "name": "John",
  "email": "john@example.com"
}
```

---

# 7. What is FastAPI?

**FastAPI** is a modern Python framework used to build APIs quickly and efficiently.

It is based on:
- Python type hints
- ASGI
- Starlette
- Pydantic

---

## Why FastAPI Is Popular

### Features

- Very fast performance
- Automatic API documentation
- Easy request validation
- Async support
- Clean syntax
- Type safety

---

## Installation

```bash
pip install fastapi uvicorn
```

---

# 8. First FastAPI Application

## Create `main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}
```

---

## Run Server

```bash
uvicorn main:app --reload
```

---

## Output

Visit:

```txt
http://127.0.0.1:8000
```

Response:

```json
{
  "message": "Hello World"
}
```

---

# 9. FastAPI Automatic Documentation

FastAPI automatically generates API docs.

## Swagger UI

```txt
http://127.0.0.1:8000/docs
```

---

## ReDoc

```txt
http://127.0.0.1:8000/redoc
```

---

# 10. Path Parameters

Path parameters allow dynamic URLs.

## Example

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

---

## Request

```txt
/users/5
```

---

## Response

```json
{
  "user_id": 5
}
```

---

# 11. Query Parameters

Query parameters are optional URL values.

## Example

```python
@app.get("/products")
def get_products(limit: int = 10):
    return {"limit": limit}
```

---

## Request

```txt
/products?limit=5
```

---

# 12. Request Body

FastAPI uses Pydantic models for validation.

## Example

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

@app.post("/users")
def create_user(user: User):
    return user
```

---

# 13. API Testing Tools

Popular tools for testing APIs:

| Tool | Purpose |
|---|---|
| Postman | API testing |
| Insomnia | REST testing |
| cURL | Command-line requests |
| Swagger UI | Interactive docs |

---

## Example cURL Request

```bash
curl -X GET http://127.0.0.1:8000/
```

---

# 14. Advantages of REST APIs

- Platform independent
- Easy integration
- Scalable
- Flexible
- Lightweight communication
- Widely supported

---

# 15. REST API Best Practices

## Use Proper HTTP Methods

- GET → fetch
- POST → create
- PUT/PATCH → update
- DELETE → remove

---

## Use Meaningful URLs

✅ Good:
```txt
/users/1/orders
```

❌ Bad:
```txt
/getUserOrders?id=1
```

---

## Return Proper Status Codes

Always return meaningful status codes.

Example:
- `201 Created`
- `404 Not Found`

---

## Version Your APIs

Example:

```txt
/api/v1/users
/api/v2/users
```

---

# 16. Difference Between REST API and FastAPI

| REST API | FastAPI |
|---|---|
| Architectural style | Python framework |
| Defines rules | Implements APIs |
| Language independent | Python specific |
| Uses HTTP | Builds REST APIs |

---

# 17. Summary

## API
A communication interface between software systems.

## REST API
A standardized way to design web APIs using HTTP.

## FastAPI
A modern Python framework for building high-performance APIs.

---

# Quick Revision Notes

| Concept | Key Point |
|---|---|
| API | Communication bridge |
| REST | Rules for API design |
| GET | Read |
| POST | Create |
| PUT | Replace |
| PATCH | Partial update |
| DELETE | Remove |
| JSON | Data format |
| FastAPI | Python API framework |
| Stateless | No memory between requests |

---

---

