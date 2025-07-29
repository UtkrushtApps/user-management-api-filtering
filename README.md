# User Management API with Role and Status Filtering

## Task Overview

A small SaaS startup is building a FastAPI backend to manage users in their internal system. The backend must provide endpoints to create, retrieve, update, delete, and list users. Product managers need to filter users by both their role (e.g., admin, customer) and status (e.g., active, inactive) for better dashboard reporting. The business expects precise filtering, so only users matching all requested criteria should be returned.

## Guidance

- Implement a RESTful API using FastAPI and PostgreSQL for persistent user storage.
- Use SQLAlchemy (async mode) for ORM and database interaction.
- Ensure that the /users endpoint supports optional query parameters for role and status, and that the filtering logic combines them correctly (using logical AND, not OR).
- Structure your code to separate routers, models, services, configuration, and database layers for maintainability.
- Adhere to best practices, such as using Pydantic models for request and response validation, proper async/await usage, and handling errors with appropriate HTTP status codes.
- Containerize the application stack with Docker and use Docker Compose for local development.

## Objectives

- Build FastAPI endpoints to create, retrieve, update, delete, and list users stored in PostgreSQL.
- The /users listing endpoint must accept optional query parameters for both role and status, returning only users matching all provided filters.
- Implement proper input validation and error handling for all endpoints.
- Ensure the filtering logic is accurate — users must match both role and status if both are specified.
- Organize code according to best practices: routers, models, services, configuration, and DB session management.
- Provide a working Docker Compose setup for both FastAPI and PostgreSQL services.

## How to Verify

- Create several users in the system with different roles and statuses.
- Query the /users endpoint with a single filter (e.g., only role=admin) and confirm only matching users are returned.
- Query using multiple filters (e.g., role=admin&status=active) and verify that only users matching all filters appear in the response.
- Check that create, retrieve, update, and delete operations work as expected and respond with the correct HTTP status codes.
- Ensure the application runs successfully using Docker Compose and the PostgreSQL database is used for persistence.
