# Query API Fullstack (Clean Architecture)

This project is a full-stack application that follows Uncle Bob’s Clean Architecture principles. It includes:

- **Backend**: Flask-based API with clean use cases, JWT auth, SQLite
- **Frontend**: React + Tailwind UI for managing users
- **Fully containerized** with Docker and `docker-compose`

---

## Features

### Backend (Flask)
- Clean Architecture: Entities, Use Cases, Gateways, Controllers
- JWT Authentication (`admin` / `password`)
- SQLite persistence
- RESTful endpoints: `/login`, `/insert`, `/users`, `/delete`

### Frontend (React + Tailwind)
- Login interface
- View, insert, and delete users
- Integrated with JWT and API

---

## How to Run

### 1. Clone or unzip this repo

```bash
cd query_api_fullstack_dockerized
```

### 2. Run the app

```bash
docker-compose up --build
```

- Backend: [http://localhost:5000](http://localhost:5000)
- Frontend: [http://localhost:5173](http://localhost:5173)

---

## Login Credentials

```
Username: admin
Password: password
```

---

## Folder Structure

```
.
├── backend/       # Flask Clean Architecture
├── frontend/      # React + Tailwind UI
├── docker-compose.yml
```

---

## Future Enhancements (Optional)

- PostgreSQL integration
- CI/CD with GitHub Actions
- Role-based access control
- E2E testing with Cypress or Playwright

---

## License

MIT
