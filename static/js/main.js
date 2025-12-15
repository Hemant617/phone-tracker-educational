// Phone Tracker - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('trackForm');
    const phoneInput = document.getElementById('phoneInput');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    const error = document.getElementById('error');

    // Form submission handler
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const phoneNumber = phoneInput.value.trim();
        
        if (!phoneNumber) {
            showError('Please enter a phone number');
            return;
        }

        // Reset UI
        hideAll();
        loading.classList.remove('hidden');

        try {
            // Send tracking request
            const response = await fetch('/track', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ phone_number: phoneNumber })
            });

            const data = await response.json();

            loading.classList.add('hidden');

            if (data.success) {
                displayResults(data);
            } else {
                showError(data.error || 'Failed to track phone number');
            }

        } catch (err) {
            loading.classList.add('hidden');
            showError('Network error. Please try again.');
            console.error('Error:', err);
        }
    });

    // Real-time validation
    phoneInput.addEventListener('input', debounce(async function() {
        const phoneNumber = phoneInput.value.trim();
        
        if (phoneNumber.length < 5) return;

        try {
            const response = await fetch('/validate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ phone_number: phoneNumber })
            });

            const data = await response.json();
            
            if (data.valid) {
                phoneInput.style.borderColor = '#27ae60';
            } else {
                phoneInput.style.borderColor = '#e74c3c';
            }

        } catch (err) {
            console.error('Validation error:', err);
        }
    }, 500));

    function displayResults(data) {
        // Populate information
        document.getElementById('phoneNumber').textContent = data.number;
        document.getElementById('country').textContent = data.country;
        document.getElementById('carrier').textContent = data.carrier;
        document.getElementById('timezone').textContent = data.timezones.join(', ');
        document.getElementById('countryCode').textContent = data.country_code;

        // Load map if available
        if (data.map_file) {
            const mapFrame = document.getElementById('mapFrame');
            mapFrame.src = `/map/${data.map_file}`;
        }

        // Show results
        results.classList.remove('hidden');
        
        // Smooth scroll to results
        results.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    function showError(message) {
        document.getElementById('errorMessage').textContent = message;
        error.classList.remove('hidden');
        error.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    function hideAll() {
        loading.classList.add('hidden');
        results.classList.add('hidden');
        error.classList.add('hidden');
    }

    // Debounce utility
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // Example phone numbers for quick testing
    const examples = [
        '+14155552671',  // US
        '+919876543210', // India
        '+442071234567', // UK
        '+61412345678',  // Australia
    ];

    // Add example buttons (optional enhancement)
    console.log('Example phone numbers for testing:', examples);
});

// Service Worker for offline capability (optional)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(reg => console.log('Service Worker registered'))
            .catch(err => console.log('Service Worker registration failed'));
    });
}
