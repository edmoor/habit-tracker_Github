import requests
from datetime import datetime

USERNAME = "XXXXXXXX"
TOKEN = "XXXXXXXXX"
GRAPH_ID = "graph1"

# Create account
pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=pixela_endpoint, json=user_parameters)
print(response.text)

# Create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_configuration = {
    "id": "graph1",
    "name": "Running Tracker",
    "unit": "Km",
    "type": "float",
    "color": "ichou"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)

# Add pixel
new_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today_date = datetime.now()
pixel_configuration = {
    "date": today_date.strftime("%Y%m%d"),
    "quantity": input("How many Kilometers did you run?")
}
response_post = requests.post(url=new_pixel_endpoint, json=pixel_configuration, headers=headers)

# Update pixel
change_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240614"
new_pixel_configuration = {
    "quantity": "8"
}
response_put = requests.put(url=change_pixel_endpoint, json=new_pixel_configuration, headers=headers)

# Delete pixel
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240614"
response_delete = requests.delete(url=delete_pixel_endpoint, json=new_pixel_configuration, headers=headers)
