import requests
import re

url = "https://www.python.org"

# Fetch webpage content
response = requests.get(url)

# Extract title
title = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)

if title:
    webpage_title = title.group(1)

    with open("title.txt", "w") as file:
        file.write(webpage_title)

    print("Title saved successfully!")
    print("Title:", webpage_title)
else:
    print("Title not found.")
