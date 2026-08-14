"""
GreenLoop - Reusable Packaging Tracking Platform
A simple Flask application for tracking reusable packages and their environmental impact
"""

from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import json
import os
from datetime import datetime
import io
import csv

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'greenloop-secret-key-2024'

# Paths to JSON data files
DATA_DIR = 'data'
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
PACKAGES_FILE = os.path.join(DATA_DIR, 'packages.json')


def load_json(filepath):
    """Load JSON data from file"""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)


def save_json(filepath, data):
    """Save JSON data to file"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)


def login_required(f):
    """Decorator to check if user is logged in"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def get_package_status(package):
    """Get the current status of a package"""
    if not package.get('history') or len(package['history']) == 0:
        return 'in_circulation'
    return package['history'][-1]['status']


def calculate_metrics():
    """Calculate key metrics from all packages"""
    packages = load_json(PACKAGES_FILE)
    
    total = len(packages)
    shipped_count = 0
    returned_count = 0
    
    for pkg_id, pkg_data in packages.items():
        status = get_package_status(pkg_data)
        if status == 'shipped':
            shipped_count += 1
        elif status == 'returned':
            returned_count += 1
    
    co2_saved = returned_count * 0.5
    
    return {
        'total': total,
        'shipped': shipped_count,
        'returned': returned_count,
        'in_circulation': total - shipped_count - returned_count,
        'co2_saved': round(co2_saved, 2)
    }


def get_recent_activity(limit=5):
    """Get recent scan events"""
    packages = load_json(PACKAGES_FILE)
    events = []

    for pkg_id, pkg_data in packages.items():
        for event in pkg_data.get('history', []):
            events.append({
                'package_id': pkg_id,
                'status': event['status'],
                'timestamp': event['timestamp']
            })

    events.sort(key=lambda x: x['timestamp'], reverse=True)
    return events[:limit]


def get_package_by_id(package_id):
    """Get a single package by ID"""
    packages = load_json(PACKAGES_FILE)
    if package_id in packages:
        pkg = packages[package_id].copy()
        pkg['current_status'] = get_package_status(pkg)
        return pkg
    return None


@app.route('/')
def index():
    """Redirect to dashboard if logged in, otherwise to login"""
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        # Form validation
        if not username:
            return render_template('login.html', error='Username is required')
        if not password:
            return render_template('login.html', error='Password is required')

        users = load_json(USERS_FILE)

        if username in users and check_password_hash(users[username]['password'], password):
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')


@app.route('/logout')
def logout():
    """Logout"""
    session.clear()
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    """Main dashboard page"""
    metrics = calculate_metrics()
    recent_events = get_recent_activity(limit=5)
    current_user = session.get('user')
    
    return render_template(
        'dashboard.html',
        metrics=metrics,
        recent_events=recent_events,
        current_user=current_user
    )


@app.route('/scan/<package_id>')
def scan_package(package_id):
    """Simulate QR code scan"""
    action = request.args.get('action', 'shipped')
    
    if action not in ['shipped', 'returned']:
        return jsonify({'error': 'Invalid action. Use "shipped" or "returned"'}), 400
    
    packages = load_json(PACKAGES_FILE)
    
    if package_id not in packages:
        packages[package_id] = {
            'id': package_id,
            'created_at': datetime.now().isoformat(),
            'history': []
        }
    
    event = {
        'status': action,
        'timestamp': datetime.now().isoformat()
    }
    packages[package_id]['history'].append(event)
    
    save_json(PACKAGES_FILE, packages)
    
    return jsonify({
        'success': True,
        'package_id': package_id,
        'status': action,
        'timestamp': event['timestamp'],
        'message': f'Package {package_id} marked as {action}'
    })


@app.route('/api/packages')
@login_required
def api_packages():
    """API endpoint to get all packages"""
    packages = load_json(PACKAGES_FILE)

    for pkg_id, pkg_data in packages.items():
        pkg_data['current_status'] = get_package_status(pkg_data)

    return jsonify(packages)


@app.route('/package/<package_id>')
@login_required
def package_detail(package_id):
    """Package lifecycle view"""
    package = get_package_by_id(package_id)

    if not package:
        return render_template('package_detail.html', error=f'Package {package_id} not found'), 404

    return render_template('package_detail.html', package=package)


@app.route('/package/<package_id>/update-status', methods=['POST'])
@login_required
def update_package_status(package_id):
    """Update package status based on current state"""
    package = get_package_by_id(package_id)

    if not package:
        return jsonify({'error': 'Package not found'}), 404

    current_status = package['current_status']

    # State machine: in_circulation → shipped → returned
    if current_status == 'in_circulation':
        new_status = 'shipped'
    elif current_status == 'shipped':
        new_status = 'returned'
    else:
        # Already returned, no more transitions
        return jsonify({'error': 'Package is already returned'}), 400

    # Add event to package history
    packages = load_json(PACKAGES_FILE)
    event = {
        'status': new_status,
        'timestamp': datetime.now().isoformat()
    }
    packages[package_id]['history'].append(event)
    save_json(PACKAGES_FILE, packages)

    return jsonify({
        'success': True,
        'package_id': package_id,
        'new_status': new_status,
        'timestamp': event['timestamp']
    })


@app.route('/export/csv')
@login_required
def export_csv():
    """Export all packages to CSV"""
    packages = load_json(PACKAGES_FILE)

    # Create CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)

    # Write header
    writer.writerow(['Package ID', 'Created At', 'Current Status', 'Last Updated', 'Events Count'])

    # Write package data
    for pkg_id, pkg_data in sorted(packages.items()):
        current_status = get_package_status(pkg_data)
        last_updated = pkg_data['history'][-1]['timestamp'] if pkg_data.get('history') else 'N/A'
        events_count = len(pkg_data.get('history', []))

        writer.writerow([
            pkg_id,
            pkg_data['created_at'],
            current_status,
            last_updated,
            events_count
        ])

    # Return as file download
    output.seek(0)
    output_bytes = io.BytesIO(output.getvalue().encode('utf-8'))
    output_bytes.seek(0)

    return send_file(
        output_bytes,
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'packages_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    )


def initialize_default_data():
    """Create default users and sample packages"""
    
    if not os.path.exists(USERS_FILE):
        users = {
            'demo': {
                'username': 'demo',
                'password': generate_password_hash('demo123')
            }
        }
        save_json(USERS_FILE, users)
        print("✓ Created default user: demo / demo123")
    
    if not os.path.exists(PACKAGES_FILE):
        packages = {
            'PKG001': {
                'id': 'PKG001',
                'created_at': '2024-01-15T10:00:00',
                'history': [
                    {'status': 'shipped', 'timestamp': '2024-01-15T10:00:00'},
                    {'status': 'returned', 'timestamp': '2024-01-20T14:30:00'}
                ]
            },
            'PKG002': {
                'id': 'PKG002',
                'created_at': '2024-01-16T09:30:00',
                'history': [
                    {'status': 'shipped', 'timestamp': '2024-01-16T09:30:00'}
                ]
            },
            'PKG003': {
                'id': 'PKG003',
                'created_at': '2024-01-17T11:00:00',
                'history': [
                    {'status': 'shipped', 'timestamp': '2024-01-17T11:00:00'},
                    {'status': 'returned', 'timestamp': '2024-01-22T16:45:00'}
                ]
            }
        }
        save_json(PACKAGES_FILE, packages)
        print("✓ Created sample packages: PKG001, PKG002, PKG003")


if __name__ == '__main__':
    initialize_default_data()
    
    print("\n" + "="*60)
    print("GreenLoop - Reusable Packaging Tracking Platform")
    print("="*60)
    print("\n📍 Open your browser and navigate to:")
    print("   http://localhost:5000")
    print("\n🔐 Default credentials:")
    print("   Username: demo")
    print("   Password: demo123")
    print("\n" + "="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
