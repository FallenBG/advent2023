import re

text = "eighthree"
pattern = r"(?=(eight|three|one|two|four|five|six|seven|nine))"

# Find all matches in the text
matches = re.findall(pattern, text)

if matches:
    print("Found:", matches)
else:
    print("No match found")
