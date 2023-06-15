import re
from geotext import GeoText
from usaddress import parse, tag

def extract_address(resume_text):
    # Extract potential locations using GeoText
    places = GeoText(resume_text)
    locations = places.cities + places.countries

    if locations:
        # Combine potential locations into a single string
        address = ' '.join(locations)
        address = re.sub(r'\b(\w+),$', r'\1', address)  # Remove trailing comma

        # Use usaddress library to parse and tag address components
        parsed_address = parse(address)
        tagged_address = tag(address)

        # Filter and combine tagged address components
        filtered_address = []
        for component, tag in tagged_address:
            if 'Address' in tag:
                filtered_address.append(component)
        
        final_address = ' '.join(filtered_address)
        return final_address
    else:
        return None

# Read resume text from a text file
file_path = 'static/uploads/Resumewords.txt'
try:
    with open(file_path, 'r') as file:
        resume_text = file.read()
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
    exit()

address = extract_address(resume_text)

if address:
    print("Address:", address)
else:
    print("Address not found in the resume.")
