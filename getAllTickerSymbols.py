from email import header
import requests
from decouple import config

iexToken=config('iexToken')

response = requests.get(
  'https://cloud.iexapis.com/beta/ref-data/symbols?',
  params={'token':iexToken}
)

print(response.json());