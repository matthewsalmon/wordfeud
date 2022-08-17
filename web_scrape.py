import httpx
import yaml

with open("scrape.yaml") as stream:
    config = yaml.safe_load(stream)

response = httpx.get(config['url1'])
html = response.text
metadata = response.headers
print(html)
print(metadata)
