# 📱 Phone Tracker - Educational Project

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Educational-orange.svg)

## ⚠️ IMPORTANT DISCLAIMER

**THIS PROJECT IS FOR EDUCATIONAL PURPOSES ONLY**

This project demonstrates phone number analysis and geolocation concepts for learning purposes. It does NOT:
- Track real-time phone locations
- Access private user data
- Violate privacy laws
- Work without proper authorization

**Legal Notice:** Tracking someone's phone without their explicit consent is illegal in most jurisdictions. This tool is meant to teach programming concepts, API integration, and geolocation basics.

## 🎯 What This Project Does

- Validates phone numbers
- Extracts country and carrier information
- Shows approximate location based on country code
- Displays timezone information
- Generates visual maps of phone number origins

## 🚀 Features

- ✅ Phone number validation and formatting
- ✅ Country and region detection
- ✅ Carrier identification
- ✅ Timezone information
- ✅ Interactive map visualization
- ✅ Web-based user interface
- ✅ Batch processing support

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection for API calls

## 🔧 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Hemant617/phone-tracker-educational.git
cd phone-tracker-educational
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up API keys (optional):**
Create a `.env` file in the root directory:
```env
OPENCAGE_API_KEY=your_api_key_here
```

Get a free API key from [OpenCage](https://opencagedata.com/)

## 💻 Usage

### Command Line Interface

```bash
# Basic usage
python tracker.py +1234567890

# Multiple numbers
python tracker.py +1234567890 +4412345678

# With detailed output
python tracker.py +1234567890 --detailed
```

### Web Interface

```bash
# Start the web server
python app.py

# Open browser to http://localhost:5000
```

## 📁 Project Structure

```
phone-tracker-educational/
├── tracker.py          # Core tracking logic
├── app.py             # Flask web application
├── requirements.txt   # Python dependencies
├── .env.example       # Environment variables template
├── .gitignore        # Git ignore rules
├── LICENSE           # MIT License
├── README.md         # This file
├── static/           # Static files (CSS, JS)
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── templates/        # HTML templates
    └── index.html
```

## 🛠️ Technologies Used

- **Python 3.8+** - Core programming language
- **phonenumbers** - Phone number parsing and validation
- **Flask** - Web framework
- **folium** - Interactive maps
- **opencage** - Geocoding API
- **python-dotenv** - Environment variable management

## 📚 How It Works

1. **Phone Number Parsing:** Uses the `phonenumbers` library to parse and validate phone numbers
2. **Information Extraction:** Extracts country code, carrier, and region data
3. **Geolocation:** Uses country code to determine approximate location
4. **Visualization:** Creates interactive maps using Folium
5. **Web Interface:** Flask serves a user-friendly web interface

## 🎓 Educational Value

This project teaches:
- API integration and usage
- Phone number formatting standards (E.164)
- Geolocation concepts
- Web development with Flask
- Data visualization
- Error handling and validation
- Environment variable management

## ⚖️ Legal & Ethical Considerations

- Always obtain explicit consent before tracking
- Respect privacy laws (GDPR, CCPA, etc.)
- Use only for authorized purposes
- Understand local regulations
- Never use for stalking or harassment

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Resources

- [phonenumbers Documentation](https://github.com/daviddrysdale/python-phonenumbers)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [OpenCage API](https://opencagedata.com/)
- [Folium Documentation](https://python-visualization.github.io/folium/)

## 👨‍💻 Author

Created by Hemant617 for educational purposes.

## 🙏 Acknowledgments

- Google's libphonenumber library
- OpenCage Geocoding API
- Flask community
- Open source contributors

---

**Remember:** With great power comes great responsibility. Use this knowledge ethically and legally.
