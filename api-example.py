import requests

# Example of querying the API
result = requests.get('https://api.senticrypt.com/v1/bitcoin.json')
result = result.json()
print('Oldest result: {}'.format(result[0]))
print('Newest result: {}'.format(result[-1]))

# Example calculations
mean_times_rate = result[-1]['rate'] * results[-1]['mean']
median_times_rate = result[-1]['rate'] * results[-1]['median']

if median_times_rate > mean_times_rate:
  print('BUY')
  
