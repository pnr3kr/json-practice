import json
import requests

url = "https://raw.githubusercontent.com/uvasds-systems/DS2022/main/labs/data/schacon.repos.json"
response = requests.get(url)

data = response.json()  # Parse the JSON data

output_file = 'chacon.csv'

with open(output_file, 'w') as csv_file:
    for i, repo in enumerate(data[:5]):  # Limit to the first 5 repositories
        name = repo.get('name', 'N/A')
        html_url = repo.get('html_url', 'N/A')
        updated_at = repo.get('updated_at', 'N/A')
        visibility = repo.get('visibility', 'N/A')

        line = f"{name},{html_url},{updated_at},{visibility}\n"
        
        csv_file.write(line)
