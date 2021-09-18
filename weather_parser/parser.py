import typing

from requests import get, Response
from fake_useragent import UserAgent
from bs4 import BeautifulSoup, Tag, NavigableString

country: str = "russia"
city: str = "moskva"
url: str = f"https://www.foreca.ru/{country}/{city}"

ua: UserAgent = UserAgent()
headers = {
    'User-Agent': str(ua.chrome),
}

response: Response = get(url, headers=headers)
page: bytes = response.content

bs: BeautifulSoup = BeautifulSoup(page, "lxml")
block_temperature: typing.Union[Tag, NavigableString] = bs.find("div", {"class": ["table", "t_cond"]})
actual_weather: typing.Union[Tag, NavigableString] = block_temperature.find("div", {
    "class": ["left"]})
value_temperature: typing.Union[Tag, NavigableString] = actual_weather.find("span", {
    "class": ["warm", "txt-xxlarge"]})
print(value_temperature.text)
