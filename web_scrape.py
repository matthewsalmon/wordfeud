import httpx
response = httpx.get("https://wordfeud.aasmul.net/Account/Login.aspx")
html = response.text
metadata = response.headers
print(html)
print(metadata)
