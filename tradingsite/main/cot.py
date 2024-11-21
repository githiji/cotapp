from bs4 import BeautifulSoup
from .models import Stock, COTReport
import requests
import datetime

# Fetch the page
def fetch_page():
    html_page = requests.get('https://www.cftc.gov/dea/futures/deacmesf.htm').text
    soup = BeautifulSoup(html_page, 'html.parser')

# Extract the content inside the <pre> tag
    table = soup.find('pre').text
    return table

# Function to find data for a given market
def data_finder(market,table):
    lines = table.split('\n')  # Split the table into lines
    for i, line in enumerate(lines):
        if market in line:  # Search for the market in the line
            # Extract relevant data (assuming the structure has longs/shorts a couple of lines down)
            data_line = lines[i + 2]  # Modify this index if data is on a different line
            data_list = data_line.split()  # Split the data into individual numbers
            
            # Clean up data by removing commas and converting to integers
            clean_data = [int(num.replace(',', '')) for num in data_list if num.replace(',', '').isdigit()]
            
            return clean_data[0],clean_data[1]

# Example usage


# Save the data to the database
def save_data(market, longs, shorts):
    stock = Stock.objects.get(symbol=market)
    report = COTReport(market=stock, long_positions = longs, short_positions =shorts, report_date = datetime.date.today())
    report.save()

    
