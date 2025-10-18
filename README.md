# HNG 0 — Django REST API

This is a simple Django REST API built for the **HNG Internship Task**.  
It exposes a single endpoint (`/me/`) that returns a JSON response containing user details and a random fact.

---

## 🚀 Features

- Built with **Python** and **Django REST Framework**
- Returns JSON data about the developer
- Deployed on **Railway**
- Includes timestamp and fun fact for dynamic response

---

## 📦 Project Structure

```
HNG_0/
├── HNG_0/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── profile_api/
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── manage.py
├── requirements.txt
└── Procfile
```

---

## ⚙️ Setup Instructions (Local)

### 1. Clone the Repository

```bash
git clone https://github.com/Eros4321/HNG_0.git
cd HNG_0
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

Then open your browser and go to:  
👉 **http://127.0.0.1:8000/me/**

---

## 🧠 API Endpoint

### `GET /me/`

**Response Example:**

```json
{
  "status": "success",
  "user": {
    "email": "BenjaminOwase@gmail.com",
    "name": "Benjamin Eromosele Odion-Owase",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-18T09:47:10.236092+00:00",
  "fact": "Mohammed loved cats and reportedly his favorite cat, Muezza, was a tabby. Legend says that tabby cats have an “M” for Mohammed on top of their heads because Mohammad would often rest his hand on the cat’s head."
}
```

---

## 🌍 Deployment

This project is deployed on **Railway**.  
Your live endpoint can be accessed at:

👉 [https://web-production-f9376.up.railway.app/me/](https://web-production-f9376.up.railway.app/me/)

---

## 🔑 Environment Variables

This project does not require any environment variables for local development.  
However, in production, ensure you set:

| Variable | Description | Example |
|-----------|-------------|----------|
| `DJANGO_SETTINGS_MODULE` | Django settings path | `HNG_0.settings` |
| `PORT` | Server port (Railway automatically provides this) | `8000` |

---

## 🧪 Tests

To test locally:
1. Run the development server.
2. Visit [http://127.0.0.1:8000/me/](http://127.0.0.1:8000/me/)  
3. Ensure the API returns a valid JSON response with:
   - `status`
   - `user` object
   - `timestamp`
   - `fact`

---

## 👨‍💻 Author

**Benjamin Eromosele Odion-Owase**  
📧 Email: [BenjaminOwase@gmail.com](mailto:BenjaminOwase@gmail.com)  
💻 Stack: Python / Django

---

## 🏁 License

This project is open source and free to use for educational purposes.
