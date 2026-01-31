
import sys
import os

# Ensure we can import from the current directory
sys.path.append(os.getcwd())

from personal_assistant.tools import _resolve_location

test_cases = [
    "Sikkim",
    "Goa",
    "Kerala",
    "Kolkata",
    "Delhi",
    "London" # Check international too
]

print("Verifying Geocoding Logic...")
for loc in test_cases:
    try:
        lat, lon, name = _resolve_location(loc)
        print(f"PASS: '{loc}' -> {name} ({lat}, {lon})")
    except Exception as e:
        print(f"FAIL: '{loc}' -> Error: {e}")
