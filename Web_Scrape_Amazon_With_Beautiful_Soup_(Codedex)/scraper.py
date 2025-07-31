import requests
from bs4 import BeautifulSoup

# Set up headers to mimic a real browser (helps avoid bot detection)
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
  'Accept-Language': 'en-US,en;q=0.5'
}

# Function to get the product title and price from a given Amazon product URL
def get_product_details(product_url: str) -> dict:
  
  product_details = {}  # Dictionary to store the scraped data

  # Send a GET request to the product page
  page = requests.get(product_url, headers=headers)

  # Parse the HTML content of the page with BeautifulSoup
  soup = BeautifulSoup(page.content, features="lxml")

  try:
    # Try to find and clean up the product title
    title = soup.find('span', attrs={'id': 'productTitle'}).get_text().strip()

    # Grab the price – sometimes there are multiple "a-price" elements,
    # but this usually grabs the first one (the main one displayed)
    extracted_price = soup.find('span', attrs={'class': 'a-price'}).get_text().strip()

    # Extract just the number from the price string
    price = '$' + extracted_price.split('$')[1]

    # Save to the dictionary
    product_details['title'] = title
    product_details['price'] = price

    return product_details

  except Exception as e:
    # If anything goes wrong (like the selectors not being found), show an error
    print('Could not fetch product details')
    print(f'Failed with exception: {e}')

# Prompt the user to enter a product URL
product_url = input('Enter product url: ')

# Get and print the product details
product_details = get_product_details(product_url)
print(product_details)
