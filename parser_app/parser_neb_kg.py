import requests
from bs4 import BeautifulSoup

URL = "https://neb.kg/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
}

def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


def get_data(html):
    bs = BeautifulSoup(html, features="html.parser")
    items = bs.find_all("div", class_="itemContainer itemContainerLast")
    neb_kg_list = []
    for item in items:
        title = item.find("h3", class_="catItemTitle").get_text(strip=True)
        neb_kg_list.append({
            "title": title,
        })
    return neb_kg_list


def parsing_neb_kg():
    response = get_html(URL)
    if response.status_code == 200:
        neb_kg_list2 = []
        for page in range(1, 2):
            response = get_html("https://neb.kg/index.php/ru/component/jak2filter/?Itemid=226&issearch=1&category_id=1,2,3,4,5,6,7,8,9,10&xf_2=2", params={"page": page})
            neb_kg_list2.extend(get_data(response.text))
        return neb_kg_list2
    else:
        raise Exception("error in parsing")

# print(parsing_neb_kg())