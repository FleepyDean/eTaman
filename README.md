# eTaman

A centralized web application developed for **Jabatan Landskap Negeri Johor (JLNJ)** to streamline the collection, management and analysis of public park data across all local authorities (PBT).

---

## Authentication Subsystem

**Developer: AMMAR**

| Sprint | Module Name | Frontend | Backend |
|--------|-------------|----------|---------|
| 1 | Login Module | Components:<br>• [src/App.jsx](src/App.jsx) (`LoginPage`) | Backend:<br>• [django_backend/taman/views.py](django_backend/taman/views.py) |
| 2 | User Registration Module | Components:<br>• [src/App.jsx](src/App.jsx) (`RegisterPage`) | Backend:<br>• [django_backend/taman/views.py](django_backend/taman/views.py) |
| 3 | Email Verification Module | Components:<br>• [src/App.jsx](src/App.jsx) | Config:<br>• [django_backend/config/settings.py](django_backend/config/settings.py) |

---

## Data Gathering Subsystem

**Developer: EDWARD**

| Sprint | Module Name | Frontend | Backend |
|--------|-------------|----------|---------|
| 1 | Template Management Module | Components:<br>• [src/App.jsx](src/App.jsx) (`BorangTaman`) | Controllers:<br>• [django_backend/taman/api.py](django_backend/taman/api.py)<br>Models:<br>• [django_backend/taman/models.py](django_backend/taman/models.py)<br>Routes:<br>• [django_backend/taman/urls.py](django_backend/taman/urls.py) |
| 2 | Drag & Drop Parser Module | Components:<br>• [src/App.jsx](src/App.jsx) (`ImportPreview`, `handleParseFile`) | Controllers:<br>• [django_backend/taman/api.py](django_backend/taman/api.py)<br>Routes:<br>• [django_backend/taman/urls.py](django_backend/taman/urls.py) |
| 3 | Validation & Merge Engine | Components:<br>• [src/App.jsx](src/App.jsx) (`handleConfirmImport`) | Controllers:<br>• [django_backend/taman/api.py](django_backend/taman/api.py)<br>Models:<br>• [django_backend/taman/models.py](django_backend/taman/models.py) |

---

## Visualizations and Analytics Subsystem

**Developer: ZULAIKHA**

| Sprint | Module Name | Frontend | Backend |
|--------|-------------|----------|---------|
| 1 | Dashboard Overview Module | Components:<br>• [src/App.jsx](src/App.jsx) (`LaporanStatistik`) | Controllers:<br>• [django_backend/taman/api.py](django_backend/taman/api.py)<br>Routes:<br>• [django_backend/taman/urls.py](django_backend/taman/urls.py) |
| 2 | Data Filtering and Comparative Analysis Module | Components:<br>• [src/App.jsx](src/App.jsx) (`filteredTaman`, `taburanDaerah`, `taburanJenis`) | Controllers:<br>• [django_backend/taman/api.py](django_backend/taman/api.py) |
| 3 | Reporting and Trend Analysis Module | Components:<br>• [src/App.jsx](src/App.jsx) (`generatePDF`, `jenisChartData`, `daerahChartData`) | Controllers:<br>• [django_backend/taman/api.py](django_backend/taman/api.py)<br>Config:<br>• [django_backend/config/settings.py](django_backend/config/settings.py) |

---

## Park Profile and Mapping Subsystem

**Developer: DANISH**

| Sprint | Module Name | Frontend | Backend |
|--------|-------------|----------|---------|
| 1 | Park Information Module | Components:<br>• [src/App.jsx](src/App.jsx) (`ProfilTaman`)<br>• [src/App.jsx](src/App.jsx) (`SenaraiBilanganTaman`) | Controllers:<br>• [django_backend/taman/api.py](django_backend/taman/api.py)<br>Models:<br>• [django_backend/taman/models.py](django_backend/taman/models.py)<br>Routes:<br>• [django_backend/taman/urls.py](django_backend/taman/urls.py) |
| 2 | Geo-Mapping Module | Components:<br>• [src/App.jsx](src/App.jsx) (`ProfilTaman` map iframe) | |
| 3 | Media and Document Module | Components:<br>• [src/App.jsx](src/App.jsx) (`uploadImages`, `removeUploadedImage`, `BorangTaman`) |  |

---

## System Administration Subsystem

**Developer: QISTINA**

| Sprint | Module Name | Frontend | Backend |
|--------|-------------|----------|---------|
| 1 | Master Data Management Module | Components:<br>• [src/SystemAdmin.jsx](src/SystemAdmin.jsx) (`MasterDataManagement`) | Controllers:<br>• [django_backend/taman/admin_api.py](django_backend/taman/admin_api.py)<br>Models:<br>• [django_backend/taman/models.py](django_backend/taman/models.py)<br>Routes:<br>• [django_backend/taman/urls.py](django_backend/taman/urls.py) |
| 2 | User Account Management Module | Components:<br>• [src/SystemAdmin.jsx](src/SystemAdmin.jsx) (`UserAccountManagement`) | Controllers:<br>• [django_backend/taman/admin_api.py](django_backend/taman/admin_api.py)<br>Routes:<br>• [django_backend/taman/urls.py](django_backend/taman/urls.py) |
| 3 | Audit and Activity Log Module | Components:<br>• [src/SystemAdmin.jsx](src/SystemAdmin.jsx) (`AuditLog`) | Controllers:<br>• [django_backend/taman/admin_api.py](django_backend/taman/admin_api.py)<br>Models:<br>• [django_backend/taman/models.py](django_backend/taman/models.py)<br>Routes:<br>• [django_backend/taman/urls.py](django_backend/taman/urls.py) |

---

## Technology Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React.js, Tailwind CSS, Lucide Icons |
| **Build Tool** | Vite |
| **Backend** | Django, Django REST (custom API views) |
| **Database** | SQLite (development) |
| **AI** | Google Gemini API |

---

## Getting Started

### Prerequisites

- **Node.js** (v18+) — [nodejs.org](https://nodejs.org)
- **Python** (v3.11+) — [python.org](https://python.org)
- **Git** — [git-scm.com](https://git-scm.com)

### 1. Clone the Repository

```bash
git clone https://github.com/FleepyDean/eTaman.git
cd eTaman
```

### 2. Frontend Setup

```bash
npm install
npm run dev
```

### 3. Backend Setup

```bash
cd django_backend
python -m venv venv

# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

> **Note:** Both the frontend (port 5173) and backend (port 8000) must be running simultaneously.

### 4. Environment Variables (Optional)

Create a `.env` file in the project root:

```env
VITE_API_BASE_URL=http://localhost:8000
```

---

## For Collaborators

```bash
git checkout main
git pull origin main
git checkout -b feature/your-feature-name

git add -A
git commit -m "Add your feature description"
git push origin feature/your-feature-name
```

Then create a **Pull Request** on GitHub to merge into `main`.
