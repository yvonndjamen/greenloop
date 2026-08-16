# GreenLoop - Reusable Packaging Tracking Platform

A simple yet realistic Python Flask web application for logistics and engineering master students.

GreenLoop is built from the **e-commerce retailer's point of view**: it's the
internal back-office dashboard a retailer's ops/sustainability team would use to
see where their reusable packaging currently is (in circulation, shipped to a
customer, or returned), not a consumer-facing app and not a courier/driver app.
Think "admin panel for the reusable packaging fleet", the same way a retailer
already has an admin panel for orders or inventory.

Getting Started with GreenLoop

This guide is written for users with no programming experience. Follow the steps in order. You do not need to understand the code to run or demonstrate the application.

⸻

Before You Start

Before running GreenLoop, you need to install three things on your computer:

* Git — used to download the GreenLoop project
* Python — used to run the application
* A web browser — Chrome, Edge, Firefox, etc.

You only need to install these tools once.

1. Install Git

Go to the official Git website and download Git for your operating system:

https://git-scm.com/downloads

Install it using the default installation options.

After installation, open Command Prompt (Windows) or Terminal (Mac/Linux).

To check that Git was installed correctly, run:

git --version

You should see something similar to:

git version 2.x.x

If you see a version number, Git is ready.

⸻

2. Install Python

Download Python from the official Python website:

https://www.python.org/downloads/

Install the latest Python 3 version.

Important for Windows: During installation, make sure to check:

Add Python to PATH

before clicking Install Now.

After installation, close and reopen Command Prompt.

Check that Python is installed:

python --version

If that does not work on Windows, try:

py --version

You should see something similar to:

Python 3.x.x

⸻

3. Check that Python’s package manager is available

Python uses a tool called pip to install the libraries required by GreenLoop.

Run:

python -m pip --version

You should see information about the installed pip version.

If this works, your computer is ready to install GreenLoop.

⸻

Getting Started

4. Clone the repository

Open Command Prompt or Terminal.

Choose the folder where you want to keep the project. For example, you can use your Desktop:

cd Desktop

Then download the GreenLoop project:

git clone https://github.com/yvonndjamen/greenloop.git

Move into the project folder:

cd greenloop

You should now be inside the GreenLoop project.

⸻

5. Create a virtual environment

A virtual environment keeps GreenLoop’s Python libraries separate from other programs on your computer.

Run:

python -m venv .venv

This may take a few seconds.

You only need to do this once.

⸻

6. Activate the virtual environment

Windows

Run:

.venv\Scripts\activate

After activation, you should see something similar to:

(.venv) C:\Users\YourName\Desktop\greenloop>

The (.venv) at the beginning means the environment is active.

Mac/Linux

Run:

source .venv/bin/activate

You should also see (.venv) at the beginning of the command line.

⸻

7. Install the required dependencies

With the virtual environment activated, run:

python -m pip install -r requirements.txt

This installs all Python libraries required by GreenLoop.

The installation may take a little while.

You only need to do this the first time.

⸻

8. Start the application

Once the dependencies have finished installing, run:

python app.py

You should see a message indicating that the application is running, for example:

Running on http://127.0.0.1:5000

Do not close this Command Prompt/Terminal window while you are using the application.

The application is now running on your computer.

⸻

9. Open the GreenLoop dashboard

Open your normal web browser and go to:

http://localhost:5000

You should see the GreenLoop login page.

Use the demo account:

* Username: demo
* Password: demo123

⸻

10. Explore the pre-loaded simulated packages

The demo automatically creates sample data the first time it runs.

The application comes with sample packages:

* PKG001
* PKG002
* PKG003
* PKG004

They are already in different states, such as:

* in_circulation
* shipped
* returned

This means the dashboard should already contain information when you log in.

The KPIs, package table, and CO₂ metric should therefore be populated immediately.

Click on any package in the table to open its lifecycle/timeline view:

/package/<id>

⸻

11. Add more simulated packages / advance their status

You do not need any real QR codes, scanners, IoT devices, or physical packages for the demo.

GreenLoop simulates a package scan using a URL.

From the package detail page, you can use the on-screen action button.

You can also trigger a simulated scan directly from the terminal.

For example, to create a new package and mark it as shipped:

curl http://localhost:5000/scan/PKG010?action=shipped

Later, you can mark the same package as returned:

curl http://localhost:5000/scan/PKG010?action=returned

Then refresh the dashboard:

http://localhost:5000/dashboard

You should see the new package and updated metrics.

⸻

Quick Demo Flow

For the school presentation, you can use this simple sequence:

Before the presentation

Make sure:

* Git is installed
* Python is installed
* GreenLoop has been cloned
* The virtual environment has been created
* Dependencies have been installed

On the day of the presentation

Open Command Prompt/Terminal and go to the project:

cd Desktop\greenloop

Activate the environment:

.venv\Scripts\activate

Start the application:

python app.py

Then open:

http://localhost:5000

Log in with:

Username: demo
Password: demo123

You can then demonstrate the dashboard, open a package, show its lifecycle, and simulate a package being shipped or returned.

⸻

Important

When you are finished with the demo, go back to the Command Prompt/Terminal where the application is running and press:

Ctrl + C

This stops the GreenLoop application.

You can start it again later by activating the virtual environment and running:

python app.py

⸻

Why We Simulate Instead of Using Real QR Codes or IoT Sensors

The GreenLoop demo does not require physical devices.

A package “scan” is simulated by sending a request to the application, for example:

curl http://localhost:5000/scan/PKG010?action=shipped

This allows the complete package lifecycle to be demonstrated without requiring a real QR scanner, IoT sensor, or connected hardware.

## UI/UX Improvements

### Visual Design
- Card-based layouts with subtle shadows for modern appearance
- Status colors - Shipped (amber), Returned (green), In Circulation (blue)
- Responsive grid system - Works on mobile, tablet, and desktop
- Professional typography - Consistent font hierarchy and spacing

### Dashboard Features
- KPI Cards - Total packages, shipped, returned, CO₂ saved with visual indicators
- Package Table - Sortable list of all packages with current status
- Real-time Search - Client-side filtering by package ID
- CSV Export - Download all package data with one click

### Package Lifecycle View
- Timeline Visualization - Visual flow of package status changes
- Status Badges - Color-coded status indicators for quick scanning
- Simulated Scan Actions - Advance a package's status the same way a QR scan would
- Breadcrumbs - Easy navigation back to dashboard

---

## Key Features

CHECKED Login System - Secure authentication with password hashing
CHECKED Package Tracking - Simulated QR scanning via URL hits
CHECKED Dashboard - Real-time KPI metrics and package overview
CHECKED Package Lifecycle - Visual timeline of all status changes
CHECKED Status-Aware Package Pages - Only valid next actions are shown
CHECKED CSV Export - Download package data for reporting
CHECKED Search & Filter - Find packages quickly by ID
CHECKED Environmental Impact - CO₂ savings calculation
CHECKED JSON-based Storage - No database required
CHECKED Form Validation - Client-side and server-side validation

---

## Dashboard Metrics

- Total Packages - Count of all packages
- Currently Shipped - Packages in transit
- Returned Packages - Packages back in inventory
- In Circulation - Packages available for reuse
- CO₂ Saved - Environmental impact (0.5 kg per returned package)

---

## Features Explained for Students

### 1. Simulated QR Scanning
- **Location:** app.py - scan_package() route (/scan/<id>)
- **What it does:** Mimics what would happen if a real QR code were scanned, by recording a status event when the URL is hit
- **Technology:** A plain Flask route triggered by curl or a browser (no real QR image is generated - see note below)
- **Educational value:** Understand how a physical QR scan maps to a simple backend state change, without needing camera/image hardware to demo it

### 2. Package Lifecycle View (/package/<id>)
- **Location:** templates/package_detail.html and app.py - package_detail() route
- **What it does:** Shows a timeline of all status changes for a package
- **Features:** Status badge, simulated scan action button, event timeline
- **Educational value:** Understand request routing, template rendering, data visualization

### 3. CSV Export (/export/csv)
- **Location:** app.py - export_csv() function
- **What it does:** Generates and downloads a CSV file of all packages
- **Technology:** Uses Python's csv module and Flask's send_file()
- **Educational value:** Learn file generation, HTTP headers, data export patterns

### 4. Real-time Search
- **Location:** templates/dashboard.html - JavaScript search function
- **What it does:** Filters package table by ID without page reload
- **Technology:** Client-side JavaScript (vanilla, no frameworks)
- **Educational value:** DOM manipulation, event listeners, user experience design

### 5. API Endpoint (/api/packages)
- **Location:** app.py - api_packages() route
- **What it does:** Returns all packages as JSON
- **Technology:** Flask @app.route with JSON response
- **Educational value:** RESTful API design, JSON data format, authentication

---

## Project Structure

```
greenloop/
├── app.py                 # Main Flask application with all routes
├── data/
│   ├── users.json        # User database (auto-created)
│   └── packages.json     # Package tracking data
├── templates/
│   ├── login.html        # Login page with form validation
│   ├── dashboard.html    # Main dashboard with package table
│   └── package_detail.html   # Package lifecycle view
├── static/
│   └── style.css         # Modern CSS with card layouts
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── QUICK_START.md       # Detailed setup guide
```

---

## Technical Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python 3 + Flask 3.0 |
| **Authentication** | Werkzeug password hashing (scrypt) |
| **Data Storage** | JSON files |
| **Frontend** | HTML5 + CSS3 + Vanilla JavaScript |
| **Responsive Design** | CSS Grid & Flexbox |

---

## Learning Objectives

Students will learn:
- Flask web development fundamentals
- User authentication and security (password hashing)
- Template rendering with Jinja2
- Responsive CSS design patterns
- JavaScript for interactive UI (search, filtering)
- File operations (CSV export, image generation)
- RESTful API design with JSON
- Real-world logistics concepts and tracking systems

---

## Key Information

### Default Credentials
| Field | Value |
|-------|-------|
| Username | demo |
| Password | demo123 |

### How Authentication Works
- Passwords are hashed using **Werkzeug's generate_password_hash** (scrypt algorithm)
- Hashes are stored in data/users.json
- If the file is missing, the app auto-creates it on startup with demo / demo123
- If the file exists with a broken hash, delete it and restart to regenerate

### Application URLs

| Route | Method | Purpose |
|-------|--------|---------|
| / | GET | Redirects to login or dashboard |
| /login | GET, POST | Login page |
| /dashboard | GET | Main dashboard (requires login) |
| /package/<id> | GET | Package lifecycle view (requires login) |
| /api/packages | GET | JSON API of all packages (requires login) |
| /export/csv | GET | Download CSV file (requires login) |
| /scan/<id>?action=shipped\|returned | GET | Simulate QR scan (no login required) |
| /logout | GET | Clear session and redirect to login |

### Why We Simulate Instead of Using Real QR Codes or IoT Sensors

A real-world reusable packaging tracker would likely use one of two approaches:

1. **Physical QR codes** printed on each package, scanned with a phone camera
2. **IoT sensors/RFID tags** that automatically report location and status

Both were deliberately left out of this project, in favor of a simple URL-based
simulation (`/scan/<id>?action=shipped|returned`). Reasons:

- **No physical device loop.** A real QR code only proves its value once someone
  scans it with a camera in the real world. On a local Flask app running on
  `localhost`, there's no phone, warehouse, or package to point a camera at, so a
  "real" QR image would just be a picture nobody actually scans - it adds
  complexity without adding a genuine test of the workflow.
- **No reliable local camera/network access.** Scanning a QR code requires a
  device with a camera that can reach the app's URL. On a student laptop
  (`localhost:5000`), that URL isn't reachable from a phone without extra network
  setup (same Wi-Fi, tunneling, HTTPS for camera permissions, etc.), which turns a
  five-minute demo into a networking exercise.
- **IoT would need real hardware.** RFID/IoT tracking needs physical tags,
  readers, and a device pipeline (MQTT broker, gateway, sensor firmware) - none of
  which exists in a local teaching app, and building a fake IoT simulator would be
  a bigger project than the tracking app itself.
- **The interesting part is the state machine, not the scan hardware.** What
  matters for teaching this project is the package lifecycle logic
  (`in_circulation → shipped → returned`), the metrics, and the API/UI around it.
  A scan is just an event that changes state - simulating that event with a URL
  hit teaches the exact same backend logic without the hardware dependency.
- **Fewer moving parts to fail during a presentation.** Camera permissions, image
  libraries (PIL), lighting conditions, and phone/laptop network reachability are
  all extra failure points that have nothing to do with the logistics concepts
  being taught.

**How the simulation works:**

- `/package/<id>` is the page a real QR code (or IoT tag lookup) would point to
- `/scan/<id>?action=shipped|returned` is the endpoint a real scan/sensor event
  would call - hitting it with `curl` or a browser stands in for "a scan just
  happened"
- The package detail page only shows the action button that is valid for the
  current status (`in_circulation → shipped → returned`), mirroring the
  state-machine validation a real scan- or sensor-based system would need
- Because the state machine and event history work identically either way, a real
  QR/IoT integration could be added later purely as a new *trigger* for the same
  `/scan/<id>` logic, without changing any of the tracking/metrics code

If you want real QR images later, generate them with the `qrcode` Python package
and add a route/button that serves the image for `/package/<id>`; that image would
just link to the same `/scan/<id>` endpoint that already exists.

---

## Testing the System

### Simulate QR Scans (no login needed)
```bash
# Mark package as shipped
curl http://localhost:5000/scan/PKG001?action=shipped

# Mark package as returned
curl http://localhost:5000/scan/PKG001?action=returned

# Create new package
curl http://localhost:5000/scan/PKG999?action=shipped
```

### Then refresh the dashboard to see updates

---

## Environmental Impact Model

Each returned package saves **0.5 kg of CO₂**:
```
CO₂ Saved = Number of Returned Packages × 0.5 kg
```

This encourages reuse and demonstrates sustainability benefits.

---

## Troubleshooting

**Port 5000 already in use?**
```bash
# Edit app.py, change line 249 from port=5000 to port=5001
```

**Module not found?**
```bash
pip install Flask==3.0.0 Werkzeug==3.0.1
```

**Can't login?**
1. Confirm you're using demo / demo123
2. If data/users.json exists with invalid hash, delete it and restart
3. Must start with python3 app.py (not flask run) for initialization

---

## Code Simplicity Notes

The code is intentionally simple for student presentations:

- **No ORM** - Direct JSON file handling is more transparent
- **Minimal JavaScript** - Only vanilla JS, no frameworks
- **Clear function names** - Every function's purpose is obvious
- **Single app.py** - All routes in one file for easy understanding
- **Template-based** - HTML templates are readable and modifiable
- **Comments in key places** - Explain WHY, not WHAT

This makes it easy to explain, modify, and extend during presentations.

---

## Presentation Tips

When presenting this project, focus on:

1. **User Flow** - Login → Dashboard → Package Details → QR Scan
2. **Data Model** - How packages and their history are stored
3. **Status Machine** - States and valid transitions
4. **UI/UX** - Card layouts, colors, responsiveness
5. **API Design** - How endpoints serve data to the frontend
6. **Scalability** - What would need to change for a real system (database, authentication)

---

## Data Files

### users.json
Contains user credentials with hashed passwords.
```json
{
  "demo": {
    "username": "demo",
    "password": "<hashed_password>"
  }
}
```

### packages.json
Stores packages with event history:
```json
{
  "PKG001": {
    "id": "PKG001",
    "created_at": "2024-01-15T10:00:00",
    "history": [
      {"status": "shipped", "timestamp": "2024-01-15T10:00:00"},
      {"status": "returned", "timestamp": "2024-01-20T14:30:00"}
    ]
  }
}
```

---

## Security Notes

**For Educational Use Only**

- Session secret key is hardcoded (change in production)
- Passwords stored with hash (good)
- No HTTPS/TLS (use in production)
- No rate limiting on login (add in production)
- CSRF protection not implemented (Flask can add this)
- No input sanitization (add HTML escaping in production)

---

**Happy learning!**

This project teaches real-world web development concepts through a practical logistics system.
