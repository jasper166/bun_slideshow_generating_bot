import os
import requests
from duckduckgo_search import DDGS
from fastcore.all import *
from PIL import Image

max_img = 5
def search_images(term, max_images=max_img):
    print(f"Searching for '{term}'")
    with DDGS() as ddgs:
        search_results = ddgs.images(keywords=term)
        image_data = list(search_results)
        image_urls = [item.get("image") for item in image_data[:max_images]]
        return L(image_urls)
    
def download_images(keyword, folder_path, max_images=10):
    urls = search_images(keyword, max_images)
    os.makedirs(folder_path, exist_ok=True)
    for i, url in enumerate(urls):
        image_filename = f"{keyword}_{i + 1}.jpg"
        image_path = os.path.join(folder_path, image_filename)
        try:
            img_data = requests.get(url).content
            img = Image.open(io.BytesIO(img_data))
            img.verify()
            with open(image_path, "wb") as f:
                f.write(img_data)
            print(f"Downloaded: {image_filename}")
        except Exception as e:
            print(f"Error downloading {image_filename}: {e}")




keywords_list = ["Design Thinking", "creativity", "users", "improvement"]
for keyword in keywords_list:
    # folder_name = keyword.replace(" ", "_").lower()
    folder_name = "img"
    download_images(keyword, folder_path=folder_name, max_images=max_img)
    print(f"Images for '{keyword}' saved in folder: {folder_name}")