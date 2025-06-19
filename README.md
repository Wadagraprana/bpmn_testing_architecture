## 🚦 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Setup Environment Variables

* Copy `.env.example` to `.env`
* Edit `.env` as needed for local/staging/production

```bash
cp .env.example .env
# Then edit .env (e.g., Mongo URI, secret key, etc)
```

### 3. Create Python Virtual Environment

```bash
make env
```

### 4. Install Dependencies (and upgrade pip, setuptools, wheel)

```bash
make upgrade
```

Atau, jika hanya ingin install tanpa upgrade:

```bash
make install
```

### 5. Run Development Server

```bash
make dev
```

Open [http://localhost:5000](http://localhost:5000) to test.

```bash
make dev
```

Open [http://localhost:5000](http://localhost:5000) to test.

---

## 🚀 Production Deployment (Gunicorn)

```bash
make run
```

Or manually:

```bash
. .venv/bin/activate  # or .venv\Scripts\activate
gunicorn --bind 0.0.0.0:5000 --workers 4 'main:app'
```

---

## 🧪 Testing, Linting, Formatting

* **Run all tests:**

  ```bash
  make test
  ```
* **Lint:**

  ```bash
  make lint
  ```
* **Autoformat:**

  ```bash
  make format
  ```

---

## 🔨 Common Makefile Commands

| Command        | Description                         |
| -------------- | ----------------------------------- |
| `make env`     | Create Python virtual environment   |
| `make install` | Install all dependencies (dev+prod) |
| `make upgrade` | Upgrade pip & install dependencies  |
| `make dev`     | Run Flask dev server                |
| `make run`     | Run Gunicorn production server      |
| `make lint`    | Run linter (flake8)                 |
| `make format`  | Autoformat code (black + isort)     |
| `make test`    | Run tests with pytest               |
| `make shell`   | Open Flask shell                    |
| `make clean`   | Delete venv and cache files         |
| `make help`    | Show all commands                   |

---

## 📂 Folder by Responsibility

* **app/api/**: Flask blueprints/routes, organized per API version.
* **app/core/models/**: Domain models/entities.
* **app/core/schemas/**: Serialization & validation (Marshmallow/Pydantic).
* **app/core/services/**: Business/application logic.
* **app/core/repositories/**: Data access logic (MongoDB abstraction).
* **app/infrastructure/db/**: DB connection config (Mongo, etc).
* **app/utils/**: Logger, error handler, etc.
* **tests/**: Unit/integration tests.
* **migrations/**: Scripts for DB migration/seed (optional).

---

## 📝 Contribution

* Fork, create branch, commit and PR!
* Use `make lint format test` before PR
* All configs/secrets via `.env` (never commit real credentials!)

---

## 📖 License

MIT License. See [LICENSE](LICENSE) for details.

---

Happy coding! 🎉
