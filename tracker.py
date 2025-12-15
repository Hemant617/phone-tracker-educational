#!/usr/bin/env python3
"""
Phone Tracker - Educational Project
Demonstrates phone number analysis and geolocation concepts
"""

import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import folium
import os
from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv
import sys

# Load environment variables
load_dotenv()

class PhoneTracker:
    """Main phone tracking class for educational purposes"""
    
    def __init__(self, api_key=None):
        """Initialize the tracker with optional API key"""
        self.api_key = api_key or os.getenv('OPENCAGE_API_KEY')
        self.geocoder = OpenCageGeocode(self.api_key) if self.api_key else None
        
    def parse_number(self, phone_number):
        """
        Parse and validate phone number
        
        Args:
            phone_number (str): Phone number to parse
            
        Returns:
            dict: Parsed phone number information or error
        """
        try:
            # Parse the phone number
            parsed = phonenumbers.parse(phone_number)
            
            # Validate the number
            if not phonenumbers.is_valid_number(parsed):
                return {
                    'success': False,
                    'error': 'Invalid phone number'
                }
            
            # Extract information
            country = geocoder.description_for_number(parsed, 'en')
            carrier_name = carrier.name_for_number(parsed, 'en')
            timezones = timezone.time_zones_for_number(parsed)
            
            # Format number in international format
            international_format = phonenumbers.format_number(
                parsed, 
                phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
            
            # Get country code
            country_code = f"+{parsed.country_code}"
            
            return {
                'success': True,
                'number': international_format,
                'country': country or 'Unknown',
                'country_code': country_code,
                'carrier': carrier_name or 'Unknown',
                'timezones': list(timezones) if timezones else ['Unknown'],
                'is_valid': True,
                'national_number': parsed.national_number
            }
            
        except phonenumbers.NumberParseException as e:
            return {
                'success': False,
                'error': f'Parse error: {str(e)}'
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Unexpected error: {str(e)}'
            }
    
    def get_location(self, country_name):
        """
        Get approximate coordinates for a country
        
        Args:
            country_name (str): Name of the country
            
        Returns:
            dict: Location data with coordinates
        """
        if not self.geocoder:
            # Fallback coordinates for common countries
            fallback_coords = {
                'United States': (37.0902, -95.7129),
                'India': (20.5937, 78.9629),
                'United Kingdom': (55.3781, -3.4360),
                'Canada': (56.1304, -106.3468),
                'Australia': (-25.2744, 133.7751),
                'Germany': (51.1657, 10.4515),
                'France': (46.2276, 2.2137),
                'China': (35.8617, 104.1954),
                'Japan': (36.2048, 138.2529),
                'Brazil': (-14.2350, -51.9253)
            }
            
            coords = fallback_coords.get(country_name, (0, 0))
            return {
                'latitude': coords[0],
                'longitude': coords[1],
                'formatted': country_name
            }
        
        try:
            # Use OpenCage API for accurate geocoding
            results = self.geocoder.geocode(country_name)
            
            if results and len(results):
                location = results[0]['geometry']
                return {
                    'latitude': location['lat'],
                    'longitude': location['lng'],
                    'formatted': results[0]['formatted']
                }
            else:
                return {
                    'latitude': 0,
                    'longitude': 0,
                    'formatted': 'Unknown'
                }
                
        except Exception as e:
            print(f"Geocoding error: {e}")
            return {
                'latitude': 0,
                'longitude': 0,
                'formatted': 'Unknown'
            }
    
    def create_map(self, phone_info, output_file='phone_location.html'):
        """
        Create an interactive map showing phone number origin
        
        Args:
            phone_info (dict): Phone information from parse_number
            output_file (str): Output HTML file path
            
        Returns:
            str: Path to generated map file
        """
        if not phone_info['success']:
            return None
        
        # Get location coordinates
        location = self.get_location(phone_info['country'])
        
        # Create map centered on location
        phone_map = folium.Map(
            location=[location['latitude'], location['longitude']],
            zoom_start=5
        )
        
        # Create popup content
        popup_html = f"""
        <div style="font-family: Arial; width: 250px;">
            <h4 style="color: #2c3e50; margin-bottom: 10px;">📱 Phone Information</h4>
            <p><strong>Number:</strong> {phone_info['number']}</p>
            <p><strong>Country:</strong> {phone_info['country']}</p>
            <p><strong>Carrier:</strong> {phone_info['carrier']}</p>
            <p><strong>Timezone:</strong> {phone_info['timezones'][0]}</p>
            <p style="color: #e74c3c; font-size: 11px; margin-top: 10px;">
                ⚠️ Approximate location based on country code
            </p>
        </div>
        """
        
        # Add marker
        folium.Marker(
            [location['latitude'], location['longitude']],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=phone_info['country'],
            icon=folium.Icon(color='red', icon='phone', prefix='fa')
        ).add_to(phone_map)
        
        # Add circle to show approximate area
        folium.Circle(
            [location['latitude'], location['longitude']],
            radius=500000,  # 500km radius
            color='red',
            fill=True,
            fillColor='red',
            fillOpacity=0.1,
            popup='Approximate coverage area'
        ).add_to(phone_map)
        
        # Save map
        phone_map.save(output_file)
        return output_file
    
    def track(self, phone_number, create_map=True):
        """
        Complete tracking workflow
        
        Args:
            phone_number (str): Phone number to track
            create_map (bool): Whether to create a map visualization
            
        Returns:
            dict: Complete tracking results
        """
        # Parse phone number
        info = self.parse_number(phone_number)
        
        if not info['success']:
            return info
        
        # Create map if requested
        map_file = None
        if create_map:
            map_file = self.create_map(info)
        
        info['map_file'] = map_file
        return info


def main():
    """Command line interface"""
    print("=" * 60)
    print("📱 PHONE TRACKER - EDUCATIONAL PROJECT")
    print("=" * 60)
    print("⚠️  FOR EDUCATIONAL PURPOSES ONLY")
    print("=" * 60)
    print()
    
    if len(sys.argv) < 2:
        print("Usage: python tracker.py <phone_number>")
        print("Example: python tracker.py +1234567890")
        sys.exit(1)
    
    # Initialize tracker
    tracker = PhoneTracker()
    
    # Process each phone number
    for phone_number in sys.argv[1:]:
        print(f"\n🔍 Analyzing: {phone_number}")
        print("-" * 60)
        
        result = tracker.track(phone_number)
        
        if result['success']:
            print(f"✅ Valid Number: {result['number']}")
            print(f"🌍 Country: {result['country']} ({result['country_code']})")
            print(f"📡 Carrier: {result['carrier']}")
            print(f"🕐 Timezone: {', '.join(result['timezones'])}")
            
            if result['map_file']:
                print(f"🗺️  Map saved: {result['map_file']}")
        else:
            print(f"❌ Error: {result['error']}")
        
        print("-" * 60)


if __name__ == "__main__":
    main()
