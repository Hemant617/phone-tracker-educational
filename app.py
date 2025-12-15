#!/usr/bin/env python3
"""
Flask Web Application for Phone Tracker
Educational project demonstrating phone number analysis
"""

from flask import Flask, render_template, request, jsonify, send_file
from tracker import PhoneTracker
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# Initialize tracker
tracker = PhoneTracker()

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track():
    """
    Track phone number endpoint
    
    Returns:
        JSON response with tracking results
    """
    try:
        data = request.get_json()
        phone_number = data.get('phone_number', '').strip()
        
        if not phone_number:
            return jsonify({
                'success': False,
                'error': 'Phone number is required'
            }), 400
        
        # Track the phone number
        result = tracker.track(phone_number, create_map=True)
        
        if result['success']:
            # Get location data
            location = tracker.get_location(result['country'])
            result['location'] = location
            
            # Add timestamp
            result['timestamp'] = datetime.now().isoformat()
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        }), 500

@app.route('/validate', methods=['POST'])
def validate():
    """
    Quick validation endpoint
    
    Returns:
        JSON response with validation status
    """
    try:
        data = request.get_json()
        phone_number = data.get('phone_number', '').strip()
        
        if not phone_number:
            return jsonify({
                'valid': False,
                'message': 'Phone number is required'
            })
        
        result = tracker.parse_number(phone_number)
        
        return jsonify({
            'valid': result['success'],
            'message': 'Valid phone number' if result['success'] else result.get('error', 'Invalid')
        })
        
    except Exception as e:
        return jsonify({
            'valid': False,
            'message': str(e)
        })

@app.route('/map/<filename>')
def serve_map(filename):
    """Serve generated map files"""
    try:
        return send_file(filename, mimetype='text/html')
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'api_configured': tracker.api_key is not None
    })

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print("=" * 60)
    print("📱 PHONE TRACKER WEB APPLICATION")
    print("=" * 60)
    print("⚠️  FOR EDUCATIONAL PURPOSES ONLY")
    print("=" * 60)
    print("\n🚀 Starting server on http://localhost:5000")
    print("📝 Press CTRL+C to stop\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
