import requests

host = "http://www.qichacha.com/search?key=%E6%95%99%E8%82%B2%E5%9F%B9%E8%AE%AD"

response = requests.get(host)
content = response.text
print(content)

