import requests
import pandas as pd

# Remplacez 'YOUR_API_KEY' par votre clé API d'Alpha Vantage
api_key = 'YOUR_API_KEY'

# Exemple d'API pour récupérer les indicateurs économiques des USA
url = f'https://www.alphavantage.co/query?function=INFLATION&apikey={api_key}'

response = requests.get(url)
data = response.json()

# Transformer les données en DataFrame
df = pd.DataFrame(data['data'])

# Sauvegarder les données dans un fichier CSV
df.to_csv('us_economic_events.csv', index=False)
print(df)
