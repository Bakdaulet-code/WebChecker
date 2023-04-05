import requests
from bs4 import BeautifulSoup

# The URL of the website to analyze
url = "https://www.example.com/"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all links on the page
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))

# Find all images on the page
images = []
for img in soup.find_all("img"):
    images.append(img.get("src"))

# Print the links and images for demonstration purposes
print("Links on the page:")
for link in links:
    print(link)

print("Images on the page:")
for image in images:
    print(image)
