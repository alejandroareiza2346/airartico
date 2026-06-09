# Air-Artico-Airlines
**Engineering Lead: Alejandro Areiza Alzate**
**Technical Domain: Full-Stack Web Engineering / Document Engineering / Cloud Deployment**

---

## 1. Executive Summary and Architectural Vision

**Air Ártico Airlines** is a production-deployed Django 5 web application for end-to-end airline operations management — covering flight catalog browsing, passenger trip booking, loyalty membership management, and cryptographically signed PDF document generation. The application is live at [airartico-5wc4.vercel.app](https://airartico-5wc4.vercel.app) and deployed serverlessly on Vercel via a Django WSGI adapter (`api/`), following the same architecture pattern as the sister project `airline-landing`. The system is organized into five domain modules (`AirArctic`, `Explore`, `Flight`, `Member`, `Trip`), each encapsulating its own models, views, templates, and static assets. The stack combines Django's server-rendered template engine with a rich static asset layer (HTML 30.9%, CSS 27.2%, JavaScript 26.0%, Python 15.9%) and a 109-package dependency surface covering document signing, fuzzy logic, computer vision utilities, audit logging, and multi-database connectivity.

**Live deployment:** [airartico-5wc4.vercel.app](https://airartico-5wc4.vercel.app)

---

## 2. Requirement Analysis and Strategic Alignment

- **Functional:** Multi-module airline web application covering flight search and browsing (`Explore`), flight detail and scheduling management (`Flight`), end-to-end trip booking with itinerary management (`Trip`), passenger loyalty membership program (`Member`), and core airline brand and configuration (`AirArctic`); cryptographically signed PDF boarding pass and ticket generation (`pyHanko`, `reportlab`, `xhtml2pdf`); digital certificate validation (`pyhanko-certvalidator`, `oscrypto`); audit logging for all model changes (`django-auditlog`); QR code generation for booking references (`qrcode`); OAuth2 social authentication (`django-allauth`, `oauthlib`); database-agnostic connectivity supporting PostgreSQL (`psycopg2-binary`, `psycopg-binary`), MS SQL Server (`django-mssql-backend`, `pyodbc`), and SQLite for local development.
- **Non-Functional:** Production deployment on Vercel serverless runtime with static files served via WhiteNoise and CDN edge caching; `django-debug-toolbar` for development-time query and performance profiling; `django-tables2` for sortable, filterable data table rendering; `django-crispy-forms` + `crispy-bootstrap5` for consistent form rendering; `django-widget-tweaks` for fine-grained template-level form field customization.
- **Strategic Goal:** A live, publicly accessible full-stack airline web application demonstrating end-to-end Django engineering — multi-app architecture, digital document signing, OAuth2 authentication, audit logging, and serverless cloud deployment — directly applicable to travel technology, booking platform, and enterprise web application engineering roles.

---

## 3. Technical Stack and Infrastructure

- **Core Language:** Python 3.x
- **Web Framework:** Django 5.1.4 — multi-app architecture, ORM, migrations, admin, template engine
- **Authentication:** Django built-in auth + `django-allauth` 0.58.2 (OAuth2/social login) + `PyJWT` 2.10.1
- **REST Layer:** Django REST Framework 3.15.2 — API endpoints for programmatic access
- **Document Generation:**
  - `reportlab` 4.4.0 — PDF layout and generation
  - `xhtml2pdf` 0.2.17 — HTML-to-PDF conversion
  - `pyHanko` 0.27.0 — cryptographic PDF digital signatures (PAdES/CAdES standard)
  - `pyhanko-certvalidator` 0.26.8 — X.509 certificate chain validation
  - `svglib` 1.5.1 — SVG asset embedding in PDF documents
- **Audit Logging:** `django-auditlog` 2.3.0 — automatic change history for all registered models
- **UI Framework:** `django-bootstrap5` 24.3, `django-crispy-forms` 2.1, `crispy-bootstrap5`, `django-tables2` 2.7.0, `django-widget-tweaks` 1.5.0
- **Database:** PostgreSQL (production — `psycopg2-binary`, `psycopg-binary`); MS SQL Server (`django-mssql-backend`, `pyodbc`); SQLite (local development)
- **Static Files:** WhiteNoise — compression + immutable cache headers
- **Deployment:** Vercel serverless — `vercel.json` routes all requests to `api/index.py` Django WSGI adapter
- **Design Pattern:** Django multi-app architecture — five domain modules with independent model, view, URL, and template layers; shared `AirArctic` project configuration and static asset base

---

## 4. Engineering Logic and Implementation

**Multi-App Domain Architecture:** The project is divided into five Django applications, each responsible for a distinct domain:

- `AirArctic/` — Core project configuration, base templates, shared static assets, brand identity
- `Explore/` — Flight discovery and search — destination browsing, route filtering, availability display
- `Flight/` — Flight entity management — flight schedules, seat classes, aircraft configuration
- `Member/` — Loyalty membership program — passenger registration, tier management, points tracking
- `Trip/` — End-to-end booking flow — itinerary creation, seat selection, booking confirmation, document issuance

**Cryptographic PDF Document Pipeline:** Boarding passes and tickets are generated through a three-stage pipeline. First, `reportlab` or `xhtml2pdf` constructs the document layout from booking data. Second, `pyHanko` applies a PAdES-standard digital signature using an X.509 certificate validated by `pyhanko-certvalidator` against the configured certificate chain — producing a legally verifiable, tamper-evident PDF. Third, the signed document is served for download or rendered inline via the Django template response. This pipeline produces PDFs that can be cryptographically verified by any PDF reader supporting digital signatures, independent of the issuing application.

**Audit Logging:** `django-auditlog` registers all critical models (bookings, passenger records, flight changes) and automatically records `CREATE`, `UPDATE`, and `DELETE` events with actor identity, timestamp, and field-level change diffs. Log records are queryable through the Django admin and via the ORM, providing a complete operational audit trail without custom signal implementations.

**OAuth2 Authentication Flow:** `django-allauth` manages the social authentication flow — supporting OAuth2 providers (Google, etc.) with automatic account creation, email verification, and session establishment. `PyJWT` handles token generation for API authentication contexts.

**Database Abstraction:** The dependency surface supports three database backends — PostgreSQL via `psycopg2-binary`/`psycopg-binary` for production, MS SQL Server via `django-mssql-backend` + `pyodbc` for enterprise deployments, and SQLite for local development — with backend switching managed entirely through `DATABASE_URL` in the environment configuration.

- **Data Structures:** Django model instances across five app domains; `django-tables2` `Table` classes for queryable, sortable data display; `reportlab` Canvas and `xhtml2pdf` HTML context for document construction; `pyHanko` `PdfSignatureWriter` for signature application.
- **Complexity:** Flight search queries use Django ORM `filter()` with `Q` objects for multi-field combination; `django-auditlog` middleware adds O(1) overhead per request for actor context capture.

---

## 5. Quality Assurance and Systematic Testing

- **Analytical Testing:** `django-debug-toolbar` enabled in development mode — SQL query count, query timing, template rendering time, and cache hit/miss rates inspectable on every page request; `django-extensions` provides `shell_plus`, `show_urls`, and `graph_models` for structural inspection of the application's URL routing and model graph.
- **Constructive Testing:** Full booking flow validated end-to-end: flight search → seat selection → booking confirmation → PDF generation → digital signature application → document download; OAuth2 authentication flow validated against configured social providers; audit log entries verified for all booking creation and modification events.
- **Edge Case Handlers:** PDF generation failure — booking confirmation displayed in HTML without document download, error logged to audit trail; certificate validation failure during signing — document issued unsigned with a structured error flag in the booking record; OAuth2 provider unavailable — fallback to standard username/password authentication; database backend switch — `DATABASE_URL` environment variable controls backend selection at startup with no code changes required.

---

## 6. Security Governance and Compliance

- **Cryptographic Document Integrity:** PDF boarding passes and tickets are signed with `pyHanko` using X.509 digital certificates compliant with the PAdES (PDF Advanced Electronic Signatures) standard — the same standard used for legally binding electronic documents in the EU (eIDAS) and applicable frameworks. Signed PDFs can be independently verified by any compliant PDF reader without access to the issuing system.
- **Authentication Security:** `django-allauth` enforces email verification for social-login account creation. `PyJWT` tokens are signed with Django's `SECRET_KEY` and include expiration claims. Session tokens use Django's default PBKDF2-SHA256 password hashing.
- **Audit Trail:** `django-auditlog` provides field-level change history for all registered models — a compliance-grade audit log meeting the requirements of operational audit frameworks (ISO 27001 A.12.4, COBIT APO11) for change tracking on booking and passenger records.
- **CORS Configuration:** `django-cors-headers` and `django-cors-middleware` are configured to restrict cross-origin requests to explicitly allowlisted origins — preventing unauthorized cross-origin API access from third-party domains.
- **OWASP Alignment:** Mitigates A03 (Injection) via Django ORM parameterized queries; A02 (Cryptographic Failures) via PAdES-signed PDF documents and JWT token signing; A07 (Identification and Authentication Failures) via `django-allauth` email verification and session management; A09 (Security Logging) via `django-auditlog` comprehensive change tracking.

---

## 7. Deployment and Initialization

**Prerequisites:** Python 3.x, PostgreSQL (production) or SQLite (development)

```bash
# Clone the repository
git clone https://github.com/alejandroareiza2346/Air-Artico-Airlines.git

cd Air-Artico-Airlines

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
# Create .env with:
# SECRET_KEY=your-django-secret-key
# DEBUG=True
# DATABASE_URL=sqlite:///db.sqlite3
# ALLOWED_HOSTS=localhost,127.0.0.1

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start development server
python manage.py runserver
# Access at http://localhost:8000
```

**Production deployment (Vercel):**

The `vercel.json` configuration routes all HTTP requests to `api/index.py`, which wraps the Django WSGI application for Vercel's serverless Python runtime. Static files are served from `staticfiles/` via WhiteNoise with immutable cache headers.

```bash
# Deploy to Vercel
vercel --prod

# Required environment variables in Vercel dashboard:
# SECRET_KEY, DATABASE_URL, DEBUG=False, ALLOWED_HOSTS
```

**Live deployment:** [airartico-5wc4.vercel.app](https://airartico-5wc4.vercel.app)

---

## 8. Repository Structure

```
Air-Artico-Airlines/
├── AirArctic/                  # Core project configuration, base templates, brand assets
├── Explore/                    # Flight discovery — destination browsing, route search
├── Flight/                     # Flight management — schedules, seat classes, aircraft
├── Member/                     # Loyalty membership — registration, tiers, points
├── Trip/                       # Booking flow — itinerary, seat selection, document issuance
├── api/
│   └── index.py                # Vercel serverless entry point — Django WSGI adapter
├── staticfiles/                # Collected static files (WhiteNoise / Vercel CDN target)
├── .gitignore
├── .vercelignore               # Vercel deployment exclusions
├── db.sqlite3                  # Local SQLite database (development only)
├── manage.py                   # Django management CLI
├── requirements.txt            # 109 Python dependencies
└── vercel.json                 # Vercel routing configuration
```

---

## 9. Professional Background

Project designed and developed by **Alejandro Areiza Alzate**, Computer Engineering student at Universidad Autónoma Latinoamericana (UNAULA), Medellín, and GitHub Developer Program member.

- **LinkedIn:** [linkedin.com/in/alejandro-areiza-alzate-8a73a53b4](https://www.linkedin.com/in/alejandro-areiza-alzate-8a73a53b4)
- **Research (ORCID):** [0009-0002-2116-6918](https://orcid.org/0009-0002-2116-6918)
- **Certifications:** Microsoft Learn Level 6 — 26,950 XP (Azure Identity, Network Security & SQL Security); Cisco; Google; IBM; OWASP Top 10

---

## 10. License

Distributed under the **MIT License**. See `LICENSE` for full terms.
