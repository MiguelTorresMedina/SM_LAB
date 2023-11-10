import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url, table_class):
    # URL of the webpage
    url = "https://www.mapa.gob.es/es/alimentacion/temas/consumo-tendencias/panel-de-consumo-alimentario/series-anuales/"
    table_class = "your-table-class"  # Replace with the actual class of the table
    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table on the page (adjust the tag and class based on the webpage structure)
        table = soup.find('table', class_=table_class)

        # Extract data from the table and store it in a list of dictionaries
        data = []
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            if columns:
                data.append([col.text.strip() for col in columns])

        # Convert the list of dictionaries into a Pandas DataFrame
        columns = [col.text.strip() for col in table.find('tr').find_all('th')]  # Assuming the first row is the header
        df = pd.DataFrame(data, columns=columns)

        return df

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None



# Call the function
#result_df = scrape_website(url, table_class)

# Check if the DataFrame is not empty before further processing
#if result_df is not None and not result_df.empty:
    # Save the DataFrame to a CSV file or perform further analysis
#    result_df.to_csv('output_dataset.csv', index=False)
#else:
#    print("No data to process.")
