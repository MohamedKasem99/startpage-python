import requests
from bs4 import BeautifulSoup
import time

class Startpage():
    def __init__(self):
        self.COOLDOWN_DELAY = 2
        self._prev_query = None
        self.headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Origin': 'https://www.startpage.com',
        'Referer': 'https://www.startpage.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
    }

        self.data = {
        't': '',
        'lui': 'english',
        'sc': 'nMI2Y8LueXGa20',
        'cat': 'web',
    }

    def get_html(self, term):
        response = requests.post(
            'https://www.startpage.com/sp/search', headers=self.headers, data=dict(
                **self.data,
                query=term
            ))
        response.raise_for_status()
        return response.text


    def _cooldown(self):
        now = int(time.time())
        if not isinstance(self._prev_query, int):
            waittime = 0
        else:
            waittime = self.COOLDOWN_DELAY - (now - self._prev_query)
            if waittime < 0:
                waittime = 0
        time.sleep(waittime)
        self._prev_query = int(time.time())

    def search(self, term):
        self._cooldown()
        html = self.get_html(term)
        # Parse
        soup = BeautifulSoup(html, "html.parser")
        result_block = soup.find_all("div", attrs={"class": "w-gl__result"})
        results = []
        for result in result_block:
            link = result.find("a", attrs={'class': "w-gl__result-url"}, href=True)
            results.append(link["href"])
        return results