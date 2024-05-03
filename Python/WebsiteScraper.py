import requests
from bs4 import BeautifulSoup

# Get the HTML content of the website
url = input("""enter url > """)
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract the text from the website
text = soup.get_text()

# Print the extracted text
print(text)
f = open("Article.txt","w")
f.write(text)
f.close()
