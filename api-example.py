import requests

# Example of querying the API
result = requests.get('https://api.senticrypt.com/v1/bitcoin.json')
result = result.json()
print('Oldest result: {}'.format(result[0]))
print('Newest result: {}'.format(result[-1]))

# Example calculations
mean_sentiment = result[-1]['mean']
median_sentiment = result[-1]['median']
rate = result[-1]['rate']

if median_sentiment > mean_sentiment and rate > 1:
    print('BUY')
