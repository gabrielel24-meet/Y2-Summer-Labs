import requests
import json

parameters = {"camera": "NAVCAM"} # Shows Navigation Camera photos only.

response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=faRn6vfvjvAmibI3UeuCfdYb3S4BFBP7rAPSfsu2", params = parameters)

parsed_content = json.loads(response.content)

Mars_pic = parsed_content["photos"][0]["img_src"]