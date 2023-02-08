import time
import requests
import concurrent.futures
from bs4 import BeautifulSoup
import cv2
import numpy


def download_image(url):
    if not url.startswith("http"):
        # Add the missing scheme to the URL
        url = "https://" + url

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception("Failed to download image")
    except Exception as e:
        print(f"Error while downloading image from {url}: {e}")
        return None


def process_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    return blurred_image

def save_image(image, file_name):
    cv2.imwrite(file_name, image)

#
def process_image_sequentially():
    start = time.time()
    URL = "https://www.if.pw.edu.pl/~mrow/dyd/wdprir/"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = [img['src'] for img in soup.find_all('img') if img['src'].endswith(('.png', '.gif'))]

    for i, link in enumerate(links):
        image = download_image(link)
        image = cv2.imdecode(numpy.frombuffer(image, numpy.uint8), cv2.IMREAD_UNCHANGED)
        image = process_image(image)
        save_image(image, f"image_{i}.png")
    print("Sequential execution time: ", time.time() - start)

#
def process_image_concurrently():
    start = time.time()
    URL = "https://www.if.pw.edu.pl/~mrow/dyd/wdprir/"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = [img['src'] for img in soup.find_all('img') if img['src'].endswith(('.png', '.gif'))]

    with concurrent.futures.ThreadPoolExecutor() as executor: # fixed
        futures = [executor.submit(download_image, link) for link in links]
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            image = cv2.imdecode(numpy.frombuffer(future.result(), numpy.uint8), cv2.IMREAD_UNCHANGED)
            image = process_image(image)
            save_image(image, f"image_{i}.png")
    print("Concurrent execution time: ", time.time() - start)

if __name__ == "__main__":
    process_image_sequentially()
    process_image_concurrently()
