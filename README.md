# Puzzle-Solving Hub

**Project Description:** An invite-only, web-base hub for solving ARGs collaboratively for me & my friends.


---

## Table of Contents
1.  About the Project
2.  Technology Stack
3.  Getting Started
4.  Develpment
5.  Contact
---

## 1. About the Project

### Description
An invite-only, web-based hub for small teams to collaboratively solve Alternate Reality Games (ARGs) and other complex puzzles, featuring advanced analytical tools and centralized version history.

### Key Features

* **Catalog:** A browsable "catalog" for finding and joining existing PuzzleHubs created by users of the web app.
* **Collaborative LogBook:** Centralized narrative feed for theories, findings, and solved steps, linked to discussion threads.
* **Source Data Versioning:** A dedicated database (`SourceTextEntry`) to track every raw ciphertext input, solver attempt, key used, and resulting output.
* **Auto-Solver Engine:** Advanced tool to process ciphertext and provide ranked solutions based on statistical analysis and dictionary match rates.
* **Cipher Tools:** A variaty of common decoding/encoding methods.
* **Invite-Only Auth:** Secure, restricted access for small, trusted teams.

---

## 2. Technology Stack

This project is fully containerized for consistent development and deployment.

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Backend** | Python 3.14 / Django | Core application logic and API. |
| **Frontend** | Tailwind CSS (via Django Templates) | Current styling/UI layer. |
| **Database** | PostgreSQL 17 (Dockerized) | Primary persistent data storage. |
| **Admin UI** | PgAdmin 4 (Dockerized) | Web interface for database inspection. |
| **Package Manager** | `uv` | High-performance dependency management. |
| **Container** | Docker / Docker Compose | Environment management and orchestration. |

---

## 3. Getting Started

### Prerequisites

1.  **Git:** Installed and configured.
2.  **Docker & Docker Compose:** Installed and running.

### Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone [Your GitHub URL Here]
    cd puzzle-solving-hub
    ```

2.  **Configure Secrets:**
    * Create a file named **`.env`** in the root directory.
    * Ensure the **`.env`** file is excluded from version control using the provided **`.gitignore`** file.
    * Copy the required variables for the database and Django from the template provided by the team (or use the following template):
    ```ini
    # .env template (must be filled out)
    SECRET_KEY=a_unique_django_secret
    DB_HOST=db
    DB_NAME=puzzle_db
    DB_USER=puzzle_user
    DB_PASSWORD=secure_password
    POSTGRES_DB=puzzle_db
    POSTGRES_USER=puzzle_user
    POSTGRES_PASSWORD=secure_password
    PGADMIN_DEFAULT_EMAIL=admin@hub.com
    PGADMIN_DEFAULT_PASSWORD=admin
    ```

3.  **Build and Run Containers:**
    ```bash
    # This command builds the app, db, and admin containers and starts them
    docker compose build --no-cache
    docker compose up
    ```

4.  **Initialize Database & Superuser:**
    * Once containers are running, execute the following commands inside the `web` container:
    ```bash
    # Run Migrations
    docker compose exec web python manage.py migrate

    # Create Superuser
    docker compose exec web python manage.py createsuperuser
    ```

### Access Points

* **Web Application:** [http://localhost:8000](http://localhost:8000) |
* **Django Admin:** [http://localhost:8000/admin/](http://localhost:8000/admin/)
* **PgAdmin 4:** [http://localhost:5050](http://localhost:5050) (Login with credentials from your `.env`)

---

## 4. Development

### Running Management Commands

Due to the use of `uv` and the custom Docker entrypoint, all Django management commands can be run directly via `docker compose exec`:

| Action | Command |
| :--- | :--- |
| Run Tests | `docker compose exec web python manage.py test` |
| Make Migrations | `docker compose exec web python manage.py makemigrations [app_name]` |
| Stopping Services | `docker compose down` |
| Shell Access | `docker compose exec web python manage.py shell` |

### Working in the Container

For a better development experience, use the **VS Code Remote - Containers** extension to open the project directly inside the running container. This provides a clean, pre-configured development environment with access to all packages.

---

## 5. Contact

* **Created By:** [Radiance3138](https://github.com/Radiance3138) 
* **License:** MIT License