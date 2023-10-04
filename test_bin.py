import pytest
import requests 
from bs4 import BeautifulSoup

#url = "http://www.example.com"
#response = requests.get(url)
#print (response.content)


# send or post data 

#data = {"name": "Kam", "message": "How are you"}
#url = "https://httpbin.org/post"
#res = requests.post(url, json=data)
#es_data = res.json()
#print(res_data)

# handle error
#try: 
 #   res = requests.get("https://httpbin.org/status/200")
  #  res.raise_for_status()

#except res.exection.HTTPError as err:
   # print(f"HTTP Error : {err} ")


# timeout 

#url = "https://httpbin.org/delay/10"

#try: 
 #   res = requests.get(url, timeout= 5)    

#except requests.exection.HTTPError as err:
 #   print(f"HTTP Error : {err} ")



# setup header 

# auth_token = "xxxxxxxxx"
# headers = {"Authorization": f"Bearer {auth_token}"}
# url = "https://httpbin.org/headers"
# res = requests.get(url, headers=headers)
# print (res.json())


# Simple web SCRAPING 
url = "http://www.example.com"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")
# print(soup)
title = soup.title.text
content = soup.find("p").text
links =[a["href"] for a in soup.find_all("a")]
print (title , content, links)

