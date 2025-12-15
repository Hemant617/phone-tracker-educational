# 🚀 Quick Start Guide

Get up and running with Phone Tracker in 5 minutes!

## Prerequisites

- Python 3.8+ installed
- pip package manager
- Internet connection

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/Hemant617/phone-tracker-educational.git
cd phone-tracker-educational
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment (Optional)

For enhanced geocoding features:

```bash
# Copy example environment file
cp .env.example .env

# Edit .env and add your OpenCage API key
# Get free key from: https://opencagedata.com/
```

## Usage Options

### Option 1: Command Line Interface

```bash
# Basic usage
python tracker.py +1234567890

# Multiple numbers
python tracker.py +14155552671 +919876543210

# With detailed output
python tracker.py +442071234567 --detailed
```

### Option 2: Web Interface

```bash
# Start the web server
python app.py

# Open your browser to:
# http://localhost:5000
```

## Example Phone Numbers for Testing

Try these valid phone numbers:

- **USA**: +14155552671
- **India**: +919876543210
- **UK**: +442071234567
- **Australia**: +61412345678
- **Germany**: +4915123456789
- **France**: +33612345678

## Features You Can Try

1. **Validate Phone Numbers**
   - Enter any phone number with country code
   - See if it's valid or invalid

2. **Get Country Information**
   - Automatically detects country from code
   - Shows country name and code

3. **Carrier Detection**
   - Identifies mobile carrier/operator
   - Works for most major carriers

4. **Timezone Information**
   - Shows timezone(s) for the number
   - Useful for international calls

5. **Visual Map**
   - Interactive map showing approximate location
   - Based on country, not GPS tracking

## Common Issues & Solutions

### Issue: Module not found
```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

### Issue: Port 5000 already in use
```bash
# Solution: Use different port
python app.py --port 8000
```

### Issue: Invalid phone number error
```bash
# Solution: Always include country code
# ✅ Correct: +14155552671
# ❌ Wrong: 4155552671
```

## Project Structure

```
phone-tracker-educational/
├── tracker.py          # Core logic (CLI)
├── app.py             # Web application
├── requirements.txt   # Dependencies
├── templates/         # HTML templates
│   └── index.html
├── static/           # CSS & JavaScript
│   ├── css/style.css
│   └── js/main.js
└── README.md         # Documentation
```

## Next Steps

1. ✅ Try tracking different phone numbers
2. ✅ Explore the web interface
3. ✅ Read the full README.md
4. ✅ Check out the code to learn
5. ✅ Contribute improvements!

## Learning Resources

- [Phone Number Standards (E.164)](https://en.wikipedia.org/wiki/E.164)
- [Python phonenumbers Library](https://github.com/daviddrysdale/python-phonenumbers)
- [Flask Web Framework](https://flask.palletsprojects.com/)
- [Folium Mapping](https://python-visualization.github.io/folium/)

## Need Help?

- 📖 Read the [README.md](README.md)
- 🐛 Report issues on GitHub
- 💬 Ask questions in Discussions
- 🤝 Check [CONTRIBUTING.md](CONTRIBUTING.md)

## Important Reminders

⚠️ **Educational Purpose Only**
- This is a learning project
- Always get consent before tracking
- Respect privacy laws
- Use responsibly

---

Happy Learning! 🎓

Made with ❤️ for education
