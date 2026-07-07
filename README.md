# Blog API

A REST API built with Django REST Framework and JWT Authentication.

## Features
- User registration and login with JWT
- Create, read, update, delete blog posts
- Comment on posts
- Protected endpoints require authentication

## Tech Stack
- Python, Django, Django REST Framework
- JWT Authentication (simplejwt)
- SQLite (local) / PostgreSQL (production)

## Endpoints
- POST /api/signup/ — Register
- POST /api/token/ — Login
- GET /api/posts/ — Get all posts
- POST /api/create/ — Create post (protected)
- PUT /api/update/<id>/ — Update post (protected)
- DELETE /api/delete/<id>/ — Delete post (protected)
- GET /api/comments/<id>/ — Get comments
- POST /api/post_comments/ — Add comment (protected)
